## this code cannot be run cause I am too lazy to produce the csv file

import csv

with open('extension.csv') as csvfile:
    readCSV = csv.reader(csvfile,delimiter=',')

    dates=[]
    colors=[]
    
    for row in readCSV:
        color=row[2]
        date=row[0]

        dates.append(date)
        colors.append(color)

    print(dates)
    print(colors)
    
    try:
        whatcolor=input('what color do you wish to know the date of?')

        if whatcolor in colors:
            coldex = colors.index(whatcolor.upper())
            theDate = dates[coldex]
            print('The date of', whatcolor, 'is', theDate)
        else:
            print('Not found')
    # except Exception, e ## this what happens in python2
    except Exception as e:
        print(e)

    print('continuing')
