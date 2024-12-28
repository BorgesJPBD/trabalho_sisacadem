import random
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
        if professor['id'] == codigo_professor:
            return professor
    return None

def buscar_alunos(codigos_alunos):
    alunos_encontrados = []
    for codigo in codigos_alunos:
        for aluno in alunos:
            if aluno['matricula'] == codigo:
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

    codigos_alunos = input("Digite os códigos dos alunos separados por vírgula: ").split(',')
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

cadastro_turma()

   
   

    
    
    
    