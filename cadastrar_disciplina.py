import random  

disciplinas = []  

def listar_disciplinas():
    if disciplinas:
        print("Disciplinas cadastradas:")
        for disciplina in disciplinas: 
            print(f"Nome: {disciplina['Nome_Disciplina']}, Código: {disciplina['código']}")
    else:
        print("Nenhuma disciplina cadastrada.")

def cadastro_disciplina():
    NomeDisciplina = input("Escreva o nome da disciplina: ")
    CargaCurricular = input("Qual a carga curricular dessa disciplina? ")
    professorDocente = input("Nome do Professor responsável pela disciplina: ")

    código = random.randint(1000, 9999)  
    
    disciplina = {
        "NomeDisciplina": NomeDisciplina,
        "código": código,
        "CargaCurricular": CargaCurricular,
        "ProfessorDocente": professorDocente,
    }

    disciplinas.append(disciplina)
    print(f"Disciplina cadastrada com sucesso! Código gerado: {código}")
    print(f"Disciplina cadastrada: {disciplina}")
    
def listar_disciplinas():
    print("Lista de disciplinas cadastradas:")
    for disciplina in disciplinas:
        print(f"Nome: {disciplina['NomeDisciplina']}, Código: {disciplina['código']}, Carga Curricular: {disciplina['CargaCurricular']}, Professor: {disciplina['ProfessorDocente']}")

def menu():
    while True:
        print("\nMenu:")
        print("1. Cadastrar nova disciplina")
        print("2. Listar disciplinas cadastradas")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastro_disciplina()
        elif opcao == "2":
            listar_disciplinas()
        elif opcao == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")
menu()