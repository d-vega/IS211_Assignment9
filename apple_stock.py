#!/usr/bin/env
# -*- coding: utf-8 -*-
"""IS211 Assignment 9 by Diandra Vega - Parse Apple stock and return
date with its close price."""


from bs4 import BeautifulSoup
import urllib2


APPLE_STOCK = urllib2.urlopen("https://www.nasdaq.com/symbol/aapl/historical")
SOUP = BeautifulSoup(APPLE_STOCK.read(), 'lxml')
STOCK = SOUP.tbody.find_all("tr")


for item in STOCK:
    row = [text for text in item.stripped_strings]
    if len(row) == 0:
        pass
    else:
        data = "{}: Close Price is ${}".format(row[0], row[4])
        print data
