#! /usr/bin/env python3

import requests
import os
import argparse

def upload(file):
    with open(file, 'rb') as f:
        ufile = requests.post("http://cfp.vim-cn.com", files = {'vimcn': f})
        return ufile.text

# opt
parser = argparse.ArgumentParser(description = 'pvim python3 version')
parser.add_argument('-c', '--codes', help = 'upload codes text')
parser.add_argument('-p', '--picture', help = 'upload picture')

args = parser.parse_args()

if args.codes:
    print(upload(args.codes))
