#!/usr/bin/env
# -*- coding: utf-8 -*-
"""IS211 Assignment 9 by Diandra Vega"""


from bs4 import BeautifulSoup
import urllib2
import json


TOUCHDOWNS_PG = urllib2.urlopen("https://www.cbssports.com/nfl/stats/player"
                                "sort/nfl/year-2018-season-regular-"
                                "category-touchdowns")
soup = BeautifulSoup(TOUCHDOWNS_PG.read(), features='lxml')
players = soup.find_all("tr", class_={"row1", "row2"})
players_td = soup.find_all("td", class_={"sort"})
plyr_list = []
plyr_list_decode = []
counter = 0


for a_tag in players:
    match = a_tag.find_all('a')
    touchdowns = a_tag.find_all("td", class_={"sort"})
    name_team = [i.text for i in match]
    plyr_td = [t.text for t in touchdowns]
    plyr_list.append(name_team)
    for touchdown in plyr_td:
        plyr_list[counter].append(touchdown)
    counter += 1


for item in plyr_list:
    tmp_list = []
    for content in item:
        print content
        decoded = content.decode("ascii")
        tmp_list.append(decoded)
    plyr_list_decode.append(tmp_list)


print plyr_list_decode
