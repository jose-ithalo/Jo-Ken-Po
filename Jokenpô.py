from random import choice
from time import sleep

lista = ['pedra', 'papel', 'tesoura']

print('\033[0;33mVamos jogar Jokenpô!\033[m '.center(40))
print()
print('''Suas opções:
 pedra
 papel
 tesoura''')
print('-' * 36)
jogador = str(input('Faça a sua jogada aqui: ')).lower().strip()
computador = choice(lista)
print('Jo')
sleep(1)
print('Ken')
sleep(1)
print('Pô!!!')
sleep(1)
print('-=' * 18)
print('Você escolheu {}'.format(jogador))
print('O computador escolheu {}'.format(computador))
print('-=' * 18)
if jogador == 'pedra':
    if computador == 'pedra':
        print('Empate!')
    elif computador == 'papel':
        print('Eu ganhei ☺')
    else:
        print('Você venceu :(')
elif jogador == 'papel':
    if computador == 'pedra':
        print('Você venceu :(')
    elif computador == 'papel':
        print('Empate!')
    else:
        print('Eu ganhei ☻')
elif jogador == 'tesoura':
    if computador == 'pedra':
        print('Eu ganhei ☺')
    elif computador == 'papel':
        print('Você venceu :(')
    else:
        print('Empate!')
else:
    print('\033[0;31mEscolha inválida\033[m')


