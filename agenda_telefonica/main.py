from funcs import adicionar_contato
from funcs import alterar_contato
from funcs import remover_contato
from funcs import listar_contato

banner = '''
    ================================
        \U0001F4DE Bem-vindo à Agenda \U0001F4DE
    ================================
    '''
print(banner)
print('Aqui você pode gerenciar seus contatos.')
print('Adicione, remova, altere ou visualize suas informações.')
print('Vamos começar a organizar sua lista de contatos!\n')

agenda_telefonica = {}

while True:

    # 1. MENU - input para o usuário decidir a ação / validador se o input é uma opção válida --> opções validas = [1, 2, 3, 4]
    def menu():
        print('\n\t1. Adicionar contato')
        print('\t2. Alterar contato')
        print('\t3. Remover contato')
        print('\t4. Listar contatos')
        print('\t5. Sair')

        global action
        action = input('\nInforme o número da ação desejada.\nAção: ')

        if action.isdigit():
            action = int(action)
            
            if action not in [1, 2, 3, 4, 5]:
                print('\n\U000026A0 Atenção!\nO valor inserido não consta como opção.\nInforme um dos números informados.\n')
                menu()

        elif not action.isdigit():
            print('\n\U000026A0 Atenção!\nO valor inserido não consta como opção.\nInforme um dos números informados.\n')
            menu()

        else:
            return action

    menu()

    if action == 1:
        adicionar_contato(agenda_telefonica)

    if action == 2:
        alterar_contato(agenda_telefonica)

    if action == 3:
        remover_contato(agenda_telefonica)
        
    if action == 4:
        listar_contato(agenda_telefonica)
        
    if action == 5:
        print('\n\U0001F44B Obrigado por usar a agenda! Até logo!')
        print('Saindo...')
        break


