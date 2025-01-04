import random
import pandas as pd

alunos = []

def cadastro_alunos():
    Nome = input("Digite o nome do aluno: ")
    RA = gerar_ra()
    Matricula = gerar_num_matricula()
    DataNascimento = input("Digite a data de nascimento (dd/mm/aaaa): ")
    Sexo = input("Digite o sexo (M para Masculino, F para Feminino): ").upper()
    Endereço = input("Digite o endereço completo: ")
    Telefone = input("Digite o telefone (apenas números com o DDD): ")
    Email = input("Digite o email: ")
    
    aluno = {
        "Nome": Nome,
        "RA": RA,
        "Matricula": Matricula,
        "DataNascimento": DataNascimento,
        "Sexo": Sexo,
        "Endereco": Endereço,
        "Telefone": Telefone,
        "Email": Email,
        
    }
    
    alunos.append(aluno)
    df = pd.DataFrame([aluno])
    print(df.to_string(index=False, justify='left'))



def gerar_ra():
    ra = random.randint(10000, 99999)  
    return ra 

def gerar_num_matricula():
    matricula = random.randint(1,9999) 
    return matricula

def visualizar_lista_alunos():
    if alunos:
        df = pd.DataFrame(alunos)
        print(df.to_string(index=False, justify='left'))
    else:
        print("Nenhum aluno cadastrado.")
        
def excluir_aluno():
    ra = int(input("Digite o RA do aluno a ser excluído: "))
    aluno_encontrado = False
    for aluno in alunos:
        if aluno['ra'] == ra:
            alunos.remove(aluno)
            aluno_encontrado = True
            print(f"Aluno com RA {ra} excluído com sucesso.")
            break
    if not aluno_encontrado:
        print("Aluno não encontrado.")        
    












    

