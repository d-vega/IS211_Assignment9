#!/usr/bin/env
# -*- coding: utf-8 -*-
"""IS211 Assignment 9 by Diandra Vega - Parse CBS NFL stats
webpage and return top 20 players with their total touchdowns"""


from bs4 import BeautifulSoup
import urllib2


TOUCHDOWNS_PG = urllib2.urlopen("https://www.cbssports.com/nfl/stats/player"
                                "sort/nfl/year-2018-season-regular-"
                                "category-touchdowns")
SOUP = BeautifulSoup(TOUCHDOWNS_PG.read(), features='lxml')
PLAYERS = SOUP.find_all("tr", class_={"row1", "row2"})
PLYR_LIST = []
COUNTER = 0
POSITION = 0


for a_tag in PLAYERS:
    match = a_tag.find_all('a')
    touchdowns = a_tag.find_all("td", class_={"sort"})
    name_team = [i.text for i in match]
    plyr_td = [t.text for t in touchdowns]
    PLYR_LIST.append(name_team)
    for touchdown in plyr_td:
        PLYR_LIST[COUNTER].append(touchdown)
    COUNTER += 1


for player in PLYR_LIST[:20]:
    POSITION += 1
    info = "{}. {} has {} touchdown(s) and is from team {}.".format(POSITION,
                                                                    player[0],
                                                                    player[2],
                                                                    player[1])
    print info
