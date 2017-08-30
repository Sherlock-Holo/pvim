#!/usr/bin/env python3

import argparse
from configparser import ConfigParser
import requests
import sys
from time import time

try:
    import pyperclip
except ImportError:
    pass

config = '/etc/pvim2/pvim2.conf'
cfg = ConfigParser()
cfg.read(config)
server = cfg.get('Setting', 'server')
img_server = cfg.get(server, 'img_server')
text_server = cfg.get(server, 'text_server')
parameter = cfg.get(server, 'arg')


def upload_img(file, arg):
    with open(file, 'rb') as f:
        start_time = time()
        ufile = requests.post(
            img_server,
            files={arg: f.read(),
                   'content_type': 'application/octet-stream'})
        end_time = time()
        url = ufile.text.split()[-1]
        usage_time = round(end_time - start_time, 2)
        print('upload time: {}s'.format(usage_time))

        try:
            pyperclip.copy(url)
        except NameError:
            pass
        except:
            pass

        return url


def upload_text(file, arg):
    postfix = file.split('.')[-1]
    with open(file, 'r') as f:
        start_time = time()
        ufile = requests.post(
            text_server,
            data={arg: f.read(),
                  'content_type': 'application/octet-stream'})
        end_time = time()
        url = ufile.text
        url = url.strip()
        url = url + "/{}".format(postfix)
        usage_time = round(end_time - start_time, 2)
        print('upload time: {}s'.format(usage_time))

        try:
            pyperclip.copy(url)
        except NameError:
            pass
        except:
            pass

        return url


def upload_pipe_test(arg):
    args = sys.stdin
    start_time = time()
    ufile = requests.post(
        text_server,
        data={arg: args.read(),
              'content_type': 'application/octet-stream'})
    end_time = time()
    url = ufile.text
    url = url.strip()
    usage_time = round(end_time - start_time, 2)
    print('upload time: {}s'.format(usage_time))

    try:
        pyperclip.copy(url)
    except NameError:
        pass

    return url


# opt
parser = argparse.ArgumentParser(description='pvim python3 version')
parser.add_argument('-t', '--text', help='upload codes text')
parser.add_argument('-p', '--picture', help='upload picture')
#parser.add_argument('--pipe',action='store_true' , help='upload from pipe')

args = parser.parse_args()

if args.picture:
    print(upload_img(args.picture, parameter))

elif args.text:
    print(upload_text(args.text, parameter))

else:
    print(upload_pipe_test(parameter))
