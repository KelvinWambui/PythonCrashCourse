# static and class methods

class User(object):
    population=5000
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    @classmethod
    def getpopulation(cl):
        print(cl.population)
    
    @staticmethod
    def Isadult(age):
        return age>=18
    
    def display(self):
        print(f'your name is {self.name} and your age {self.age}')


user=User('Kelvin',80)

user.getpopulation()
ageCon=user.Isadult(34)

if ageCon :
    print('you are an adult')
else :
    print('Plesase you are under 18')

