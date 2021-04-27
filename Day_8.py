# Número primo

def primo_num(num):
    is_prime = True
    for i in range (2, num):
        if num % i == 0:
            is_prime = False
    if is_prime:
        print('É primo!!')
    else:
        print('Não é primo!!')



num = int(input('qual o seu número? '))
primo_num(num= num)