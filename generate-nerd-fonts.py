#!/usr/bin/env python3
# Generate CSS files for various Nerd Fonts.

import base64
import json
import sys
import urllib.error
import urllib.request


CSS_TEMPLATE = """\
@font-face {{
    font-family: "{name} Nerd Font";
    font-style: normal;
    font-weight: 400;
    src: url(data:font/ttf;charset-utf-8;base64,{regular});
}}
@font-face {{
    font-family: "{name} Nerd Font";
    font-style: normal;
    font-weight: 700;
    src: url(data:font/ttf;charset-utf-8;base64,{bold});
}}
@font-face {{
    font-family: "{name} Nerd Font";
    font-style: italic;
    font-weight: 400;
    src: url(data:font/ttf;charset-utf-8;base64,{italic});
}}
@font-face {{
    font-family: "{name} Nerd Font";
    font-style: italic;
    font-weight: 700;
    src: url(data:font/ttf;charset-utf-8;base64,{bold_italic});
}}
"""


def download_as_base64(url):
    # 'https://github.com/ryanoasis/nerd-fonts/raw/master/patched-fonts/{font}/{regular}'
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as r:
        data = r.read()
        return base64.b64encode(data).decode('utf-8')


def generate_css(fonts):
    for font, paths in fonts.items():
        name = paths.get('name', font)
        name_esc = name.replace(' ', '%20')
        filename = '%s Nerd Font.css' % name
        print('Creating: ' + filename)
        with open(filename, 'w') as fd:
            args = {
                'font': font,
                'name': name,
                'regular': 'Regular/complete/{}%20Regular%20Nerd%20Font%20Complete.ttf'.format(name_esc),
                'bold': 'Bold/complete/{}%20Bold%20Nerd%20Font%20Complete.ttf'.format(name_esc),
                'italic': 'Italic/complete/{}%20Italic%20Nerd%20Font%20Complete.ttf'.format(name_esc),
                'bold_italic': 'Bold-Italic/complete/{}%20Bold%20Italic%20Nerd%20Font%20Complete.ttf'.format(name_esc),
            }
            args.update(paths)
            for key in ('regular', 'bold', 'italic', 'bold_italic'):
                args[key] = download_as_base64(
                    'https://github.com/ryanoasis/nerd-fonts/raw/master/patched-fonts/%s/%s' % (font, args[key]),
                )
            fd.write(CSS_TEMPLATE.format(**args))


def main():
    with open('nerd-fonts.json', 'r') as fd:
        fonts = json.load(fd)
    generate_css(fonts)


if __name__ == '__main__':
    main()
