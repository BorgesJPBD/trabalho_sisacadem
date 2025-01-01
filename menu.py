from cadastrar_alunos import cadastro_alunos, visualizar_lista_alunos, excluir_aluno, alunos
from cadastrar_professor import cadastro_professor, listar_professores, professores
from cadastrar_disciplina import cadastro_disciplina, listar_disciplinas , disciplinas
from cadastrar_turmas import cadastro_turma, listar_turmas, turmas 

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
        "Excluir Aluno",
        "Excluir Professor",
        "Excluir Disciplina",
        "Excluir Turma",
        "Sair"
    ]
    for i, opcao in enumerate(opcoes, start=1):
        print(f"{i}. {opcao}")

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
        "11": excluir_aluno,
        "12": excluir_professor,
        "13": excluir_disciplina,
        "14": excluir_turma,
        "15": sair
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
    professor = next((p for p in professores if p['id'] == codigo_professor), None)
    if not professor:
        print("Professor não encontrado.")
        return

    disciplina['ProfessorDocente'] = professor
    print(f"Professor {professor['nome']} inserido na disciplina {disciplina['NomeDisciplina']} com sucesso.")
    
    

def matricular_aluno_em_turma():
    
    listar_turmas()
    codigos_turma = int(input("Digite o código da turma: "))
    turma = next((t for t in turmas if t['codigo_turma'] == codigos_turma), None)
    if not turma:
        print("Turma não encontrada.")
        return

    visualizar_lista_alunos()
    codigos_alunos = input("Digite os números de RA dos alunos separados por vírgula:")
    ra_alunos = [int(ra.strip()) for ra in codigos_alunos.split(",")]

    for codigo_aluno in ra_alunos:
        aluno = next((a for a in alunos if a['ra'] == codigo_aluno), None)  
        if not aluno:
            print(f"Aluno com RA {codigo_aluno} não encontrado.")
            continue

    turma['alunos'].append(aluno)
    print(f"Aluno {aluno['nome']} matriculado na turma {turma['nome_turma']} com sucesso.")

def excluir_professor():
    
    listar_professores()
    codigo_professor = int(input("Digite o código do professor a ser excluído: "))
    professor_encontrado = False
    for professor in professores:
        if professor['id'] == codigo_professor:
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
        if aluno['ra'] == ra:
            alunos.remove(aluno)
            aluno_encontrado = True
            print(f"Aluno com RA {ra} excluído com sucesso.")
            break
    if not aluno_encontrado:
        print("Aluno não encontrado.")  

def menu():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")
        executar_opcao(opcao)
        
menu()