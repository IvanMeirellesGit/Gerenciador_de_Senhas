from gerenciar_senha import gerar_senha, guardar_senha
from salvar_senha import carregar_senhas



def exibir_title():
    print('\n-----------------------------')
    print('Gerenciador de Senhas')
    print('-----------------------------')


def exibir_menu():
    print('O que deseja fazer?\n')
    print('1. Gerar Senha')
    print('2. Guardar Senha')
    print('3. Exibir Senhas')
    print('4. Sair')
    print()


def exibir_senhas(filtro=None):
    senhas = carregar_senhas()
    if filtro:
        senhas = [senha for senha in senhas if senha['servico'] == filtro or senha['email'] == filtro]
    if not senhas:
        print('Nenhuma senha encontrada.')
    else:
        print('Senhas Armazenadas:')
        for idx, senha in enumerate(senhas, start=1):
            print(f'{idx}. Serviço: {senha["servico"]}')
            print(f'    Email: {senha["email"]}')
            print(f'    Senha: {senha["senha"]}\n')


def senha_sucesso(senha):
    print('\nSenha Gerada Com Sucesso!')
    print(f'Senha: {senha}')


def valida_menu(opcao):

    if opcao == '1':

        tamanho = int(input('Digite o tamanho da senha: '))
        senha = gerar_senha(tamanho)
        senha_sucesso(senha)

    elif opcao == '2':

        op = int(input('Escolha uma das opções a seguir:\n'
                       '1- Gerar e Guardar Senha Automaticamente\n'
                       '2- Inserir Senha Manualmente\n'))
        if op == 1:
            servico = input('Digite o serviço do qual essa senha pertence: ')
            email = input('Digite o email usado nesse serviço: ')
            tamanho = int(input('Digite o tamanho da senha: '))
            senha = gerar_senha(tamanho)
            guardar_senha(servico, email, senha)
            senha_sucesso(senha)

        elif op == 2:
            servico = input('Digite o serviço do qual essa senha pertence: ')
            email = input('Digite o email usado nesse serviço: ')
            senha = input('Digite sua senha: ')
            guardar_senha(servico, email, senha)
            senha_sucesso(senha)
        else:
            print('Opção Inválida. Escolha uma das opções válidas')

    elif opcao == '3':
        op = int(input('Escolha uma das opções a seguir:\n'
                       '1- Para exibir todas as senhas\n'
                       '2- Para pesquisar por Email ou Serviço\n'))

        if op == 1:
            exibir_senhas()
        if op == 2:
            op = int(input('1. Pesquisar por Email:\n'
                           '2. Pesquisar por Serviço:\n'))
            if op == 1:
                pesquisa = input('Digite o email que deseja pesquisar: ')
                exibir_senhas(pesquisa)
            if op == 2:
                pesquisa = input('Digite o Serviço que deseja pesquisar: ')
                exibir_senhas(pesquisa.capitalize())
            else:
                print('Digite uma opção válida:')

    elif opcao == '4':
        sair()
    else:
        print('Opção Inválida. Porfavor, escolha uma opção valida.')


def sair():
    print('Programa encerrado.')
    exit()
