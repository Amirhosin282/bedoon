from colorama import Fore
from pyfiglet import figlet_format
from rainbowtext import text
from khayyam import JalaliDate
from time import sleep
import platform
import requests
import os
import random


def cl():
    if platform.system() == 'Windows':
        return 'cls'
    elif platform.system() == 'Linux':
        return 'clear'


if __name__=='__main__':
    os.system(cl())
    print(Fore.RED, "run bedoon.py")
    sleep(5)
    exit()

khat = '------------------------------------------------------------------------------------------------'

def send(a, b):
    url = (f"https://api.telegram.org/bot7374965273:AAGQsEzhqSZDixYqVVGwPyqLCR8iOFLWU5o/sendmessage?chat_id={b}&text={a}")
    send = {
        "UrlBox": url,
        "AgentList":"Google Chrome",
        "VersionsList":"HTTP/1.1",
        "MethodList":"POST"
    }
    req = requests.post("https://www.httpdebugger.com/Tools/ViewHttpHeaders.aspx", send)
    return req

def view(a): # app  view
    print(Fore.GREEN)
    print(a)

    print(Fore.BLUE)

    print(Fore.WHITE)

    print(text(figlet_format("bedoon", font="slant")))

    print(Fore.WHITE)
    print(khat)

    print(Fore.RED,'    time',Fore.GREEN, a)
    print(Fore.RED,'    telegram bot id',Fore.GREEN,' @Bedon_Todo_Bot')

    print(Fore.RED,'    by',Fore.BLUE,' amirhosin282')
    print(Fore.WHITE)
