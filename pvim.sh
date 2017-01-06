#!/bin/bash

cat $1 | curl -F 'vimcn=<-' http://cfp.vim-cn.com/ | xclip -selection clipboard

echo "已复制到剪贴板"
