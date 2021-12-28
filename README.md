# outputformater
Python library to decorate and beautify your standard output 💖

![ouf_image_example](https://felipedelestro.files.wordpress.com/2021/12/ouf_notebook_example.png)

## Installation
To get the latest version, simply use pip:

``` Python
pip install outputformater
```

## Basic usage

It is recommended to use `ouf` as shortcut for `outputformater`:

``` Python
import outputformater as ouf
```

Main functions are:
* `ouf.boxtitle`
* `ouf.linetitle`
* `ouf.bigtitle`
* `ouf.showlist`
* `ouf.bar`
* `ouf.barlist`

By default, functions `print` the result. You have the alternative to return a `string` instead, by passing the argument `return_str=True`  (nothing will be printed in this case).

## Titles
To decorate titles with a box around it, use `ouf.boxtitle`:
```Python
ouf.boxtitle("Long title in a box")
```
```
╭─────────────────────╮
│ Long title in a box │
╰─────────────────────╯
```

Boxes can have different styles:
``` Python
ouf.boxtitle("Box with 'line' style", style="line")
ouf.boxtitle("Box with 'double' style", style="double")
ouf.boxtitle("Box with 'dashes' style", style="dashes")
```
```
╭───────────────────────╮
│ Box with 'line' style │
╰───────────────────────╯
╔═════════════════════════╗
║ Box with 'double' style ║
╚═════════════════════════╝
╭╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╮
┊ Box with 'dashes' style ┊
╰╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╯
```

Or you can pass any character and it will be used for the decoration:
``` Python
ouf.boxtitle("Box with custom character as style", style="ø")
```
```
øøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøø
ø Box with custom character as style ø
øøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøø
```

With all the same options as for `boxtitle`, you can use `linetitle` for a simple line underneath your text:
```
ouf.linetitle("Long title with 'double' underline", style="double")
```
```
Long title with 'double' underline
══════════════════════════════════
```

### Big title
It is possible to use ASCII art to generate big titles:
``` Python
outputstring = ouf.bigtitle("Here's a big title!")
```
```
█ █ █▀▀ █▀█ █▀▀ ▀ █▀   ▄▀█   █▄▄ █ █▀▀   ▀█▀ █ ▀█▀ █   █▀▀ █ 
█▀█ ██▄ █▀▄ ██▄   ▄█   █▀█   █▄█ █ █▄█    █  █  █  █▄▄ ██▄ ▄
```

Currently, only one font is available, and the supported characters are: `"0123456789abcdefghijklmnopqrstuvwxyz_-!.' "`

(You can get them by using `ouf.fonts.suported_chars`)


