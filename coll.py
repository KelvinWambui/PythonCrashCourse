#collections
#class in python that helps manipulate various methods

from collections import Counter
'''
c=Counter('balabs')
lnum=c['l']
if lnum>1 :
    print('the number of l is greater than 1 and is %d' %(lnum))
else :
    print ('the number of l is less than one')


c=Counter(['a','a','s','s','d'])
print(c)
print(list(c.elements()))
print(c.most_common(3))
c=Counter({'a':2,'b':3})
print(c)
print(c['a'])
c=Counter(dogs=4,cats=9)
print(c)

print(list(c.elements()))
'''
c=Counter(a=4,b=3,c=2,d=-2)
d=['a','b','b','c','d']

#c.subtract(d)
c.update(d)

print(c)
