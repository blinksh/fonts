# [Blink Shell](http://www.blink.sh) Fonts

With [Blink Shell](http://www.blink.sh) you can have your terminal, your way. We know how important it is for you to have your [color scheme](https://github.com/blinksh/themes) and the font that you feel comfortable looking at all day. And don't forget to send us your PRs to share them with others too!

Although [iOS now supports installing fonts at the OS level](https://9to5mac.com/2019/06/12/ios-13-how-to-use-custom-fonts-on-iphone-and-ipad/), the process is still cumbersome.

In this gallery you will find a wide range of Monospace fonts, both unpatched and patched with Nerd Fonts for new CLI editors. All the included fonts should work right out of the box with Blink. To install them, just paste the URL of the CSS font under Appearance -> Fonts -> New Font.

Some of the fonts in this gallery were only designed in a single weight. Terminals now render bold, italic and bold-italic weights, and consequently we recommend using a font that includes all the variants. Using a font family that misses a specific weight will render ok but it may not align in the terminal. This is specially true of bold fonts, in that case you can disable them within Settings and enable "bold as bright" instead. 

To help you select a complete font, we have marked which ones are complete in the Font Families table.

Our main feeds are based on the [Nerd-Fonts repository](https://github.com/ryanoasis/nerd-fonts font aggregator), so to their maintainers goes all the credit.

Check also the [Themes Gallery](https://github.com/blinksh/themes)

You can also find about [Blink's official repository](https://github.com/blinksh/blink)

## Contributing
This repository consists of the generate_fonts.py script and the JSON feeds that point to locations where to download the font families. At the moment, the feeds will read from the Nerd Fonts repository to package all the variants as CSS files by Blink. The output CSS fonts are subsequently stored into two collections: patched and unpatched. Because files are really heavy, these collections are submodules to handle them as their own repositories.

Our plan is to keep our main feeds tied to the Nerd Fonts collection, and we accept new feeds for other fonts or collections.

If you want to maintain your own font repository, send it to us and we will link it here as well.

#### How to help us keep fonts updated
- [ ] **Help us by automating this scripts**. At the moment we will try to keep the repository updated by running everything manually, but help automating and even using other repositories changes to trigger GitHub Actions may be more convenient.

- If you need a specific font updated immediately, you can run the script yourself for that unique font within your machine, and then submit the specific font CSS as a PR for everyone else to take advantage of it.

#### How to help by adding a new font
Before adding a new font to the repository, there are a few things to take into account:
- Make sure you are using a Mono variant. Monospaced fonts sometimes may include larger icons or Proportional variants. Although Blink can render them, you will experience issues in some contexts, so it is better to stick to the Mono variant.
- Include all the font weights if available.
- If a font comes with and witout ligatures, create a new font as the ligature variant and name it "with Ligatures".
- Beware of licenses.

To add a new font:
- If the font is already included within the Nerd Fonts aggregator, and we missed it, just add it to the corresponding patched-fonts.json or unpatched-fonts.json feeds.
- If the font is in a different GitHub repository, you can create a different feed for it and maintain it under a different repository. In that case, make sure to add the proper base_url within the main script.

## Fonts

| Font Name                                        | Font Name and Repository            | ver        | Weights  |
|:-------------------------------------------------|:------------------------------------|:-----------|:---------|
| [3270 Nerd Font][p-3270]                         | [3270][f-3270]                      | 3.0.1      | r        |
| [Agave][p-agave]                                 | [Agave][f-agave]                    | 37         | r,b      |
| [AnonymicePro Nerd Font][p-anonymous-pro]        | [Anonymous Pro][f-a-pro]            | 1.002      | r,b,i,bi |
| [Arimo][p-arimo]                                 | [Arimo][f-arimo]                    | 1.33       | r,b,i,bi |
| [Aurulent Sans Mono Nerd Font][p-aurulent]       | Stephen G. Hartke                   |            | r        |
| [BigBlueTerminal][p-bigblueterm]                 | VileR                               |            | r        |
| [Bitstrom Wera Nerd Font][p-bitstream]           | Bitstream Inc                       | 1.1        | r,b,i,bi |
| [Blex Mono][p-blex]                              | [IBM Plex Mono][f-ibm-plex]         | 2.3        | r,b,i,bi |
| [Caskaydia Cove Nerd Font][p-cascadia]           | [Cascadia Code][f-cascadia]         | 2111.01    | r,b,i,bi |
| [Code New Roman Nerd Font][p-code-nr]            | Sam Radian                          | 2.0        | r,b,i    |
| [Comic Shanns Mono Nerd Font][p-comic]           | [Comic Shanns Mono][f-comic]        | 1.3        | r,b      |
| [Cousine Nerd Font][p-cousine]                   | [Cousine][f-cousine]                | 1.211      | r,b,i,bi |
| [DaddyTimeMono][p-daddytimemono]                 | [DaddyTimeMono][f-daddytimemono]    | 1.2.3      | r        |
| [DejaVu Sans Mono Nerd Font][p-dejavu]           | [DejaVu][f-dejavu]                  | 2.37       | r,b,i,bi |
| [Droid Sans Mono Nerd Font][p-droid]             | Ascender Corp                       | 1.00-113   | r        |
| [Envy Code R Nerd Font][p-envy]                  | [Envy Code R][f-envy]               | 0.79       | r,b,i    |
| [Fantasque Sans Nerd Font][p-fantasque]          | [Fantasque Sans][f-fant]            | 1.8.0      | r,b,i,bi |
| [Fira Code Nerd Font][p-fira-code]               | [Fira Code][f-fira-code]            | 6.2        | r,b      |
| [Fira Mono Nerd Font][p-fira-mono]               | [Fira][f-fira-mono]                 | 3.206      | r,b      |
| [Go Mono Nerd Font][p-go-mono]                   | [Go-Mono][f-go-mono]                | 2.010      | r,b,i,bi |
| [Gohu Nerd Font][p-gohu]                         | [Gohu TTF][f-gohu2],[Gohu][f-gohu]  | 2.0        | r        |
| [Hack Nerd Font][p-hack]                         | [Hack][f-hack]                      | 3.003      | r,b,i,bi |
| [Hasklug Nerd Font][p-hasklig]                   | [Hasklig][f-hasklig]                | 1.2        | r,b,i,bi |
| [Heavy Data Mono Nerd Font][p-heavy-data]        | Vic Fieger                          | 1          | r        |
| [Hurmit Nerd Font][p-hermit]                     | [Hermit][f-hermit]                  | 2.0        | r,b,i,bi |
| [iM-Writing][p-im-writing]                       | [iA-Writer][f-ia-writer]            | Dec 2018   | r,b,i,bi |
| [Inconsolata Nerd Font][p-inconsolata]           | [Inconsolata][f-inconsolata]        | 3.000      | r,b,i,bi |
| [Intone Mono Nerd Font][p-intel-one-mono]        | [Intel One Mono][f-intel-one-mono]  | 1.2.1      | r,b,i,bi |
| [Iosevka Nerd Font][p-iosevka]                   | [Iosevka][f-iosevka]                | 22.1.0     | r,b,i    |
| [Iosevka Term Nerd Font][p-iosevka-term]         | [Iosevka Term][f-iosevka]           | 22.1.0     | r,b,i,bi |
| [JetBrains Mono][p-jetbrains-mono]               | [JetBrains Mono][f-jetbrains-mono]  | 2.304      | r,b,i,bi |
| [Lekton Nerd Font][p-lekton]                     | [Lekton][f-lekton]                  | 34         | r,b,i    |
| [Literation Mono Nerd Font][p-liberation]        | [Liberation][f-liberation]          | 2.1.5      | r,b,i,bi |
| [Lilex Nerd Font][p-lilex]                       | [Lilex][f-lilex]                    | 2.000      | r,b      |
| [Meslo Nerd Font][p-meslo]                       | [Meslo][f-meslo]                    | 1.21       | r,b,i,bi |
| [Monofur Nerd Font][p-monofur]                   | Tobias B Koehler                    | 1.0        | r,b,i    |
| [Monoid Nerd Font][p-monoid]                     | [Monoid][f-monoid]                  | 0.61       | r,b,i    |
| [Mononoki Nerd Font][p-mononoki]                 | [Mononoki][f-mononoki]              | 1.6        | r,b,i,bi |
| [M+ (MPlus) Nerd Font][p-mplus]                  | [M+ Fonts][f-mplus]                 | 2023/03    | r,b      |
| [Noto][p-noto]                                   | [Noto][f-noto]                      | div        | r,b      |
| [OpenDyslexic][p-opendyslexic]                   | [OpenDyslexic][f-opendyslexic]      | 2.001      | r,b,i,bi |
| [Overpass][p-overpass]                           | [Overpass][f-overpass]              | 3.0.5      | r,b      |
| [ProFont (x11) Nerd Font][p-profont]             | [ProFont][f-profont]                | 2.2        | r        |
| [ProggyClean Nerd Font][p-proggy-clean]          | Tristan Grimmer                     | 2004/04/15 | r        |
| [Roboto Mono][p-roboto]                          | [Roboto Mono][f-roboto]             | 3.0        | r,b,i,bi |
| [Sauce Code Nerd Font][p-source-code-pro]        | [Source][f-source]                  | 2.038      | r,b,i,bi |
| [Shure Tech Mono Nerd Font][p-share-tech-mono]   | [Share Tech Mono][f-share]          | 1.003      | r        |
| [Space Mono Nerd Font][p-space-mono]             | [Space Mono][f-space]               | 1.001      | r,b,i,bi |
| [Terminess Nerd Font][p-terminus]                | [Terminus TTF][f-terminus]          | 4.49.2     | r,b,i,bi |
| [Tinos][p-tinos]                                 | [Tinos][f-tinos]                    | 1.23       | r,b,i,bi |
| [Ubuntu Mono Nerd Font][p-ubuntu-mono]           | [Ubuntu Font][f-ubuntu]             | 0.80       | r,b,i,bi |
| [Victor Mono][p-victor]                          | [Victor Mono][f-victor]             | 1.5.4      | r,b,i,bi |

## Licensing

This repository is a re-purpose of the [Nerd-Fonts fonts repository](https://github.com/ryanoasis/nerd-fonts). The license is hence inherited from it, including the MIT license for our scripts. See [LICENSE](https://github.com/ryanoasis/nerd-fonts/blob/-/LICENSE).

<!--
Font repos
-->

[f-3270]:https://github.com/rbanffy/3270font
[f-agave]:https://github.com/agarick/agave
[f-a-pro]:https://www.marksimonson.com/fonts/view/anonymous-pro
[f-arimo]:https://github.com/googlefonts/Arimo
[f-cascadia]:https://github.com/microsoft/cascadia-code
[f-cousine]:https://fonts.google.com/specimen/Cousine
[f-comic]:https://github.com/jesusmgg/comic-shanns-mono
[f-daddytimemono]:https://github.com/BourgeoisBear/DaddyTimeMono
[f-dejavu]:https://github.com/dejavu-fonts/dejavu-fonts
[f-envy]:https://github.com/damieng/envy-code-r
[f-fant]:https://github.com/belluzj/fantasque-sans
[f-fira-code]:https://github.com/tonsky/FiraCode
[f-fira-mono]:https://github.com/mozilla/Fira
[f-gohu2]:https://github.com/koemaeda/gohufont-ttf
[f-gohu]:http://font.gohu.org/
[f-go-mono]:https://go.googlesource.com/image/+/master/font/gofont/ttfs/
[f-hack]:https://github.com/chrissimpkins/Hack
[f-hasklig]:https://github.com/i-tu/Hasklig
[f-hermit]:https://pcaro.es/hermit
[f-ia-writer]:https://github.com/iaolo/iA-Fonts
[f-ibm-plex]:https://github.com/IBM/plex
[f-inconsolata]:https://github.com/googlefonts/Inconsolata
[f-inconsolatago]:https://levien.com/type/myfonts/inconsolata.html
[f-inconsolatalgc]:https://github.com/MihailJP/Inconsolata-LGC
[f-intel-one-mono]:https://github.com/intel/intel-one-mono
[f-iosevka]:https://github.com/be5invis/Iosevka
[f-jetbrains-mono]:https://github.com/JetBrains/JetBrainsMono
[f-lekton]:https://fonts.google.com/specimen/Lekton
[f-liberation]:https://github.com/liberationfonts/liberation-fonts
[f-lilex]:https://github.com/mishamyrt/Lilex
[f-meslo]:https://github.com/andreberg/Meslo-Font
[f-monoid]:https://github.com/larsenwork/monoid
[f-mononoki]:https://madmalik.github.io/mononoki
[f-mplus]:https://mplusfonts.github.io
[f-noto]:https://fonts.google.com/noto
[f-opendyslexic]:https://github.com/antijingoist/open-dyslexic
[f-overpass]:http://overpassfont.org
[f-profont]:https://tobiasjung.name/profont
[f-roboto]:https://fonts.google.com/specimen/Roboto+Mono
[f-share]:https://fonts.google.com/specimen/Share+Tech+Mono
[f-source]:https://github.com/adobe-fonts/source-code-pro
[f-space]:https://fonts.google.com/specimen/Space+Mono
[f-terminus]:http://terminus-font.sourceforge.net
[f-tinos]:https://fonts.google.com/specimen/Tinos
[f-ubuntu]:http://font.ubuntu.com
[f-victor]:https://github.com/rubjo/victor-mono
