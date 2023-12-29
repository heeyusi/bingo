#importões
import random
import time

#lista de numero
numbers = list(range(1,76))
drawn_numbers = []
count = 1

#apresentação
print('Bem-vindo ao Sorteador de bingo')
time.sleep(3)
print('Para realiazar um sorteio, basta apertar a tecla ENTER')
time.sleep(3)
print('Está tudo pronto para seu sorteio acontecer, aperte ENTER para começar!')
#sorteador 
while len(numbers) != 0:
    drawn_number = random.choice(numbers)
    drawn_numbers.append(drawn_number)
    input() #pausa do programa
    print('Sorteio nº{0}:'.format(count))
    count += 1
    print(drawn_number)
    numbers.remove(drawn_number)

#formatação da lista dos numeros sorteados
drawn_numbers_formatted = ', '.join(map(str, drawn_numbers))
    
#finalização
time.sleep(3)
print('Todos os números foram sorteados')
time.sleep(3)
answer = input('Você deseja ver os números sorteados?: ')
if answer == "Sim":
    print('Aqui estão os números sorteados em ORDEM para possíveis problemas')
    time.sleep(1)
    print('Números sorteados: {0}'.format(drawn_numbers_formatted))
elif answer == "Não":
    print('Obrigado por usar o sorteador, volte sempre')
else: 
    print('Não entendemos sua resposta, poderia escrever dessa maneira: Sim ou Não')
