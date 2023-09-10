#!/usr/bin/env python3

import requests,time, json, sys, threading, itertools, os, curses
from termcolor import cprint,colored

cmd_args = sys.argv

def fetch():
    if (len(sys.argv)> 1):
        if isinstance(cmd_args[1], str):
            try:
                url = "https://api.dictionaryapi.dev/api/v2/entries/en/"
                response = requests.get(url+cmd_args[1])
                if response.status_code == 200:
                    data = response.json()
                    return resPos(cmd_args[1], data)
                else:
                    raise Exception("Request failed!")
            except:
                cprint("\bSomething went wrong, could not fetch meaning!!!", 'red')
        else:
            cprint("\bInput must be a string.", 'red')
    else:
        cprint("\bPlease provide a word", "red")


def resPos(keyword, data):

        sys.stdout.write("\033[A\b")                

        my_keyw = colored(" "+keyword+ " ","black", "on_white", attrs=["bold"])
        speech = data[0]['meanings'][0]['partOfSpeech']

        defination_one = data[0]['meanings'][0]['definitions'][0]['definition']

        if (len(data[0]['meanings'][0]['definitions'])>1):
            if (len(data[0]['meanings'][0]['definitions'])>2):
                defination_two = data[0]['meanings'][0]['definitions'][1]['definition']
                defination_three = data[0]['meanings'][0]['definitions'][2]['definition']

                cprint((f"\n{my_keyw} ({speech})\n[1] {defination_one}\n[2] {defination_two}\n[3] {defination_three}\n"),'yellow')
            else:
                defination_two = data[0]['meanings'][0]['definitions'][1]['definition']
                cprint((f"\n{my_keyw} ({speech})\n[1] {defination_one}\n[2] {defination_two}\n"), 'yellow')
        else:
            cprint((f"\n{my_keyw} ({speech})\n[1] {defination_one}\n"), 'yellow')


mainThread = threading.Thread(target=fetch)

mainThread.start()

spinner = itertools.cycle(['-', '/', '|', '\\'])

while mainThread.is_alive():
    sys.stdout.write(next(spinner))   # write the next character
    sys.stdout.flush()                
    sys.stdout.write('\b')            # erase the last written char

