#optional functional parameters 
def func(word,freq=1):
    return word*freq

call=func('kelvin',10)
print(call)

class car():
    def __init__(self,name,year,model,make,color,milage):
        self.name=name
        self.year=year
        self.model=model
        self.make=make
        self.color=color
        self.milage=milage
    def display(self,showall) :
        if showall:
             print(f'The car name is {self.name} \n the year of make is {self.year} \n the model is {self.model} its color is {self.color} \n and the milage is {self.milage}')
        else :
             print(f'The car name is {self.name} and the year of make {self.year}')
          

Car=car('tesla','2020','Model x','Station wagon','black',2000202002)

Car.display(True)


    


