import random
import pandas as pd
from save import carregar_dados, salvar_dados


# Carregar dados dos arquivos pickle
turmas = carregar_dados('turmas.pkl')
disciplinas = carregar_dados('disciplinas.pkl')
professores = carregar_dados('professores.pkl')
alunos = carregar_dados('alunos.pkl')

def buscar_disciplina(codigo_disciplina):
    
    """
    Busca uma disciplina pelo código.
    
    codigo_disciplina (int): Código da disciplina.
    
 Retorna A disciplina encontrada ou None se não encontrada.
    """
    for disciplina in disciplinas:
        if disciplina['código'] == codigo_disciplina:
            return disciplina
    return None

def buscar_professor(codigo_professor):
    """
    Busca um professor pelo código.
    Retorna
    O professor encontrado ou None se não encontrado.
    """
    for professor in professores:
        if professor['Id'] == codigo_professor:
            return professor
    return None

def buscar_alunos(codigos_alunos):
    """
    Busca alunos pelos códigos de RA.
    
    Lista de códigos de RA dos alunos.
    Retorna Lista de alunos encontrados.
    """
    alunos_encontrados = []
    for codigo in codigos_alunos:
        for aluno in alunos:
            if aluno['RA'] == codigo:
                alunos_encontrados.append(aluno)
                break
    return alunos_encontrados

def cadastro_turma():
    """
    Solicita informações da turma ao usuário, gera um código aleatório,
    e salva os dados da turma em um arquivo pickle.
    """
    
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

    salvar_dados('turmas.pkl', turmas)  # Salvar os dados no arquivo pickle
    print(f"Turma {nome_turma} cadastrada com sucesso! Código gerado: {codigo_turma}")
    

def listar_turmas():
    """
    Mostra a lista de turmas cadastradas em formato de tabela.
    Se não tiver nenhuma turma cadastrada, exibe uma mensagem informando que nenhuma turma foi cadastrada.
    """
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
    