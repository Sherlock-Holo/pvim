#!/bin/bash

cat $1 | curl -F 'vimcn=<-' http://cfp.vim-cn.com/

# echo "已复制cfp-vim的URL到剪贴板"  已废弃
