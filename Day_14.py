from Game_data import data
import random
from Day_12_logo import Logo

#print(Logo)
score = 0

def format_data(acount):
    """ Format the data  """
    account_name = acount['name']
    account_descr = acount['description']
    account_follower = acount['follower_count']
    account_country = acount['name']
    return f'{account_name}, {account_descr}, {account_country} e {account_follower}'

def check_answer (follower_1, follower_2, option):
    if follower_1 > follower_2:
        return option == "a"
    else:
        return option == "b"

acount_b = random.choice(data)
flag = True

while flag:
    acount_a = acount_b
    acount_b = random.choice(data)
    if acount_a == acount_b:
        acount_b = random.choice(data)


    print(f'Compare A: {format_data(acount_a)}. ')
    print(f'Compare B: {format_data(acount_b)}. ')

    guess = input('Who has more followers? Type "A" or "B" -->  '). lower()
    follower_a = acount_a["follower_count"]
    follower_b = acount_b["follower_count"]
    is_correct = check_answer(follower_1=follower_a, follower_2=follower_b, option=guess)
    if is_correct:
        score += 1
        print(f'Você acertou é acumulou o score de {score}')
    else:
        flag = False
        print(f'Desculpe!, Infelizmente você errou e sua pontuação final é de {score}')





