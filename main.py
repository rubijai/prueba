print('Hola a todos')
str1 = 'INPUT THE TIME, RANGE FROM OAR_MsgParam1 TO OAR_MsgParam2 MINUTES!'
x = str1.split(' ')
print(x)
valor_oar1 = 5
valor_oar2 = 12
z = {}
print(type(z))

for y in x:
    if y == 'OAR_MsgParam1':
        z[y] = valor_oar1
    if y == 'OAR_MsgParam2':
        z[y] = valor_oar2

print(z)
print(z['OAR_MsgParam1'])
#Range = f"Range = {(z['OAR_MsgParam1'] - z['OAR_MsgParam2'])} Minutes"
#print(Range)
str2 = f"INPUT THE TIME, RANGE FROM OAR_MsgParam1 = {z['OAR_MsgParam1']} TO OAR_MsgParam2 = {z['OAR_MsgParam2']} MINUTES!"
str3 = f"INPUT THE TIME, RANGE FROM  {z['OAR_MsgParam1']} TO  {z['OAR_MsgParam2']} MINUTES!"
print(str2)
print(str3)

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

print(MENU['cappuccino']['ingredients']['water'])
print(MENU['cappuccino']['cost'])
print(resources['coffee'])
