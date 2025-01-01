import random

alunos = []

def cadastro_alunos():
    nome = input("Digite o nome do aluno: ")
    ra = gerar_ra()
    matricula = gerar_num_matricula()
    data_nascimento = input("Digite a data de nascimento (dd/mm/aaaa): ")
    sexo = input("Digite o sexo (M para Masculino, F para Feminino): ").upper()
    endereco = input("Digite o endereço completo: ")
    telefone = input("Digite o telefone (apenas números com o DDD): ")
    email = input("Digite o email: ")
    
    aluno = {
        "nome": nome,
        "ra": ra,
        "matricula": matricula,
        "data_nascimento": data_nascimento,
        "sexo": sexo,
        "endereco": endereco,
        "telefone": telefone,
        "email": email,
        
    }
    
    alunos.append(aluno)
    print(f"Aluno cadastrado com sucesso: {aluno['nome']} - Matrícula: {aluno['matricula']} - RA: {aluno['ra']}")
def gerar_ra():
    ra = random.randint(10000, 99999)  
    return ra 

def gerar_num_matricula():
    matricula = random.randint(1,9999) 
    return matricula

def visualizar_lista_alunos():
    print("Lista de alunos cadastrados:")
    for aluno in alunos:
        print(f"{aluno['nome']} - RA: {aluno['ra']} - Matrícula: {aluno['matricula']}")
        
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
    












    

