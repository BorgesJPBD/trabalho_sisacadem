
import random  
disciplinas = []  

def listar_disciplinas():
    if not disciplinas:
        print("Nenhuma disciplina cadastrada.")
    else:
        print("Disciplinas cadastradas:")
        for disciplina in disciplinas:
            print(f"Nome: {disciplina['Nome_Disciplina']}, Código: {disciplina['código']}")

def cadastro_disciplina():
    Nome_Disciplina = input("Escreva o nome da disciplina: ")
    carga_curricular = input("Qual a carga curricular dessa disciplina? ")
    professor_docente = input("Nome do Professor responsável pela disciplina: ")

    código = random.randint(1000, 9999)  
    
    disciplina = {
        "Nome_Disciplina": Nome_Disciplina,
        "código": código,
        "carga_curricular": carga_curricular,
        "professor_docente": professor_docente,
    }

    disciplinas.append(disciplina)
    print(f"Disciplina cadastrada com sucesso! Código gerado: {código}")
    print(f"Disciplina cadastrada: {disciplina}")

print("1. Cadastrar nova disciplina")
print("2. Listar disciplinas cadastradas")
opcao = input("Escolha uma opção: ")

if opcao == "1":
    cadastro_disciplina()
elif opcao == "2":
    listar_disciplinas()
else:
    print("Opção inválida.")