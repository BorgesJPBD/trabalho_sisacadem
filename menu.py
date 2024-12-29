from cadastrar_alunos import cadastro_alunos, visualizar_lista_alunos, excluir_aluno
from cadastrar_professor import cadastro_professor, listar_professores
from cadastrar_disciplina import cadastro_disciplina, listar_disciplinas
from cadastrar_turmas import cadastro_turma, listar_turmas

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
  
    print("Inserir professor em disciplina ainda não implementado.")

def matricular_aluno_em_turma():
    
    print("Matricular aluno em turma ainda não implementado.")

def excluir_professor():
    
    print("Excluir professor ainda não implementado.")

def excluir_disciplina():
    
    print("Excluir disciplina ainda não implementado.")

def excluir_turma():
    print("Excluir turma ainda não implementado.")

def menu():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")
        executar_opcao(opcao)
        
menu()