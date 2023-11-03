#!/usr/bin/env python3
# Generate CSS files for various Nerd Fonts.

import base64
import json
import sys
import pathlib
import urllib.error
import urllib.request


CSS_TEMPLATE_REGULAR = """\
@font-face {{
    font-family: "{name}";
    font-style: normal;
    font-weight: 400;
    src: url(data:font/{extension};charset-utf-8;base64,{b64_data});
}}
"""
CSS_TEMPLATE_BOLD = """\
@font-face {{
    font-family: "{name}";
    font-style: normal;
    font-weight: 700;
    src: url(data:font/{extension};charset-utf-8;base64,{b64_data});
}}
"""
CSS_TEMPLATE_ITALIC = """\
@font-face {{
    font-family: "{name}";
    font-style: italic;
    font-weight: 400;
    src: url(data:font/{extension};charset-utf-8;base64,{b64_data});
}}
"""
CSS_TEMPLATE_BOLD_ITALIC = """\
@font-face {{
    font-family: "{name}";
    font-style: italic;
    font-weight: 700;
    src: url(data:font/{extension};charset-utf-8;base64,{b64_data});
}}
"""


def download_as_base64(url):
    # 'https://github.com/ryanoasis/nerd-fonts/raw/master/patched-fonts/{font}/{regular}'
    print(url)
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as r:
        assert r.getcode() == 200
        data = r.read()
        return base64.b64encode(data).decode('utf-8')


def generate_css(fonts, base_url, is_nerd_font):
    for font, paths in fonts.items():
        name = paths.get('name', font)
        if is_nerd_font:
            name = name + " Nerd Font"

        filename = '%s.css' % name
        if not 'regular' in paths:
            print('Incomplete: ' + filename)
            continue
        else:
            print('Creating: ' + filename)

        extension = pathlib.Path(paths['regular']).suffix.replace('.', '')

        with open(filename, 'w') as fd:
            for (weight, template) in (('regular', CSS_TEMPLATE_REGULAR),
                        ('bold', CSS_TEMPLATE_BOLD),
                        ('italic', CSS_TEMPLATE_ITALIC),
                        ('bold_italic', CSS_TEMPLATE_BOLD_ITALIC)):
                if not weight in paths:
                    continue
                params = urllib.parse.quote('%s/%s' % (font, paths[weight]))
                b64_data = download_as_base64(
                    base_url + '/%s' % (params),
                )
                fd.write(template.format(name = name, b64_data = b64_data, extension = extension))


def unpatched_fonts():
    with open('fonts-unpatched.json', 'r') as fd:
        fonts = json.load(fd)
        generate_css(fonts, 'https://github.com/ryanoasis/nerd-fonts/raw/master/src/unpatched-fonts', False)

def patched_fonts():
    with open('fonts-patched.json', 'r') as fd:
        fonts = json.load(fd)
        generate_css(fonts, 'https://github.com/ryanoasis/nerd-fonts/raw/master/patched-fonts', True)

if __name__ == '__main__':
    unpatched_fonts()
