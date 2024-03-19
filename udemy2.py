import math as m
'''
def greeting(name,city):
    print(f'Hello {name} ')
    print(f'My name is JR I am in {city}')
    print('How are you today')
        
greeting('Angela', 'Cali')


def cal_area(alt, anch, cov):
    n_pot = m.ceil(alt*anch/cov)
    return f'El numero de potes es {n_pot}'
a = 2
b = 4
c = 5
print(cal_area(a,b,c))


#prime numbers

def prime_numbers(list):
    n_primos = [2,3,5,7,11,13]
    for n in list:
        
        if (n>13 and n%2 != 0 and n%3!= 0 and n%5!=0 and n%7!=0 and n%11!=0 and n%13!=0 ): 
            n_primos.append(n)
    return n_primos

list = []
for n in range(201):
    list.append(n)

primos = prime_numbers(list)
print(primos)
es_primo = int(input('numero: '))
if es_primo in primos:
    print(f'{es_primo} es un numero primo')
else:
    print(f'{es_primo} no es un numero primo')


def checker(numero):
    for i in range(2,numero):
        if numero%i == 0:
            return f'{es_primo} no es un numero primo'
            break
        
        return f'{es_primo} es un numero primo'
            
print(checker(es_primo))

def es_pri(numero):
    es_prim = True
    for i in range(2,numero):
        if numero%i == 0:
            es_prim = False
    if es_prim:
        return f'{es_primo} es un numero primo'
    else:
        return f'{es_primo} no es un numero primo'

print(es_pri(es_primo))

#Encriptar
alfabeto = "a, b, c, d, e, f, g, h, i, j, k, l, m, n, ñ, o, p, q, r, s, t, u, v, w, x, y, z, a, b, c, d, e, f, g, h, i, j, k, l, m, n, ñ, o, p, q, r, s, t, u, v, w, x, y, z"
#print(alfabeto.strip(' '))
alfa_list= alfabeto.split(', ')   # lista de letras

def encript(texto):
    
    n_text =texto.lower()
    print(n_text)
    t = list(n_text)
    #print(len(t))
    #print(t)

    for i in range(len(t)):
        if t[i]!=' ':
        #print(t[i])
        
            j = alfa_list.index(t[i])
        #print(j)
        
            t[i] = alfa_list[j+2]
    return ('').join(t)
texto = 'Hola JaimeZ'

t_encript = encript(texto)
print(t_encript)

def desencript(text):
    n_text =text.lower()
    t = list(n_text)
    #print(len(t))
    #print(t)

    for i in range(len(t)):
        if t[i]!=' ':
        #print(t[i])
        
            j = alfa_list.index(t[i])
        #print(j)
        
            t[i] = alfa_list[j-2]
    return ('').join(t)

t_desencript = desencript(t_encript)
print(t_desencript)





# Diccionarios
calif_est = {
    'Jim' : 84,
    'Joe' : 92,
    'Tom' : 75,
    'Tim' : 62,
    'Jack': 84,
}
calif_est['Bill'] = 99
print(calif_est)
grade_est = {}
for key in calif_est:
    if 91 <= calif_est[key]<=100:
        grade_est[key] = 'excelente'
    elif 81< calif_est[key]<90:
        grade_est[key] = 'Excede expectativas'

    elif  71  <= calif_est[key]<=80:
        grade_est[key] = 'Aceptable'

    else:
        grade_est[key] = 'Raspado'

print(grade_est)




def add_new_country(country,visits,cities):
    new_dict = {}
    new_dict[ 'country'] = country
    new_dict[ 'visits'] = visits
    new_dict[ 'cities'] = cities
    return new_dict

travel_log = [
    {
    'country' : 'France',
    'visits' : 12,
    'cities' : ['Paris', 'Lille', 'Dijon'],
    },
    {'country' : 'Germany',
    'visits' : 6,
    'cities' : ['Berlin', 'Hamburg', 'Stuttgart'],
    }     
]
print(travel_log)
country = 'Russia'
visits = 2
cities = ['Moscow','Saint Petersburg']
travel_log.append(add_new_country(country,visits,cities))
print(travel_log)


subasta = {}
subasta_open = True
while subasta_open == True:

    nombre = input('Nombre : ')
    bid = int(input('Bid :'))
    subasta[nombre] = bid
    Max_sub = subasta[nombre]
    mas_ofertas = input('¿Hay mas participantes? entre si o no: ')
    if mas_ofertas == 'no':
        subasta_open = False
    print(subasta)

for key in subasta:
    
    #print(Max_sub)
    #print(key)
    if subasta[key]>Max_sub:
        Max_sub = subasta[key]
        #print(Max_sub)
        
        ganador = key
        #print(ganador) 

        print(f'El ganador es {ganador} con una oferta de ${subasta[key]}')
 



bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  # bidding_record = {"Angela": 123, "James": 321}
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid: 
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
  name = input("What is your name?: ")
  price = int(input("What is your bid?: $"))
  bids[name] = price
  should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
  if should_continue == "no":
    bidding_finished = True
    find_highest_bidder(bids)
  elif should_continue == "yes":
    pass
    
  
def dias_en_mes(año, mes):
    if año == 366:
        dias_mes = [31,29,31,30,31,30,31,31,30,31,30,31]
    else:
        dias_mes = [31,28,31,30,31,30,31,31,30,31,30,31]
    return dias_mes[mes]
print(dias_en_mes(365,1))'''




def suma(n1,n2):
    return n1 +n2
def resta(n1,n2):
    return n1-n2
def multiplicacion(n1,n2):
    return n1*n2
def division(n1,n2):
    return n1/n2



operaciones = {
    '+':suma,
    '-':resta,
    '*':multiplicacion,
    '/':division
}
print(operaciones)
n1 = int(input('n1 = '))
n2 = int(input('n2 = '))


for key in operaciones:
    print(key)
simbolo = input('selecione un simbolo : ')
resp = operaciones[simbolo](n1,n2)
print(resp)

print(f'{n1} {simbolo} {n2} = {resp}')



print('''
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
''')



