#!/usr/bin/env python3
things = {}      # an empty dictionary
listofstuff = [] # an empty array
print(things)
things = {'diane': 10, 'jack': 13}
print(things)
things['diane']
things['billy'] = 15 # assign a new key/value pair
# if you have a list of pairs of things
strangerthings = dict([('Will', 12), ('Jim', 44), ('Joyce', 45), ('Eleven',11),('Lucas',10)])
print(strangerthings['Eleven'])
for key,value in strangerthings.items():
    print("key is", key,"value is",value)
