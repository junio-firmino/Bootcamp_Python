# Create Password
import random

letras = ['a', 'b',  'c', 'd', 'e', 'f', 'g', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
          'x', 'z', 'w']

letras_M = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
            'X', 'Z', 'W']

number = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

simbol = ['!', '#', '@', '$', '%', '&', '*', '(', ')', '_', '+']


q_letras = int(input('Qual a quantidade de letras minúscula? '))
q_letras_M = int(input('Qual a quantidade de letras MAIÚSCULA? '))
q_number = int(input('Qual a quantidade de numeros? '))
q_simbol = int(input('Qual a quantidade de simbolos? '))

password = []

for letra in range(1, q_letras+1):
    password += random.choice(letras)
    # print(password)

for letra in range(1, q_letras_M+1):
    password += random.choice(letras_M)
    # print(password)

for letra in range(1, q_number+1):
    password += random.choice(number)
    # print(password)

for letra in range(1, q_simbol+1):
    password += random.choice(simbol)
    # print(password)


random.shuffle(password)

past = ''

for letra in password:
    past += letra

print(f'A senha final é --> {past}')
