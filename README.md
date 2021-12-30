# outputformat
Python library to decorate and beautify your standard output 💖

![ouf_image_example](https://felipedelestro.files.wordpress.com/2021/12/ouf_intro.png)

## Installation
To get the latest version, simply use pip:

``` Python
pip install outputformat
```
There are **no dependencies**. 

`Python>=3.6` is needed, as it uses f strings.

## Basic usage

It is recommended to use `ouf` as shortcut for `outputformat`:

``` Python
import outputformat as ouf
```

Main functions are:
* `ouf.boxtitle`
* `ouf.linetitle`
* `ouf.bigtitle`
* `ouf.showlist`
* `ouf.bar`
* `ouf.barlist`

By default, functions `print` the result. You have the alternative to return a `string` instead, by passing the argument `return_str=True`  (nothing will be printed in this case).

## Showing titles
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

## Showing lists

You can simply show a list using bullet points:
``` Python
data = ["Item A", "Item B", "Item C", "Item D"]
ouf.showlist(data)
```
```
• Item A
• Item B
• Item C
• Item D
```

And also there's an option to add a title to your list:
``` Python
data = ["Item A", "Item B", "Item C", "Item D"]
ouf.showlist(data, title="List of items")
```
```
List of items
• Item A
• Item B
• Item C
• Item D
```

Different styles are available, as `bullet`, `line`, `box` and `ordinal`
``` Python
data = ["Item A", "Item B", "Item C", "Item D"]

ouf.showlist(data, style="line", title="Style line")
ouf.showlist(data, style="box", title="Style box")
ouf.showlist(data, style="ordinal", title="Style ordinal")
```
```
 Style line
╭──────────
├ Item A
├ Item B
├ Item C
╰ Item D

╭───────────╮
│ Style box │
├───────────╯
├ Item A
├ Item B
├ Item C
╰ Item D

Style ordinal
1. Item A
2. Item B
3. Item C
4. Item D
```

Or pass any string to be used as marker
``` Python
data = ["Item A", "Item B", "Item C", "Item D"]
ouf.showlist(data, style="~>", title="Custom style list")
```
```
Custom style list
~> Item A
~> Item B
~> Item C
~> Item D
```

## Showing bars

You can create a simple horizontal bar using `ouf.bar`
The first parameter (`value`) is the filled amount, the second (`maxvalue`) is the maximum amount

``` Python
ouf.bar(35, 50)
```
```
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░ 35/50 ( 70.00%)

```
Note that there's some **integer rounding** needed to create the bar, so the size is not precise, more like a ballpark visualisation.

The size of the bar (in characters) is defined by `length`
``` Python
ouf.bar(35, 50, length=10)
ouf.bar(35, 50, length=50)
```
```
▓▓▓▓▓▓▓░░░ 35/50 ( 70.00%)
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░░ 35/50 ( 70.00%)
```

Different styles are available, as well as the option to have a title before the bar:
``` Python
ouf.bar(35, 50, style="block", length=15, title="Block style", title_pad=15)
ouf.bar(35, 50, style="battery", length=15,title="Battery style", title_pad=15)
ouf.bar(35, 50, style="bar", length=15, title="Bar style", title_pad=15)
ouf.bar(35, 50, style="circle", length=15, title="Circle style", title_pad=15)
```
```
Block style....: ▓▓▓▓▓▓▓▓▓▓░░░░░ 35/50 ( 70.00%)

Battery style..: ┫██████████     ┣ 35/50 ( 70.00%)

Bar style......: [■■■■■■■■■■     ] 35/50 ( 70.00%)

Circle style...: ●●●●●●●●●●○○○○○ 35/50 ( 70.00%)
```

There's also a star emoji style, that works better with small values for `length` and using `show_percentage=False` and `show_values=False`

``` Python
ouf.bar(60, 100, style="star", length=5, title="Item A", show_percentage=False, show_values=False)
ouf.bar(20, 100, style="star", length=5, title="Item B", show_percentage=False, show_values=False)
ouf.bar(90, 100, style="star", length=5, title="Item C", show_percentage=False, show_values=False)
```
```
Item A: ⭐⭐⭐
Item B: ⭐
Item C: ⭐⭐⭐⭐
```
### Custom bars

A totally custom style for the bar can be created, passing a list of characters as `style`
``` Python
ouf.bar(35, 50, style=["(", "X", "-", ")"], title="Custom style")
```
```
Custom style: (XXXXXXXXXXXXXXXXXXXXXX----------) 35/50 ( 70.00%)

```


Or you can pass just a simple character, and it will be used for a basic bar:
``` Python
ouf.bar(35, 50, style="$", title="Custom style")
```
```
Custom style: [$$$$$$$$$$$$$$$$$$$$$$          ] 35/50 ( 70.00%)
```


### Multiple bars from list
It is possible to use `ouf.barlist` and pass directly a list of `values` with the correspondent list of `titles`

``` Python
values = [6, 3, 13, 8]
titles = ["var", "long var name", "medium var", "one more"]
ouf.barlist(values, titles, maxvalue=15, style="bar")
```
```
var..........: [■■■■■■■■■■■■                    ]  6/15 ( 40.00%)
long var name: [■■■■■■                          ]  3/15 ( 20.00%)
medium var...: [■■■■■■■■■■■■■■■■■■■■■■■■■■■     ] 13/15 ( 86.67%)
one more.....: [■■■■■■■■■■■■■■■■■               ]  8/15 ( 53.33%)
```
The same parameters from `ouf.bar` can be used. Only one `maxvalue` is used for all the lists

## Show emoji
Some shortcuts for the unicode values of common emoji are available
``` Python
print(ouf.emoji.heart, ouf.emoji.thumbs_up)
```
```
💖 👍
```

Current shortcuts are the following:
```
crazy.............:🤪
sad...............:😥
circle_red........:🔴
circle_orange.....:🟠
circle_yellow.....:🟡
circle_green......:🟢
circle_white......:⚪
circle_black......:⚫
star..............:⭐
heart.............:💖
thumbs_up.........:👍
check.............:✅
clap..............:👏
bomb..............:💣
```
