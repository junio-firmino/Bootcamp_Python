import random

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
    card = random.choice(cards)
    return card

user_cards = []
computer_cards = []

for i in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

def calculate_score(**kwargs):
    y1 = kwargs.get('y')
    z1= kwargs.get('z')
    total = sum(y1+z1)
    return total


print(user_cards,computer_cards)


x =calculate_score(y = user_cards,z=computer_cards)
print(x)