from colorama import Fore
from khayyam import JalaliDate
from time import sleep
import platform
import requests
import os

def cl():
    if platform.system() == 'Windows':
        return 'cls'
    elif platform.system() == 'Linux':
        return 'clear'


if __name__=='__main__':
    os.system(cl())
    print(Fore.RED, "run main.py")
    sleep(5)
    exit()

time = JalaliDate.today()

khat = '------------------------------------------------------------------------------------------------'

def send(a, b):
    url = (f"https://api.telegram.org/bot7374965273:AAGQsEzhqSZDixYqVVGwPyqLCR8iOFLWU5o/sendmessage?chat_id={b}&text={a}")
    send = {
        "UrlBox": url,
        "AgentList":"Google Chrome",
        "VersionsList":"HTTP/1.1",
        "MethodList":"POST"
    }
    requests.post("https://www.httpdebugger.com/Tools/ViewHttpHeaders.aspx", send)