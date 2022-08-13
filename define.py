#!/usr/bin/env python

import requests, json, sys

argus = sys.argv

def fetch(keyword):
    if isinstance(keyword, str):
        try:
            url = "https://api.dictionaryapi.dev/api/v2/entries/en/"
            response = requests.get(url+keyword)
            if response.status_code == 200:
                data = response.json()

                speech = data[0]['meanings'][0]['partOfSpeech']
                definations = data[0]['meanings'][0]['definitions'][0]['definition']

                return definations
            else:
                raise Exception("Request failed!")
        except:
            return "Something wrong happened!!!"
    else:
        return "input must be a string."



# listy = 
# print(len(argus))
if len(argus) > 1:
    print(fetch(argus[1]))
else:
    print("please provide a word!!")

