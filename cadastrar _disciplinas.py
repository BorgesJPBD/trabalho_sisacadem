import random
from cadastrar_professor import professores

disciplinas = [] 

def listar_professores():
    if not professores:
        print("Nenhum professor cadastrado no momento.")
        return
    print("Professores Cadastrados:")
    
    for prof in professores:
        print(f"{prof['id']} - {prof['nome']} - {prof['disciplina']}")
    print()

def cadastro_disciplinas ():
    nome = input("Digite o Nome da Disciplina")
    código_disciplina = random.randint(1000, 9999)
    