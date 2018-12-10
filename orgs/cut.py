#!/bin/env/python3

from bs4 import BeautifulSoup
import sys
import os


def UsageExit():
    print('python3 cut.py [.html file]')
    sys.exit()


if len(sys.argv) != 2:
    UsageExit()

if os.path.isfile(sys.argv[1]) == False:
    UsageExit()

soup = BeautifulSoup(open(sys.argv[1]), "lxml")

k = soup.find('div', id='content')

savedStdout = sys.stdout
f = open("tmp.html", "w")
sys.stdout = f
print(k)
f.close

sys.stdout = savedStdout
print("done")
