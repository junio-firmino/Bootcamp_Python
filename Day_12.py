from Day_12_logo import Logo
from random import randint
from replit import clear

hard_level = 5
easy_level = 10

def game():
    print(Logo)
    print('Welcome to the number guessing game!')
    print("Choose a number between 1 a 100")
    answer = randint(1, 100)
    print(answer)

    turns = set_difficulty()
    #check_answer(resposta_com=answer, escolha=guess, number_turns=turns)
    guess = 0
    while guess != answer:
        clear()
        print(f'You have only {turns} changes.')
        guess = int(input('Qual a sua escolha? '))
        turns = check_answer(resposta_com=answer,escolha=guess,number_turns=turns)  # Essa classe armazena as informações e muda o Turns
        # if guess == answer:
        #     print('você acertou')
        #     return
        if turns == 0:
            print(f'You lose because all changes was used and the number secret is {answer}.')
            return





def check_answer(resposta_com, escolha, number_turns):
    if escolha > resposta_com:
        print('Too high.')
        return number_turns - 1
    elif escolha < resposta_com:
        print('Too low.')
        return number_turns - 1
    else:
        print('Você acertou.')



def set_difficulty():
    question = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if question == 'e':
        return easy_level
    else:
        return hard_level


game()