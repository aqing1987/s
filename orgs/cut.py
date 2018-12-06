#!/bin/env/python3

from bs4 import BeautifulSoup

soup = BeautifulSoup(open('openwrt-00013.html'), "lxml")

k = soup.find('div', id='content')
print(k)
