##---- License:MIT
##---- Welcome Vector
##-- Make By Rain

import requests
import socket
import sys
import os
import time
from pystyle import Colors, Colorate
from colorama import Fore

pick = {Fore.BLUE}

##-- Test logo
print(Colorate.Horizontal(Colors.red_to_purple, '''
 /$$    /$$                      /$$                        
| $$   | $$                     | $$                        
| $$   | $$ /$$$$$$   /$$$$$$$ /$$$$$$    /$$$$$$   /$$$$$$ 
|  $$ / $$//$$__  $$ /$$_____/|_  $$_/   /$$__  $$ /$$__  $$
 \  $$ $$/| $$$$$$$$| $$        | $$    | $$  \ $$| $$  \__/
  \  $$$/ | $$_____/| $$        | $$ /$$| $$  | $$| $$      
   \  $/  |  $$$$$$$|  $$$$$$$  |  $$$$/|  $$$$$$/| $$      
    \_/    \_______/ \_______/   \___/   \______/ |__/ ''', 1))
print (f"{pick}test")


def help1():
    global onstart1
    print(f"""
{Fore.BLUE}         ⢀⣀⣀⣀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀
{Fore.BLUE}⠀⠀⠀⠀⠀⠀⢀⣀⡿⠿⠿⠿⠿⠿⠿⢿⣀⣀⣀⣀⣀⡀⠀⠀
{Fore.BLUE}⠀⠀⠀⠀⠀⠀⠸⠿⣇⣀⣀⣀⣀⣀⣀⣸⠿⢿⣿⣿⣿⡇⠀⠀   {Fore.RESET}Welcome Vector 
{Fore.BLUE}⠀⠀⠀⠀⠀⠀⠀⠀⠻⠿⠿⠿⠿⠿⣿⣿⣀⡸⠿⢿⣿⡇⠀⠀    {Fore.RED}== Warning ==
{Fore.BLUE}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣤⣿⣿⣿⣧⣤⡼⠿⢧⣤⡀    {Fore.RESET}Please be sure to read it!
{Fore.BLUE}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣤⣿⣿⣿⣿⠛⢻⣿⡇⠀⢸⣿⡇    {Fore.RESET}This tool is for educational purposes
{Fore.BLUE}⠀⠀⠀⠀⠀⠀ ⠀⣤⣤⣿⣿⣿⣿⠛⠛⠀⢸⣿⡇⠀⢸⣿⡇
{Fore.BLUE}⠀⠀⠀⠀⠀⠀⢠⣤⣿⣿⣿⣿⠛⠛⠀⠀⠀⢸⣿⡇⠀⢸⣿⡇
{Fore.BLUE}⠀⠀⠀⠀⢰⣶⣾⣿⣿⣿⠛⠛⠀⠀⠀⠀⠀⠈⠛⢳⣶⡞⠛⠁
{Fore.BLUE}⠀⠀⢰⣶⣾⣿⣿⣿⡏⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠁⠀⠀
{Fore.BLUE}⢰⣶⡎⠉⢹⣿⡏⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
{Fore.BLUE}⢸⣿⣷⣶⡎⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
{Fore.BLUE}⠀⠉⠉⠉⠁⠀⠀⠀""")
    agree = input("do you agree Y/N:")

    if agree == "y":
        os.system('cls')
        help2()

    if agree == "n":
        print ("Goodbye.. Uninstall Here")
        os.system('pause')

    if agree == "Y":
        os.system('cls')
        help2()

    if agree == "N":
        print ("Goodbye.. Uninstall Here")
        os.system('pause')


def help2():
    global onstart2
    print ("test")


def onstart1():
    os.system("cls && title Vector - Welcome")
    help1() 
 
onstart1()

def onstart2():
    help2() 
 
onstart1()

def main1():
    os.system("cls && title Vector - Home")
 
main1()
