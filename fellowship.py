#!/usr/bin/env python3

import os
import sys
import subprocess
import time
import datetime
import enum

class Colors:
    Red = '\x1b[38;5;124m'
    Green = '\x1b[38;5;119m'
    Blue = '\x1b[38;5;122m'
    White = '\x1b[38;5;231m'
    Reset = '\x1b[0m'

try:

    freq = input('How ' + Colors.Blue + 'often' + Colors.Reset + ' should your connection be checked? (seconds)\n')
    remote = input('What ' + Colors.Blue + 'target' + Colors.Reset + ' should be checked for availability?\n')


    command = ["ping", "-c", "1", "-w", freq, remote]

    print("Checking " + Colors.Blue + remote + Colors.Reset + " every " + Colors.Blue + freq + Colors.Reset + " seconds...")

    with open("availability.txt", 'a', encoding = 'utf-8') as log:
        while True:
            result = subprocess.call(command, stdout = subprocess.DEVNULL)

            while(result == 0):
                result = subprocess.call(command, stdout = subprocess.DEVNULL)

                print(Colors.Green + "Internet came online at: " + Colors.White + str(datetime.datetime.now()) +   #ping worked
                Colors.Blue + "\nWriting to file...")
                log.write("Internet came online at: " + str(datetime.datetime.now()) + "\n") #logging the date and time that the internet came online

                while(result == 0):
                    result = subprocess.call(command, stdout = subprocess.DEVNULL)

                    print(Colors.Green + "Internet is still up")
                    time.sleep(int(freq))

            else:
                result = subprocess.call(command, stdout = subprocess.DEVNULL)

                print(Colors.Red + "Internet went down at: " + Colors.White + str(datetime.datetime.now()) +  #ping did not work
                Colors.Blue + "\nWriting to file...")
                log.write("Internet went offline at: " + str(datetime.datetime.now()) + "\n")

                while(result !=0):
                    result = subprocess.call(command, stdout = subprocess.DEVNULL)
                    print(Colors.Red + "Internet is still down")


except KeyboardInterrupt:
    print(Colors.White + "\rShutting down...")
