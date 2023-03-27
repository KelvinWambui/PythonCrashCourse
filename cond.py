#conditional in python

x=90
y=81
z=11
'''
if x>y :
    print(f'{x} is greater than {y}')
elif x==y :
    print(f'{x} is equal {y}')
elif x<=y :
    print(f'{x} is not equal to {y}')
elif y>x :
    print(f'{y} is  greater than {x}')    

if x>y or x==z :
    print(f'{x} is greater than {y} and {x} is equal to {z}')
 '''

numbers =[1,2,2,10,90]  
is_b=bool
if x not in numbers :
    is_b=x in numbers
    
if is_b==True :
    print(f'{x} is not in numbers')
else :
    print(f'{x} in numbers')
    