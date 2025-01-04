import random
import pandas as pd 
professores = []

def gerar_id_professor():
   
    return random.randint(1000, 9999)

def cadastro_professor():
    Nome = input("Digite o nome do professor: ")
    Disciplina = input("Digite a disciplina: ")
    DataNascimento = input("Digite a data de nascimento (dd/mm/aaaa): ")
    Sexo = input("Digite o sexo (M para Masculino, F para Feminino): ").upper()
    Endereço = input("Digite o endereço completo: ")
    Telefone = input("Digite o telefone (apenas números com o DDD): ")
    Email = input("Digite o email: ")

    id_professor = gerar_id_professor()

    professor = {
        'Id': id_professor,
        'Nome': Nome,
        'Disciplina': Disciplina,
        'DataNascimento': DataNascimento,
        'Sexo': Sexo,
        'Endereço': Endereço,
        'Telefone': Telefone,
        'Email': Email
    }

    professores.append(professor)
    df = pd.DataFrame([professor])
    print(df.to_string(index=False, justify='left'))

def listar_professores():
    if professores:
        df = pd.DataFrame(professores)
        print(df.to_string(index=False, justify='left'))
    else:
        print("Nenhum professor cadastrado.")
    