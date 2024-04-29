import random
import string
from salvar_senha import salvar_senha


def gerar_senha(tamanho):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return password


def guardar_senha(servico, email, senha):
    salvar_senha(servico, email, senha)
    print('Senha salva com sucesso!')