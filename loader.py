import wget
import requests
import os
import sys
import time
import json
import ctypes
import colorama
import datetime

#===========================================[CONFIG]==================================================#

def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.05)

def get_hwid():
    return os.popen('wmic csproduct get uuid').read().split('\n')[1].strip()

def get_ip():
    return requests.get('https://api.ipify.org').text

def get_os():
    return os.name

def get_pc_name():
    return os.popen('hostname').read().strip()

def get_pc_username():
    return os.popen('whoami').read().strip()

#====================================================================================================#

print_slow('Loading...\n')
try:
    requests.get('https://google.com')
except:
    print(colorama.Fore.RED + 'No internet connection!')
    time.sleep(5)
    sys.exit()

