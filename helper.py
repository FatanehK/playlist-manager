import os
from termcolor import cprint


def gPrint(text):
    cprint(text, "green")


def bPrint(text, bold=False):
    cprint(text, "blue", attrs=["bold"] if bold else [])


def yPrint(text, bold=False):
    cprint(text, "yellow", attrs=["bold"] if bold else [])


def rPrint(text, bold=False):
    cprint(text, "red", attrs=["bold"] if bold else [])


def clear():
    os.system("clear")
