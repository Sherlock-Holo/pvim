#! /usr/bin/env python3

import requests
import argparse
import pyperclip

def upload_img(file):
    with open(file, 'rb') as f:
        ufile = requests.post("https://img.vim-cn.com", files = {'vimcn': f})
        url = ufile.text
        url = url.split()[0]
        pyperclip.copy(url)
        return url

def upload_text(file):
    with open(file, 'r') as f:
        ufile = requests.post("https://cfp.vim-cn.com", data = {'vimcn': f.read()})
        url = ufile.text
        url = url.split()[0]
        pyperclip.copy(url)
        return url

# opt
parser = argparse.ArgumentParser(description = 'pvim python3 version')
parser.add_argument('-t', '--text', help = 'upload codes text')
parser.add_argument('-p', '--picture', help = 'upload picture')

args = parser.parse_args()

if args.picture:
    print(upload_img(args.picture))

elif args.text:
    print(upload_text(args.text))
