# !/usr/local/bin/python
# -*- coding: utf-8 -*-

import csv

with open('datecolor.csv') as csvfile:
    # read a csv file, the row of the fiel is separated by ','
    readCSV = csv.reader(csvfile,delimiter=',')

    dates=[]
    colors=[]
    
    # get into the csv.reader object
    for row in readCSV:
        color=row[1]
        date=row[0]

        dates.append(date)
        colors.append(color)

    print(dates)
    print(colors)
    
    try:
        # user can input using `raw_input` in python
        whatcolor=raw_input('what color do you wish to know the date of?')

        if whatcolor in colors:
            # get the index of an element in a list. If multiple the same, the first one's index is extracted
            coldex = colors.index(whatcolor)
            theDate = dates[coldex]
            print('The date of', whatcolor, 'is', theDate)
        else:
            print('Not found')
    # except Exception, e ## this what happens in python2
    except Exception, e:
        print(e)
