import random
import pandas as pd 
from save import carregar_dados, salvar_dados


professores = carregar_dados('professores.pkl')

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
    salvar_dados('professores.pkl', professores)
    print(f"Professor {Nome} cadastrado com sucesso!")

def listar_professores():
    if professores:
        df = pd.DataFrame(professores)
        print(df.to_string(index=False))
    else:
        print("Nenhum professor cadastrado.")
        
            
def excluir_professor():
    listar_professores()
    codigo_professor = int(input("Digite o código do professor a ser excluído: "))
    professor_encontrado = False
    for professor in professores:
        if professor['Id'] == codigo_professor:
            professores.remove(professor)
            professor_encontrado = True
            print(f"Professor com código {codigo_professor} excluído com sucesso.")
            break
        
        
    if not professor_encontrado:
        print("Professor não encontrado.")
    salvar_dados('professores.pkl', professores)
    