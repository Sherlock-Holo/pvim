#!/bin/bash

Input=$1
Type=$2

if [ $# != 2 ]; then
        echo "You need to tell me the file's type(codes or pics)"
        exit 1
fi

if [ $Type == "codes" ]; then
        cat $Input | curl -F 'vimcn=<-' https://cfp.vim-cn.com/ | tee /dev/stderr | head -c -1 |xclip -sel c -i
fi

if [ $Type == "pics" ]; then
        curl -F 'name=@'${Input}'' https://img.vim-cn.com/ | tee /dev/stderr | head -c -1 |xclip -sel c -i
fi
# tee /dev/stderr 是为了输出到屏幕
# head -c -1 是为了去除粘贴时那奇怪的换行
# xclip -sel c -i 复制到剪贴板
