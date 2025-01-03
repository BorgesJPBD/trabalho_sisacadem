import random
from tabulate import tabulate
professores = []

def gerar_id_professor():
   
    return random.randint(1000, 9999)

def cadastro_professor():
    nome = input("Digite o nome do professor: ")
    disciplina = input("Digite a disciplina: ")
    data_nascimento = input("Digite a data de nascimento (dd/mm/aaaa): ")
    sexo = input("Digite o sexo (M para Masculino, F para Feminino): ").upper()
    endereco = input("Digite o endereço completo: ")
    telefone = input("Digite o telefone (apenas números com o DDD): ")
    email = input("Digite o email: ")

    id_professor = gerar_id_professor()

    professor = {
        'id': id_professor,
        'nome': nome,
        'disciplina': disciplina,
        'data_nascimento': data_nascimento,
        'sexo': sexo,
        'endereco': endereco,
        'telefone': telefone,
        'email': email
    }

    professores.append(professor)
    print(f"Professor {nome} cadastrado com sucesso! ID: {id_professor}")
    headers = ["Nome", "ID", "Departamento"]
    table = [[professor["nome"], professor["id"], professor["disciplina"]]]
    print(tabulate(table, headers, tablefmt="grid"))

def listar_professores():
    if professores:
        headers = ["Nome", "ID", "Disciplina", "Data de Nascimento", "Sexo", "Endereço", "Telefone", "Email"]
        table = [[professor["nome"], professor["id"], professor["disciplina"], professor["data_nascimento"], professor["sexo"], professor["endereco"], professor["telefone"], professor["email"]] for professor in professores]
        print(tabulate(table, headers, tablefmt="grid"))
    else:
        print("Nenhum professor cadastrado.")
    