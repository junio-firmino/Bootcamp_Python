import random
word_list = ['cafe', 'carro', 'empilhadeira']
chosen_word = random.choice(word_list)
num_word = len(chosen_word)

print(f'A palavra escolhida é {chosen_word}')

suges = input('qual a sua sugestão de letra? ').lower()

dis = []
for letter in range(num_word):
    dis += "-"


for letter_1 in range(num_word):
    position = chosen_word[letter_1]
    if position == suges:
        dis[letter_1] = position

print(dis)