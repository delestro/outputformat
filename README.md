# outputformater
Python library to decorate and beautify strings

## Basic usage
``` Python
import outputformater as ouf

ouf.bigtitle("Welcome to ouf!")

ouf.showlist(["Organize", "Explain", "Report"], style="line", title="Things you can do with ouf")

values = [6, 3, 13, 8]
titles = ["var", "long var name", "medium var", "variable"]
ouf.barlist(values, titles, maxvalue=15, length=15, style="bar")
```

Output:
``` Text
█ █ █ █▀▀ █   █▀▀ █▀█ █▀▄▀█ █▀▀   ▀█▀ █▀█   █▀█ █ █ █▀▀ █ 
▀▄▀▄▀ ██▄ █▄▄ █▄▄ █▄█ █ ▀ █ ██▄    █  █▄█   █▄█ █▄█ █▀  ▄ 

 Things you can do with ouf
╭──────────────────────────
├ Organize
├ Explain
╰ Report

var..........: [■■■■■■         ]  6/15 ( 40.00%)
long var name: [■■■            ]  3/15 ( 20.00%)
medium var...: [■■■■■■■■■■■■■  ] 13/15 ( 86.67%)
variable.....: [■■■■■■■■       ]  8/15 ( 53.33%)
```
