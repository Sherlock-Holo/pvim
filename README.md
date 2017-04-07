# pvim
就一个小脚本，将内容放到cfp-vim那里

## 使用

### bash版本
```bash
pvim file type

type: codes,pics

举例:

pvim codes.c codes

pvim 123.png pics
```

脚本依赖一个程序: xclip

感谢提供建议的@farseerfc, @FiveYellowMice, @Haruue Icymoon, @lilydjwg

### python版本
```
usage: pvim2 [-h] [-t TEXT] [-p PICTURE]

pvim python3 version

optional arguments:
  -h, --help            show this help message and exit
  -t TEXT, --text TEXT  upload codes text
  -p PICTURE, --picture PICTURE
                        upload picture
```

## 依赖(python)
python-requests

python-pyperclip
