
motion_dic = {}
flag = True

def maior_number (dic_bids):
    value = 0
    for bider in dic_bids:
        value_bids = dic_bids[bider]
        if value_bids > value:
            highest_value = value_bids
            highest_person = bider
    print(f'A pessoa que deu a melhor proposta foi {highest_person.title()} no valor de {highest_value}.')


while flag:
    name = input('qual o seu nome? ')
    price = int(input('qual a sua proposta? $ '))

    motion_dic[name] = price
    question = input('Você quer cadastrar mais propostas? "s" ou "n"')
    if not question == 's':
        flag = False
        maior_number(dic_bids=motion_dic)

