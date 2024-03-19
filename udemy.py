'''n = input('n_dos_dig : ')
sum = int(n[0]) +int(n[1]) 
print(sum) 
print(int(n[0]) +int(n[1]))

h = float(input('alt(m) : '))
w = float(input('peso(kg) : '))
BMI = w/h**2
print(int(round(BMI,2)))


edad = int(input('edad : '))
y_left = 90 - edad
m_left = y_left*12
s_left = y_left*52
d_left = y_left*365
print(f'Ud. le quedan {d_left} days, {s_left} semanas, {m_left} meses ')


n = int(input('n = '))
if n % 2 == 0:
    print('n es par')
else:
    print('n es impar')

h = int(input('h(cm) = '))
e = int(input('edad = '))
if h >= 150:
    if e > 20:
        print('Tiene que pagar $15')
    elif 15<e<=20:
        print('Tiene que pagar $10')
    else:
        print('Tiene que pagar $5')

else:
    print('Lo siento, no puede entrar')
h = float(input('alt(m) : '))
w = float(input('peso(kg) : '))
BMI = w/h**2
res = float(round(BMI,1))
print(res)

if res < 18.5:
    print(f'Su BMI es {res}, Ud tiene peso bajo')
elif 18.5 < res < 25:
    print(f'Su BMI es {res}, Ud tiene peso normal')
elif 25 < res < 30:
    print(f'Su BMI es {res}, Ud tiene sobrepeso ')
elif 30 < res < 35:
    print(f'Su BMI es {res}, Ud es obeso ')
else:
    print(f'Su BMI es {res}, Ud es obeso clinico')

año = int(input('año : '))
if año % 4 == 0:
    if año % 100 == 0:
        if año % 400 == 0:
            print(f'El año {año} es bisiesto')
        else:
            print(f'El año {año} no es bisiesto')
    else:
        print(f'El año {año} no es bisiesto')
else:
    print(f'El año {año} no es bisiesto')





h = int(input('h(cm) = '))
e = int(input('edad = '))
foto = input('Quiere una foto : (si o no)')
if foto == 'si':
    precio = 5
else:
    precio = 0
if h >= 150:
    if e > 20:
        precio += 15
        print(f'Tiene que pagar ${precio}')
    elif 15<e<=20:
        precio += 10
        print(f'Tiene que pagar ${precio}')
    else:
        precio += 5
        print(f'Tiene que pagar ${precio}')

else:
    print('Lo siento, no puede entrar')

h = int(input('h(cm) = '))
if h < 150:
    print('Lo siento, no puede entrar')
else:
    e = int(input('edad = '))
    if e > 20:
        precio = 15
        
    elif 15<e<=20:
        precio = 10
        
    else:
        precio = 5
        
foto = input('Quiere una foto : (si o no)')
if foto == 'si':
    precio += 5
print(f'Valor de la boleta : ${precio}')





print('Bienvenido a Pizza Delivery')
size = input('Tamaño de la pizza (p,m,g): ')
pep  = input('Pepperoni : si, no: ')
eq   = input('Extra queso : si, no: ')
if size == 'g':
    precio = 25
if size == 'm':
    precio = 20
if size == 'p':
    precio = 15
if pep == 'si':
    if size == 'p':
        precio += 2
    else:
        precio += 3
if eq == 'si':
    precio += 1

print(f'Ud. debe pagar un total de: ${precio}')






h = int(input('h(cm) = '))
e = int(input('edad = '))
foto = input('Quiere una foto : (si o no)')
if foto == 'si':
    precio = 5
else:
    precio = 0

if h >= 150:
    if e > 20 and 45 < e < 55:
        print('Ud entra gratis')
    elif e > 20 and not(45 < e < 55):     
        precio += 15
        print(f'Tiene que pagar ${precio}')
    elif 15<e<=20:
        precio += 10
        print(f'Tiene que pagar ${precio}')
    else:
        precio += 5
        print(f'Tiene que pagar ${precio}')

else:
    print('Lo siento, no puede entrar')


name1 = input('Entre su nombre: ')
name2 = input('Entre nombre de su amor: ')
n1 = name1.lower()
n2 = name2.lower()
n = n1+n2
print(n)
y = n.count('e')
print(y)
c1 = 0
for let in 'true':
    c1 += n.count(let)
print(c1)
c2 = 0
for let in 'love':
    c2 += n.count(let)
print(c2)
score = int(str(c1) + str(c2))

if score < 10 or score > 90:
    print(f' your score is {score} ,you go together like coke and mentos')
elif 40 < score < 50 :
    print(f' your score is {score} , you are alright  together ')
else:
     print(f' your score is {score} ')

import random as rn
for i in range(10):
    n1 = round(5*rn.random(),2)
    n2 = rn.randint(0,10)
    n3 = round(rn.uniform(0,10),2)
    print(n1, n2, n3)
    if n1 >= 2.5:
        print('Sello')
    else:
        print('Cara')

import random as rn
names = input(' Entre nombre de personas en la mesa separados por comas: ')
l_names = names.split(',') 
print(l_names) 
i = rn.randint(0,len(l_names))
choice1 = l_names[i] 
print(f'Hoy la cuenta la debe pagar {choice1}') 
choice2 = rn.choice(l_names)
print(f'Hoy la cuenta la debe pagar {choice2}')





row1 = ['_','_','_']
row2 = ['_','_','_']
row3 = ['_','_','_']
map = [row1,row2,row3]
print(f'{row1}\n{row2}\n{row3}')
fila = int(input('fila: '))
col  = int(input('col: '))
map[fila-1][col-1] = 'X'
print(f'{row1}\n{row2}\n{row3}')'''

import random 

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

sel_usuario = int(input('what do you choose? Type 0 for rock, 1 for paper, 2 scissors: '))
while sel_usuario < 0 or sel_usuario > 2:
    print('Solo puede selecionar 0, 1 o 2')
    sel_usuario = int(input('what do you choose? Type 0 for rock, 1 for paper, 2 scissors: '))


imagenes =[rock, paper, scissors]



print(imagenes[sel_usuario])
sel_comp = random.randint(0,2)

print(imagenes[sel_comp])

if sel_usuario == 0 and sel_comp == 2:
    print('Ud. gana')
    
elif sel_usuario == 1 and sel_comp == 0:
    print('Ud. gana')
elif sel_usuario == 2 and sel_comp == 1:
    print('Ud. gana')
elif sel_usuario == sel_comp:
    print('Ud. empata')
else:
    print('Ud. pierde')

    





####### Debugging challenge: #########
#Try running this code and type 5.
#It will give you an IndexError and point to line 32 as the issue.
#But on line 38 we are trying to prevent a crash by detecting
#any numbers great than or equal to 3 or less than 0.
#So what's going on?
#Can you debug the code and fix it?
#Solution: https://repl.it/@appbrewery/rock-paper-scissors-debugged-end


print('''
--------------------------------------------------
°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
''')

