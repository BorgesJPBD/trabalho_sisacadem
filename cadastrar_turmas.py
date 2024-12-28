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

def gerar_codigo_turma():
    return random.randint(1000, 9999)

def cadastro_turma():
    codigo_turma = gerar_codigo_turma()
    print("Escolha a disciplina para a turma:")
    for disciplina in disciplinas:
        print(f"Código: {disciplina['código']} - {disciplina['Nome_Disciplina']}")
        codigo_disciplina = int(input("Digite o código da disciplina: "))
        print("Disciplina não encontrada.")
        return
    
    print(f"Disciplina selecionada: {disciplina['Nome_Disciplina']} (Código: {disciplina['código']})")