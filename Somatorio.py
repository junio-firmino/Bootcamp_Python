# lista = [1,2,3,50]
# #for i in lista:
# y = sum(lista)
#
# print(y)

def soma(ar):
    y = sum(ar)
    print(y)


# lista = [1,2,3,50]
# w = soma(lista)
lista = []
flag = True
while flag:
    c = int(input('qual os número? '))
    lista.append(c)
    print(lista)
    x = input('quer finalizar? ')
    if x == 'f':
        flag = False
    else:
        flag = True
w = soma(lista)












