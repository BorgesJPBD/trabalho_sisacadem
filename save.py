import pickle

def carregar_dados(nome_arquivo):
    try:
        with open(nome_arquivo, 'rb') as arquivo:
            return pickle.load(arquivo)
    except FileNotFoundError:
        return []

def salvar_dados(nome_arquivo, dados):
    with open(nome_arquivo, 'wb') as arquivo:
        pickle.dump(dados, arquivo)