

# 1. Adicionar contato

def adicionar_contato(agenda_telefonica):
    print('\n--- Adicionando Contato ---')
    nome = input('Nome: ').title()
    contato = {}  

    erro = True
    while erro:
        numero = input('Número: ')
        if validador_numero(numero):
            contato['Número'] = numero 
            erro = False
        else:
            print('\n\U000026A0 O número celular deve conter apenas dígitos.')

    erro = True
    while erro:
        email = input('E-mail: ').lower()
        if validador_email(email):
            contato['E-mail'] = email 
            erro = False
        else:
            print('\n\U000026A0 E-mail inválido!')

    agenda_telefonica[nome] = contato 
    print(f'\n\U00002705 Contato {nome} adicionado com sucesso!')



######


# 2. Alterar contato

def alterar_contato(agenda):
    print('\n--- Alterar Contato ---')  
    print('Qual contato deseja alterar?')
    contato = input('Contato: ').title()

    if contato not in agenda:
        print('\n\U000026A0 Atenção! Contato não encontrado na agenda.')
        return 
    
    contato_atual = agenda[contato]
    novo_nome = input('Nome atualizado: ').title()

    erro = True
    while erro:
        numero = input('Número atualizado: ')
        if validador_numero(numero):
            contato_atual['Número celular'] = numero
            erro = False
        else:
            print('\n\U000026A0 Atenção! O número celular deve conter apenas dígitos.')

    erro = True
    while erro:
        email = input('E-mail atualizado: ').lower()
        if validador_email(email):
            contato_atual['E-mail'] = email  
            erro = False
        else:
            print('\n\U000026A0 Atenção! E-mail inválido!')

    agenda.pop(contato) 
    agenda[novo_nome] = contato_atual  
    
    print(f'\n\U00002705 Contato {novo_nome} atualizado com sucesso!')



######


# 3. Remover contato

def remover_contato(agenda):
    print('\n--- Removendo Contato ---')
    excluir_contato = True

    while excluir_contato:
        print('Qual contato deseja excluir?')
        contato = input('Contato: ').title()

        if contato not in agenda:
            print('\U000026A0 O contato informado não está listado na agenda')
        else:
            decisao = input(f'\nConfirma a exclusão de {contato}?(s/n): ').lower()

            opcoes_validas = {'s', 'n'}

            if decisao in opcoes_validas:
                if decisao == 's':
                    del agenda[contato]
                    print(f'\n\U00002705 Exclusão do contato {contato} realizada com sucesso!')
                else:
                    print('\n\U0000274C Exclusão cancelada!')

            else:
                print('\n\U000026A0 Atenção! O valor inserido não é uma opção válida. Informe uma das opções: (s/n)\n')

        decisao2 = input('\n\U0001F503 Deseja excluir um novo contato?(s/n): ').lower()

        if decisao2 in opcoes_validas:
            if decisao2 == 'n':
                excluir_contato = False


######


# 4. Listar contato

def listar_contato(agenda_telefonica):
    print('\n--- Lista de Contatos ---')

    if len(agenda_telefonica) == 0:
        print('\U0001F622 Agenda vazia!')

    else:
        for numeracao, chave in enumerate(agenda_telefonica.keys(), start=1):
            print(f'\t{numeracao} - {chave}')

        mais_detalhes = input('\n\U0001F50D Deseja ver mais informações sobre um contato? (s/n): ').lower()

        # Validando a entrada
        opcoes_validas = {'s', 'n'}
        while mais_detalhes not in opcoes_validas:
            print('\n\U000026A0 Atenção! O valor inserido não é uma opção válida. Informe uma das opções: (s/n)\n')
            mais_detalhes = input('Deseja ver mais informações sobre um contato? (s/n): ').lower()

        while mais_detalhes == 's':
            contato = input('Informe o contato que deseja visualizar: ').title()

            if contato not in agenda_telefonica:
                print('\n\U000026A0 Atenção! O contato informado não está na sua Agenda. Por favor, informe um contato válido:\n')
                contato = input('Informe o contato que deseja visualizar: ')
            else:
                print(f'\n--- Detalhes do Contato: {contato} ---')
                for chave, valor in agenda_telefonica[contato].items():
                    print(f'\t{chave}: {valor}')
                
            mais_detalhes = input('\n\U0001F503 Deseja ver mais informações sobre outro contato? (s/n): ').lower()

            # Validando a entrada
            while mais_detalhes not in opcoes_validas:
                print('\n\U000026A0 Atenção! O valor inserido não é uma opção válida. Informe uma das opções: (s/n)\n')
                mais_detalhes = input('Deseja ver mais informações sobre um contato? (s/n): ').lower()


######


# 1.1 Validador de infos passadas

def validador_numero(numero):
    return numero.isdigit() 

def validador_email(email):
    return '@' in email and '.' in email.split('@')[-1] 


