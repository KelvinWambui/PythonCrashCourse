#how to create classes

class User :
    def __init__(self,name,age ) :
        self.name=name
        self.age=age
     
    def greetings(self) :
     return f'greetings{self.name} you age is {self.age}'
    def adage(self) :
       self.age +=3   

#extending a class
class Customer(User):
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def addbalance(self, bal):
        self.bal=bal
    def greetings(self) :
     return f'greetings{self.name} you age is {self.age} your balance is {self.bal}'
     
      
cus=Customer('Janet',27)
cus.addbalance(1000)
print(cus.greetings())
user=User('kelvin',27)
user.adage()
result=user.greetings()
print(result)

    

        