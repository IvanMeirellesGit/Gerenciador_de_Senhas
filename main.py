from menu import exibir_title, exibir_menu, valida_menu


def main():
    while True:
        exibir_title()
        exibir_menu()
        opcao = input('Escolha uma opção:')
        valida_menu(opcao)


if __name__ == '__main__':
    main()
