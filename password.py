# Create Password
import random

letras = ['a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e', 'E', 'f', 'F', 'g', 'G', 'i', 'I', 'j', 'J', 'k', 'K',
          'l', 'L', 'm', 'M', 'n', 'M', 'o', 'O', 'p', 'P', 'q', 'Q', 'r', 'R', 's', 'S', 't', 'T', 'u', 'U',
          'v', 'V', 'x', 'X', 'z', 'Z', 'w', 'W']

number = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

simbol = ['!', '#', '@', '$', '%', '&', '*', '(', ')', '_', '+']


q_letras = int(input('Qual a quantidade de letras? '))
q_number = int(input('Qual a quantidade de numeros? '))
q_simbol = int(input('Qual a quantidade de simbolos? '))

password = []

for letra in range(1, q_letras+1):
    password += random.choice(letras)
   # print(password)

for letra in range(1, q_number+1):
    password += random.choice(number)
    #print(password)

for letra in range(1, q_simbol+1):
    password += random.choice(simbol)
    #print(password)

random.shuffle(password)

past = ''

for letra in password:
    past += letra

print(f'A senha final é --> {past}')
