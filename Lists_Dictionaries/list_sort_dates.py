#!/usr/bin/env python3
from datetime import datetime

dates = ['3-Jan-2016', '4-Mar-2015', '2-Aug-1999', '1-May-2000']
print(dates)
dates.sort()
print(dates)

#newdates = [ datetime.strptime(d,"%d-%b-%Y") for d in dates ]
newdates = []
print(newdates)
for str in dates:
    newdates.append(datetime.strptime(str,'%d-%b-%Y'))
print(newdates)
newdates.sort()
print(newdates)

for n in newdates:
    print(datetime.strftime(n,"%Y-%b-%d")," OR ", 
          datetime.strftime(n,"%Y-%m-%d"), " OR ",
          datetime.strftime(n,"%A, %b %d, %Y"), " OR ",
          datetime.strftime(n,"%c")
    )
