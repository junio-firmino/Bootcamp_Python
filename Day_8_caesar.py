alphabet = [' ','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', '+', '-', '!', '@', '#', '$', '%', '&', '*', '/']



def caesar (initial, shift_amount, direction):
    flag = True
    while flag:
        end_text=""
        if direction == 'decore':
            shift_amount *= -1
        for letter in initial:
            posi = alphabet.index(letter)
            new_posi = posi + shift_amount
            new_posi = new_posi % 37
            end_text += alphabet[new_posi]
        print(f'Aqui foi escolhido a direção {direction} e o resultado foi {end_text}')

        question = input('Quer continuar?')
        if question == 's':
            flag = True
        else:
            flag = False




direction = input('qual a direção você quer? ')
text = input('Digite o seu texto? ')
shift = int(input('Quantos passos?'))
s = caesar(initial=text, shift_amount=shift,direction=direction)
s
