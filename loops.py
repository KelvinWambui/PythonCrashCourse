#loops 

people = ['john', 'cassie','goge','lydia','ferzul']

'''
for person in people :
    if person=='goge' :
        continue
    print(f'current person:{person}')


for i in range(0,11) :
    print(f'number : {i}')


for i in range(len(people)) :
    print(f'the {i} person is {people[i]}')
'''
count = 0

while count<len(people) :
    print(f'current person :{people[count]}')
    count += 1