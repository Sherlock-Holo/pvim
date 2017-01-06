#!/bin/bash

cat $1 | curl -F 'vimcn=<-' http://cfp.vim-cn.com/ | tee /dev/stderr | head -c -1 |xclip -sel c -i

# tee /dev/stderr 是为了输出到屏幕
# head -c -1 是为了去除粘贴时那奇怪的换行
# xclip -sel c -i 复制到剪贴板
