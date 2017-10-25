#!/usr/bin/env python3
l = [ 'a', 100, 12/3.3 ]
print(l)
['a', 100, 3.6363636363636367]
#",".join(l) # this throws an error
";".join(map(str,l)) # have to cast numbers as string
l = [1,2,3,4]
print(l)
squares = list(map(lambda x: x**2, l))
print(squares)

l = ['zzz','yyy','a']
print(list(reversed(l)))
for n in reversed(l):
    print(n)
