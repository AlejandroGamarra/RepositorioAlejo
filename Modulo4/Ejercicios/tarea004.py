#Ejercicio1 Problema1

def problema1():
    n=0
    while n<1 or n>10:
        n = int(input('Ingrese un nro del 1 al 10: '))
    with open(f'./tabla-{n}.txt', 'w') as f:
        for i in range(1, 13):
            texto=f'{i} x {n} = {i*n}\n'
            f.write(texto)
    for i in range(1, 13):
        print(f'{i} x {n} = {i*n}\n')
    

problema1()

#Ejercicio1 Problema 2

def E1_P2():
    n=0
    while n<1 or n>10:
        n = int(input('Ingrese un nro del 1 al 10: '))
    
    try:
        with open(f'./tabla-{n}.txt', 'r') as f:
            texto = f.read()
            print(f"{texto}")
    except:
        print("Archivo no encontrado")

E1_P2()

#Ejercicio1 Problema3

def E1_P3():
    n=0
    while n<1 or n>10:
        n = int(input('Ingrese un nro del 1 al 10: '))
    
    try:
        with open(f'./tabla-{n}.txt', 'r') as f:
            lista_texto = f.readlines()
            m=int(input('ingrese la linea m: '))
            print(f"{lista_texto[m-1]}")
    except:
        print("Archivo no encontrado")

E1_P3()


#Problemas de Expresiones Regulares

#Problema 01
# Cadena entrada
import re
s = '@robot9! @robot4& I have a good feeling that the show isgoing to be amazing! @robot9$ @robot7%'
s
print(re.findall(r"@robot\d\W", s))

#Problema 02
# Cadena entrada
s = "Unfortunately one of those moments wasn't a giant squid monster. User_mentions:2, likes: 9, number of retweets: 7"
s
print(re.findall(r"User_mentions:\d", s))
print(re.findall(r"likes: \d", s))
print(re.findall(r"number of retweets: \d", s))

#Problema 03
import re

cadena= """AIshadowhunters.txt aaaaand back to my literature review. At least i have a friendly cup aeOprueba.txt of coffee to keep me company
ouMYTAXES.txt I am worried that I won't get my $900 even though I paid tax last year"""


posibles=re.findall(r"^[aeiouAEIOU]{2,3}\w*.txt", cadena)
print(f"{posibles}")

#Problema04
# Escriba una expresión regular para validar un correo
regex = r""

emails = ['n.john.smith@gmail.com', '87victory@hotmail.com', '!#mary-=@msca.net']
for example in emails:
    # Match the regex to the string
    if re.match(regex, example):
        # Complete the format method to print out the result
        print("The email {email_example} is a valid email".format(email_example=example))
    else:
        print("The email {email_example} is invalid".format(email_example=example))  


##EJERCICIO 2 ###
import re
regex=r"[456][0-9]{3}-?[0-9]{4}-?[0-9]{4}-?[0-9]{4}"
tarjetas = ['4123456789123456','5123-4567-8912-3456','61234-567-8912-3456','4123356789123456','5133-3367-8912-3456','5123 - 3567 - 8912 - 3456']
for f in tarjetas:
    if re.match(regex,f):
        print(f"{f} es Valido")
    else:
        print(f"{f} NO es Valido") 