#use of filters
#filters are used to map a function that is has a specific filter purpose to a list

def func(x) :
    return x*7
def isOdd(x) :
    return x%2 != 0

li=[2,6,77,89,44,223,4,678,987,4456,7565,9907,3445,7675,244456,775667675,4333254]

#a=list(filter(isOdd,li))
b=list(map(func,filter(isOdd,li)))
print(b)

