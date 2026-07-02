while True:
    print("Bem-vindo ao programa de verificação de cardápio! \n")
    print('1 - Ver cardápio da semana')
    print('0 - sair do sistema')

    dias_semana = ('segunda-feira,terça-feira,quarta-feira,sexta-feira,sábado,domingo')
    cardapio_da_semana = {" "
    "segunda-feira": "Arroz feijao e bife",
    "Terça-feira": "frango frito",
    "Quarta-feira": "peixe",
    "Quinta-feira": "lasanha",
    "Sexta-feira": "feijoada",
    "sábado": "churrasco",
    "domingo": "pizza"
    }

    opcao = input("Digite a opção desejada: ")
   
    if opcao == '1':
    
        print("/modulo04 Estruturas de dados Dicionários \n")

        print('-'*40)

    nome_usuario = input("Digite seu nome para começar:")
    dia_esolhido =input('Que dia é hoje :')


    print("Bem-vindo ao programa de verificação de cardápio! \n")
    dia_escolhido = input("Digite um dia da semana para saber o menu: ").lower().strip()

    if dia_escolhido in cardapio_da_semana:

        comida = cardapio_da_semana[dia_escolhido]
        print(f"No {dia_escolhido}, o prato do dia é: {comida}!")
    else:print(
            f'Desculpe, "{dia_escolhido}" não é um dia válido no nosso cardápio. Tente usar o hífen (ex: segunda-feira).'
        )
    if opcao == '0':
            print("Saindo do sistema...")
            break
