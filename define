#!/usr/bin/env python3

import requests, json, sys
from termcolor import colored, cprint


def fetch(keyword):
    if isinstance(keyword, str):
        try:
            url = "https://api.dictionaryapi.dev/api/v2/entries/en/"
            response = requests.get(url+keyword)
            if response.status_code == 200:
                data = response.json()
                return resPos(keyword, data)
            else:
                raise Exception("Request failed!")
        except:
            return "Something wrong happened!!!"
    else:
        return "input must be a string."



def resPos(keyword, data):
        speech = data[0]['meanings'][0]['partOfSpeech']
        defination_one = data[0]['meanings'][0]['definitions'][0]['definition']

        if (len(data[0]['meanings'][0]['definitions'])>1):
            if (len(data[0]['meanings'][0]['definitions'])>2):
                defination_two = data[0]['meanings'][0]['definitions'][1]['definition']
                defination_three = data[0]['meanings'][0]['definitions'][2]['definition']
                return (f"{keyword}:({speech})\n[1]{defination_one}\n[2]{defination_two}\n[3]{defination_three}")
            else:
                defination_two = data[0]['meanings'][0]['definitions'][1]['definition']
                return (f"{keyword}:({speech})\n[1]{defination_one}\n[2]{defination_two}")
        else:
            return (f"{keyword}:({speech})\n[1]{defination_one}")


cmd_args = sys.argv

if len(cmd_args) > 1:
    cprint(fetch(cmd_args[1]), 'yellow')
else:
    cprint("please provide a word!!", 'red')

