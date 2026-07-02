'''
modulo04 - Estruturas de dados -Lista

modulo04 - Estruturas de dados - tuplas
'''
dias_da_semana = ("Segunda", "Terça", "Quarta", "Quinta", "Sexta") 
print("dias_da_semana")

print("olá tudo bem, bem vindo a meu mundo, oque vôce deseja adicionar a esse semana:")

dia_favorito = input('Seu dia da semana favorito é: ')
print()
if dia_favorito == "Segunda":
    print('meio chato')

elif dia_favorito == "Terça":
    print('razoavel!')

elif dia_favorito == "Quarta":
    print('legalzinho')

elif dia_favorito == "Quinta":
    print('quase final de semana')

elif dia_favorito == "Sexta":
    print('Que acerto é realmente o melhor dia!')

elif dia_favorito == "Sabado":
    print('Melhor dia do fim de semana')

elif dia_favorito == "Domingo":
    print('Domingo é dia de Macarronada 🍜')   
else:\
    print("Opção invalida, Por favor escreva com a primeira letra Maiuscula!")
