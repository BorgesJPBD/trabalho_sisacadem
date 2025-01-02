import random  
from tabulate import tabulate

disciplinas = []  

def listar_disciplinas():
    if disciplinas:
        headers = ["Nome Disciplina", "Código Disciplina", "Carga Curricular", "Professor"]  
        table = [[disciplina["NomeDisciplina"], disciplina["código"], disciplina["CargaCurricular"], disciplina["ProfessorDocente"]] for disciplina in disciplinas]  
        print(tabulate(table, headers, tablefmt="grid"))  
    else:
        print("Nenhuma disciplina cadastrada.")

def cadastro_disciplina():
    NomeDisciplina = input("Escreva o nome da disciplina: ")
    CargaCurricular = input("Qual a carga curricular dessa disciplina? ")
    professorDocente = input("Nome do Professor responsável pela disciplina:") 

    código = random.randint(1000, 9999)  
    
    disciplina = {
        "NomeDisciplina": NomeDisciplina,
        "código": código,
        "CargaCurricular": CargaCurricular,
        "ProfessorDocente": professorDocente,
    }

    disciplinas.append(disciplina)
    print(f"Disciplina cadastrada com sucesso! Código gerado: {código}")
    headers = ["Nome Disciplina", "Código Disciplina", "Carga Curricular", "Professor"]
    table = [[disciplina["NomeDisciplina"], disciplina["código"], disciplina["CargaCurricular"], disciplina["ProfessorDocente"]]]
    print(tabulate(table, headers, tablefmt="grid"))
    
    
def listar_disciplinas():
    print("Lista de disciplinas cadastradas:")
    for disciplina in disciplinas:
        print(f"Nome: {disciplina['NomeDisciplina']}, Código: {disciplina['código']}, Carga Curricular: {disciplina['CargaCurricular']}, Professor: {disciplina['ProfessorDocente']}")
        
listar_disciplinas()


