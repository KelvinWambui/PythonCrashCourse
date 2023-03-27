import json

userJSON='{"Firstname":"Kelvin","lastname":"Mutua","age":27}'

user=json.loads(userJSON)

print(user['Firstname'])
print(user)

car={'name':'tesla','model':2009}

carJSON=json.dumps(car)

print(carJSON)