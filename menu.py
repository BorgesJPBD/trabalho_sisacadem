import json
from cadastrar_alunos import cadastro_alunos, visualizar_lista_alunos, excluir_aluno, alunos
from cadastrar_professor import cadastro_professor, listar_professores, professores
from cadastrar_disciplina import cadastro_disciplina, listar_disciplinas , disciplinas
from cadastrar_turmas import cadastro_turma, listar_turmas, turmas 
from tabulate import tabulate
import pandas as pd


def carregar_dados(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []

def salvar_dados(nome_arquivo, dados):
    with open(nome_arquivo, 'w') as arquivo:
        json.dump(dados, arquivo, indent=4)
        
        
alunos = carregar_dados('alunos.json')
professores = carregar_dados('professores.json')
disciplinas = carregar_dados('disciplinas.json')
turmas = carregar_dados('turmas.json')      




def exibir_menu():
    print("\nMenu Principal:")
    opcoes = [
        "Cadastrar Aluno",
        "Cadastrar Professor",
        "Cadastrar Disciplina",
        "Cadastrar Turma",
        "Inserir Professor em Disciplina",
        "Listar Professores",
        "Listar Alunos",
        "Listar Disciplinas",
        "Listar Turmas",
        "Matricular Aluno em Turma",
        "Consultar Alunos em Turma",
        "Excluir Aluno",
        "Excluir Professor",
        "Excluir Disciplina",
        "Excluir Turma",
        "Filtrar Professores por Disciplina",  
        "Consultar Professores em Disciplinas",
        "Consultar Disciplinas em Turmas",
        "Sair"
    ]
    headers = ["Opção", "Descrição"]
    table = [[i + 1, opcao] for i, opcao in enumerate(opcoes)]
    print(tabulate(table, headers, tablefmt="grid", maxcolwidths=[10, 30]))

def executar_opcao(opcao):
    acoes = {
        "1": cadastro_alunos,
        "2": cadastro_professor,
        "3": cadastro_disciplina,
        "4": cadastro_turma,
        "5": inserir_professor_em_disciplina,
        "6": listar_professores,
        "7": visualizar_lista_alunos,
        "8": listar_disciplinas,
        "9": listar_turmas,
        "10": matricular_aluno_em_turma,
        "11": consultar_alunos_em_turma,
        "12": excluir_aluno,
        "13": excluir_professor,
        "14": excluir_disciplina,
        "15": excluir_turma,
        "16": filtrar_professores_por_disciplina,
        "17": consultar_professores_em_disciplinas,
        "18": consultar_disciplinas_em_turmas,
        "19": sair
        
    }

    acao = acoes.get(opcao)
    if acao:
        try:
            acao()
        except Exception as e:
            print(f"Erro ao executar a opção: {e}")
    else:
        print("Opção inválida. Tente novamente.")

def sair():
    print("Saindo...")
    salvar_dados('alunos.json', alunos)
    salvar_dados('professores.json', professores)
    salvar_dados('disciplinas.json', disciplinas)
    salvar_dados('turmas.json', turmas)
    exit()

def inserir_professor_em_disciplina():
    
    listar_disciplinas()
    codigo_disciplina = int(input("Digite o código da disciplina: "))
    disciplina = next((d for d in disciplinas if d['código'] == codigo_disciplina), None)
    if not disciplina:
        print("Disciplina não encontrada.")
        return

    listar_professores()
    codigo_professor = int(input("Digite o código do professor: "))
    professor = next((p for p in professores if p['Id'] == codigo_professor), None)
    if not professor:
        print("Professor não encontrado.")
        return

    disciplina['ProfessorDocente'] = professor
    print(f"Professor {professor['Nome']} inserido na disciplina {disciplina['NomeDisciplina']} com sucesso.")
    
    

def matricular_aluno_em_turma():
    
    listar_turmas()
    codigos_turma = int(input("Digite o código da turma: "))
    turma = next((t for t in turmas if t['codigo_turma'] == codigos_turma), None)
    if not turma:
        print("Turma não encontrada.")
        return

    visualizar_lista_alunos()
    codigos_alunos = input("Digite os números de RA dos alunos separados por vírgula: ")
    ra_alunos = [int(ra.strip()) for ra in codigos_alunos.split(",")]

    for ra in ra_alunos:
        aluno = next((a for a in alunos if a['RA'] == ra), None)  
        if not aluno:
            print(f"Aluno com RA {ra} não encontrado.")
            continue

        turma['alunos'].append(aluno)
        print(f"Aluno {aluno['Nome']} matriculado na turma {turma['nome_turma']} com sucesso.")  
        
        

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

def excluir_disciplina():
    
    listar_disciplinas()
    codigo_disciplina = int(input("Digite o código da disciplina a ser excluída: "))
    disciplina_encontrada = False
    for disciplina in disciplinas:
        if disciplina['código'] == codigo_disciplina:
            disciplinas.remove(disciplina)
            disciplina_encontrada = True
            print(f"Disciplina com código {codigo_disciplina} excluída com sucesso.")
            break
    if not disciplina_encontrada:
        print("Disciplina não encontrada.")

def excluir_turma():
    
    listar_turmas()
    codigo_turma = int(input("Digite o código da turma a ser excluída: "))
    turma_encontrada = False
    for turma in turmas:
        if turma['codigo_turma'] == codigo_turma:
            turmas.remove(turma)
            turma_encontrada = True
            print(f"Turma com código {codigo_turma} excluída com sucesso.")
            break
    if not turma_encontrada:
        print("Turma não encontrada.")
    

def excluir_aluno():
    
    visualizar_lista_alunos()
    ra = int(input("Digite o RA do aluno a ser excluído: "))
    aluno_encontrado = False
    for aluno in alunos:
        if aluno['RA'] == ra:
            alunos.remove(aluno)
            aluno_encontrado = True
            print(f"Aluno com RA {ra} excluído com sucesso.")
            break
    if not aluno_encontrado:
        print("Aluno não encontrado.")  
        
def listar_disciplinas():
    if disciplinas:
        headers = ["Nome Disciplina", "Código", "Carga Curricular", "Professor"]  
        table = [[disciplina["NomeDisciplina"], disciplina["código"], disciplina["CargaCurricular"], disciplina["ProfessorDocente"]] for disciplina in disciplinas]  
        print(tabulate(table, headers, tablefmt="grid", maxcolwidths=[20, 10, 15, 20], colalign=("left", "center", "center", "left"))) 
    else:
        print("Nenhuma disciplina cadastrada.")
        
        
def listar_turmas():
    if turmas:
        df = pd.DataFrame([{
            'Código da Turma': turma['codigo_turma'],
            'Nome da Turma': turma['nome_turma'],
            'Disciplina': turma['disciplina']['NomeDisciplina'],
            'Professor': turma['professor']['Nome'],
            'Alunos': ', '.join([aluno['Nome'] for aluno in turma['alunos']])
        } for turma in turmas])
        print(df.to_string(index=False, justify='left'))
    else:
        print("Nenhuma turma cadastrada.")


def filtrar_professores_por_disciplina():
    listar_disciplinas()
    codigo_disciplina = int(input("Digite o código da disciplina para filtrar os professores: "))
    disciplina = next((d for d in disciplinas if d['código'] == codigo_disciplina), None)
    if not disciplina:
        print("Disciplina não encontrada.")
        return

    professor = disciplina.get('ProfessorDocente')
    if professor:
        headers = ["ID", "Nome", "Departamento"]
        table = [[professor["Id"], professor["Nome"], professor["Departamento"]]]
        print(tabulate(table, headers, tablefmt="grid", maxcolwidths=[10, 20, 20]))
    else:
        print("Nenhum professor encontrado para esta disciplina.")
        
def consultar_alunos_em_turma():
    listar_turmas()
    codigo_turma = int(input("Digite o código da turma para consultar os alunos: "))
    turma = next((t for t in turmas if t['codigo_turma'] == codigo_turma), None)
    if not turma:
        print("Turma não encontrada.")
        return

    if turma['alunos']:
        headers = ["RA", "Nome"]
        table = [[aluno["RA"], aluno["Nome"]] for aluno in turma['alunos']]
        print(tabulate(table, headers, tablefmt="grid", maxcolwidths=[10, 20]))
    else:
        print("Nenhum aluno matriculado nesta turma.")    
        
        
def consultar_professores_em_disciplinas():
    listar_disciplinas()
    codigo_disciplina = int(input("Digite o código da disciplina para consultar os professores: "))
    disciplina = next((d for d in disciplinas if d['código'] == codigo_disciplina), None)
    if not disciplina:
        print("Disciplina não encontrada.")
        return

    professor = disciplina.get('ProfessorDocente')
    if professor and isinstance(professor, dict):
        headers = ["ID", "Nome", "Departamento"]
        table = [[professor["Id"], professor["Nome"], professor["Departamento"]]]
        print(tabulate(table, headers, tablefmt="grid", maxcolwidths=[10, 20, 20]))
    else:
        print("Nenhum professor alocado nesta disciplina.")   
        
        
        
def consultar_disciplinas_em_turmas():
    listar_turmas()
    codigo_turma = int(input("Digite o código da turma para consultar as disciplinas: "))
    turma = next((t for t in turmas if t['codigo_turma'] == codigo_turma), None)
    if not turma:
        print("Turma não encontrada.")
        return

    disciplina = turma.get('disciplina')
    if disciplina and isinstance(disciplina, dict):
        headers = ["Código", "Nome", "Carga Curricular"]
        table = [[disciplina["código"], disciplina["NomeDisciplina"], disciplina["CargaCurricular"]]]
        print(tabulate(table, headers, tablefmt="grid", maxcolwidths=[10, 20, 20]))
    else:
        print("Nenhuma disciplina alocada nesta turma.")
 
                 
def menu():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")
        executar_opcao(opcao)
        
if __name__ == "__main__":
        
    menu()