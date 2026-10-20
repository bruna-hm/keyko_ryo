import alunos
import aulas
import pagamentos
from utils import formatar_decimal

def menu():
    while True:
        print("\nMenu:")
        print("1. Alunos")
        print("2. Aulas")
        print("3. Pagamentos")
        print("4. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            menu_alunos()
        elif escolha == "2":
            menu_aulas()
        elif escolha == "3":
            menu_pagamentos()
        elif escolha == "4":
            break
        else:
            print("Opção inválida. Tente novamente.")

def menu_alunos():
    while True:
        print("\nMenu Alunos:")
        print("1. Listar alunos")
        print("2. Cadastrar aluno")
        print("3. Excluir aluno")
        print("4. Voltar")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            lista_alunos = alunos.listar_alunos()
            for aluno in lista_alunos:
                print(f"ID: {aluno[0]}, Nome: {aluno[1]}, Contato: {aluno[2]}, Ativo: {aluno[3]}")
        elif escolha == "2":
            nome = input("Digite o nome do aluno: ")
            contato = input("Digite o contato do aluno: ")
            novo_aluno = alunos.cadastrar_aluno(nome, contato)
            print(f"Aluno cadastrado com sucesso! ID: {novo_aluno}")
        elif escolha == "3":
            aluno_id = int(input("Digite o ID do aluno a ser excluído: "))
            alunos.excluir_aluno(aluno_id)
        elif escolha == "4":
            break
        else:
            print("Opção inválida. Tente novamente.")
            
def menu_aulas():
    while True:
        print("\nMenu Aulas:")
        print("1. Listar aulas")
        print("2. Cadastrar aula")
        print("3. Excluir aula")
        print("4. Adicionar alunos a uma aula")
        print("5. Voltar")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            lista_aulas = aulas.listar_aulas()
            for aula in lista_aulas:
                print(f"ID: {aula[0]}, Data: {aula[1]}, Assunto: {aula[2]}, Status: {aula[3]}")
        elif escolha == "2":
            data = input("Digite a data da aula (YYYY-MM-DD): ")
            assunto = input("Digite a descrição da aula: ")
            status = input("Digite o status da aula (agendada, realizada, cancelada, remarcada): ")
            nova_aula = aulas.cadastrar_aula(data, assunto, status)
            print(f"Aula cadastrada com sucesso! ID: {nova_aula}")
        elif escolha == "3":
            aula_id = int(input("Digite o ID da aula a ser excluída: "))
            aulas.excluir_aula(aula_id)
        elif escolha == "4":
            aula_id = int(input("Digite o ID da aula: "))
            aluno_id = int(input("Digite o ID do aluno a ser adicionado à aula: "))
            aulas.adicionar_alunos(aula_id, aluno_id)
            print(f"Aluno {aluno_id} adicionado à aula {aula_id} com sucesso!")
        elif escolha == "5":
            break
        else:
            print("Opção inválida. Tente novamente.")

def menu_pagamentos():
    while True:
        print("\nMenu Pagamentos:")
        print("1. Listar pagamentos")
        print("2. Cadastrar pagamento")
        print("3. Excluir pagamento")
        print("4. Voltar")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            lista_pagamentos = pagamentos.listar_pagamentos()
            for pagamento in lista_pagamentos:
                print(f"ID: {pagamento[0]}, Aluno: {pagamento[1]}, Valor: {pagamento[2]}, Data: {pagamento[3]}")
        elif escolha == "2":
            aluno_id = int(input("Digite o ID do aluno: "))
            mes_referencia = input("Digite o mês de referência (YYYY-MM): ")
            try:
                valor = formatar_decimal(input("Digite o valor do pagamento: "))
            except Exception as e:
                print(f"Erro ao formatar valor: {e}")
                continue
            data_pagamento = input("Digite a data do pagamento (YYYY-MM-DD): ")
            status = input("Digite o status do pagamento (pago, pendente): ")   
            novo_pagamento = pagamentos.cadastrar_pagamento(aluno_id, mes_referencia, valor, data_pagamento, status)
            print(f"Pagamento cadastrado com sucesso! ID: {novo_pagamento}")
        elif escolha == "3":
            pagamento_id = int(input("Digite o ID do pagamento a ser excluído: "))
            pagamentos.excluir_pagamento(pagamento_id)
        elif escolha == "4":
            break
        else:
            print("Opção inválida. Tente novamente.")