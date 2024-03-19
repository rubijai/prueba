
import random as rn

'''names = ['tim', 'tom', 'jack', 'jim', 'pete']
for nom in names:
    print(nom) 

alt_est = input('lista altura estudiantes en cm separadas por coma: ' )
print(alt_est,type(alt_est))
alt_tot = []
for x in alt_est.split(' '):
    alt_tot.append(int(x))
total = sum(alt_tot)
prom_alt = int(round(total/(len(alt_est.split())))) 
print(prom_alt)
print(max(alt_tot))

#Promedio
list = [12,15,44,56,87,23,45]
suma = 0
for x in list:
    suma += x
promedio = round(suma/len(list),2)
prom = int(round(sum(list)/len(list),0))
print(promedio,prom)
prom1 = round(sum(list)/len(list),2)
print(max(list))
print(prom1,max)
print(min(list))
min = list[0]
for x in list:
    if x < min:
        min = x
print(min)

#sumar los numeros 1 hasta n

n = int(input('n : '))
sum = 0
for i in range(1,n+1):
    sum += i
print(sum)
sum = 0
for i in range(0,n+1,2):
    sum += i
print(sum)

#Fizzbuzz game
for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0 and i % 5 != 0:
        print('Fizz')
    elif i % 5 == 0 and i != 0:
        print('Buzz') 
    else:
        print(i)





print('Password Generator')
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 
's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 
'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']





let = int(input('num de letras: '))
sim = int(input('num de simbolos: '))
dig = int(input('num de digitos: '))
password = ''
for i in range(let):
    password += rn.choice(letters)
print(password)

for i in range(sim):
    password += rn.choice(symbols)
print(password)

for i in range(dig):
    password += rn.choice(numbers)
    print(password)
    new_passw = []
    for x in password:
        new_passw.append(x)
        rn.shuffle(new_passw)
final_pw = ('').join(new_passw)
print(final_pw)'''

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

word_list = ["aardvark", "baboon", "camel"]

pal = rn.choice(word_list)
pal1 = []
pal2 = []
for i in range(len(pal)):
    pal1.append(' ')
print(pal1)

vidas = 7
print(vidas)
while vidas != 0:
    letra = input('letra: ')
    if letra in pal:
        i = pal.find(letra)
        pal1[i] = letra
        if ' ' not in pal1:
            vidas = 0
            print('You win ')
        
        print(pal1)
        
    else:
        print(HANGMANPICS[-vidas])
        vidas -= 1
        print(vidas)
        if vidas == 0:
        
            print('You loose')
        













print('''
--------------------------------------------------
°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
''')

