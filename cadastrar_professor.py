import random
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
    print(f"Professor {nome} cadastrado com sucesso!")

def listar_professores():
    print("Lista de professores cadastrados:")
    for professor in professores:
        print(f"ID: {professor['id']}, Nome: {professor['nome']}, Disciplina: {professor['disciplina']}, Data de Nascimento: {professor['data_nascimento']}, Sexo: {professor['sexo']}, Endereço: {professor['endereco']}, Telefone: {professor['telefone']}, Email: {professor['email']}")

    
    