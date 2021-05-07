import random

def deal_card():
    '''Function for choice the cards in amount.'''
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
    card = random.choice(cards)
    return card

user_cards = []
computer_cards = []

for i in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

def calculate_score(cards_1):  #
    '''Function calculate the score from the cards chosen. '''
    if sum(cards_1) == 21 and len(cards_1) == 2:
        return 0
    if 11 in cards_1 and sum(cards_1)>21:
        cards_1.remove(11)
        cards_1.append(1)

    return sum(cards_1), (cards_1)





x = calculate_score(user_cards)
y = calculate_score(computer_cards)
print(x)
print(y)