#!/usr/bin/env python3
# Generate CSS files for various Nerd Fonts.

import base64
import json
import sys
import pathlib
import urllib.error
import urllib.request
import os

NF_RELEASE_TAG = "v3.4.0"

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
    print(url)
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as r:
        assert r.getcode() == 200
        data = r.read()
        return base64.b64encode(data).decode("utf-8")


def generate_css(fonts, base_url, is_nerd_font, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    for font, paths in fonts.items():
        name = paths.get("name", font)
        if is_nerd_font:
            name = name + " Nerd Font"

        filename = os.path.join(output_dir, f"{name}.css")
        if "regular" not in paths:
            print(f"Incomplete: {filename}")
            continue
        else:
            print(f"Creating: {filename}")

        extension = pathlib.Path(paths["regular"]).suffix.replace(".", "")

        with open(filename, "w") as fd:
            for weight, template in (
                ("regular", CSS_TEMPLATE_REGULAR),
                ("bold", CSS_TEMPLATE_BOLD),
                ("italic", CSS_TEMPLATE_ITALIC),
                ("bold_italic", CSS_TEMPLATE_BOLD_ITALIC),
            ):
                if weight not in paths:
                    continue
                params = urllib.parse.quote(f"{font}/{paths[weight]}")
                b64_data = download_as_base64(
                    f"{base_url}/{params}",
                )
                fd.write(
                    template.format(name=name, b64_data=b64_data, extension=extension)
                )


def unpatched_fonts():
    with open("fonts-unpatched.json", "r") as fd:
        fonts = json.load(fd)
        generate_css(
            fonts,
            f"https://github.com/ryanoasis/nerd-fonts/raw/refs/tags/{NF_RELEASE_TAG}/src/unpatched-fonts",
            False,
            output_dir="unpatched",
        )


def patched_fonts():
    with open("fonts-patched.json", "r") as fd:
        fonts = json.load(fd)
        generate_css(
            fonts,
            f"https://github.com/ryanoasis/nerd-fonts/raw/refs/tags/{NF_RELEASE_TAG}/patched-fonts",
            True,
            output_dir="patched",
        )


if __name__ == "__main__":
    unpatched_fonts()
    patched_fonts()
