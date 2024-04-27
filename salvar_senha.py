import json


def manipular_arquivo_json(arquivo_json, default=[]):
    try:
        with open(arquivo_json, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {'senhas': default}
    return data.get('senhas', default)


def salvar_senha(servico, email, senha, arquivo_json='passwords.json'):
    senhas = manipular_arquivo_json(arquivo_json)
    senhas.append({'servico': servico, 'email': email, 'senha': senha})
    with open(arquivo_json, 'w') as file:
        json.dump({'senhas': senhas}, file, indent=4)


def carregar_senhas(arquivo_json='passwords.json'):
    return manipular_arquivo_json(arquivo_json)
