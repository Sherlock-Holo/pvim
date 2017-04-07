#! /usr/bin/env python3

import requests
import argparse
import pyperclip
from configparser import ConfigParser

config = '/etc/pvim2/pvim2.conf'
cfg = ConfigParser()
cfg.read(config)
server = cfg.get('Setting', 'server')
img_server = cfg.get(server, 'img_server')
text_server = cfg.get(server, 'text_server')
parameter = cfg.get(server, 'arg')

def upload_img(file, arg):
    with open(file, 'rb') as f:
        ufile = requests.post(img_server, files = {arg: f.read(), 'content_type': 'application/octet-stream'})
        url = ufile.text.split()[-1]
        #url = url.strip()
        pyperclip.copy(url)
        return url

def upload_text(file, arg):
    postfix = file.split('.')[-1]
    with open(file, 'r') as f:
        ufile = requests.post(text_server, data = {arg: f.read(),  'content_type': 'application/octet-stream'})
        url = ufile.text
        url = url.strip()
        url = url + "/{}".format(postfix)
        pyperclip.copy(url)
        return url

# opt
parser = argparse.ArgumentParser(description = 'pvim python3 version')
parser.add_argument('-t', '--text', help = 'upload codes text')
parser.add_argument('-p', '--picture', help = 'upload picture')

args = parser.parse_args()

if args.picture:
    print(upload_img(args.picture, parameter))

elif args.text:
    print(upload_text(args.text, parameter))
