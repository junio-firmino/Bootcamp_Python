import random
word_list = ['cafe', 'carro', 'empilhadeira']
chosen_word = random.choice(word_list)
num_word = len(chosen_word)

print(f'A palavra escolhida é {chosen_word}')

dis = []
for letter in range(num_word):
    dis += "-"

end = False
count = 0
while not end:
    count += 1

    suges = input('qual a sua sugestão de letra? ').lower()


    for letter_1 in range(num_word):
        position = chosen_word[letter_1]
        if position == suges:
            dis[letter_1] = position

    print(dis)
    if count == 3:
        end = True
        print('Você não venceu')