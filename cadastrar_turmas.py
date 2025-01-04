import random
import pandas as pd
from cadastrar_alunos import alunos 
from cadastrar_professor import professores 
from cadastrar_disciplina import disciplinas  

turmas = []

def buscar_disciplina(codigo_disciplina):
    for disciplina in disciplinas:
        if disciplina['código'] == codigo_disciplina:
            return disciplina
    return None

def buscar_professor(codigo_professor):
    for professor in professores:
        if professor['Id'] == codigo_professor:
            return professor
    return None

def buscar_alunos(codigos_alunos):
    alunos_encontrados = []
    for codigo in codigos_alunos:
        for aluno in alunos:
            if aluno['RA'] == codigo:
                alunos_encontrados.append(aluno)
                break
    return alunos_encontrados

def cadastro_turma():
    nome_turma = input("Digite o nome da turma: ")
    codigo_disciplina = int(input("Digite o código da disciplina: "))
    disciplina = buscar_disciplina(codigo_disciplina)
    if not disciplina:
        print("Disciplina não encontrada.")
        return
    
    codigo_professor = int(input("Digite o código do professor: "))
    professor = buscar_professor(codigo_professor)
    if not professor:
        print("Professor não encontrado.")
        return
    
    codigos_alunos = input("Digite o numero de RA de cada aluno separados por virgula: ").split(',')
    codigos_alunos = [int(codigo.strip()) for codigo in codigos_alunos]
    alunos_turma = buscar_alunos(codigos_alunos)
    if len(alunos_turma) != len(codigos_alunos):
        print("Um ou mais alunos não foram encontrados.")
        return
    
    codigo_turma = random.randint(1000, 9999)
    turma = {
        'codigo_turma': codigo_turma,
        'nome_turma': nome_turma,
        'disciplina': disciplina,
        'professor': professor,
        'alunos': alunos_turma
    }

    turmas.append(turma)
    print(f"Turma cadastrada com sucesso! Código da turma: {codigo_turma}")
    df = pd.DataFrame([{
        'Código da Turma': turma['codigo_turma'],
        'Nome da Turma': turma['nome_turma'],
        'Disciplina': turma['disciplina']['NomeDisciplina'],
        'Professor': turma['professor']['Nome'],
        'Alunos': ', '.join([aluno['Nome'] for aluno in turma['alunos']])
    }])
    print(df.to_string(index=False, justify='left'))

def listar_turmas():
    if turmas:
        df = pd.DataFrame([{
            'Código da Turma': turma['codigo_turma'],
            'Nome da Turma': turma['nome_turma'],
            'Disciplina': turma['disciplina']['NomeDisciplina'],
            'Professor': turma['professor']['Nome'],
            'Alunos': ', '.join([aluno['nome'] for aluno in turma['alunos']])
        } for turma in turmas])
        print(df.to_string(index=False, justify='left'))
    else:
        print("Nenhuma turma cadastrada.")
    