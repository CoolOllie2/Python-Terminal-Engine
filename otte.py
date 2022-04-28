from colorama import init, Fore
from art import tprint
from time import sleep
import sys
import os

init()
lines = []

def osleep(seconds):
    sleep(seconds)

def oclear(seconds_till_clear):
    sleep(seconds_till_clear)
    os.system("clear")

class colour:
    BLACK = Fore.BLACK
    RED = Fore.RED
    GREEN = Fore.GREEN
    YELLOW = Fore.YELLOW
    BLUE = Fore.BLUE
    MAGENTA = Fore.MAGENTA
    CYAN = Fore.CYAN
    WHITE = Fore.WHITE
    RESET = Fore.RESET

def ocolour(colour):
    print(colour, end = '')

def oart(text):
    tprint(text)
    sys.stdout.flush()
    osleep(0.05)

def otext(text):
    for char in text:
        print(char, end = '')
        sys.stdout.flush()
        osleep(0.05)

def oinput(text):
    for char in text:
        print(char, end='')
        sys.stdout.flush()
        osleep(0.05)
    value = input()  
    return value