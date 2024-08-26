# Importações necessárias
import json

# Função para carregar dados de um arquivo JSON
def carregar_dados(arquivo):
    try:
        with open(arquivo, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# Função para salvar dados em um arquivo JSON
def salvar_dados(arquivo, dados):
    with open(arquivo, 'w') as f:
        json.dump(dados, f, indent=4)

# Função para gerar um novo ID
def gerar_novo_id(lista):
    if not lista:
        return 1
    return max(item['ID'] for item in lista) + 1

# Inicializar listas para armazenar dados
estudantes = carregar_dados('estudantes.json')
disciplinas = carregar_dados('disciplinas.json')
professores = carregar_dados('professores.json')
turmas = carregar_dados('turmas.json')
matriculas = carregar_dados('matriculas.json')

# Funções CRUD para cada entidade
def incluir(lista, item):
    item_id = gerar_novo_id(lista)
    item['ID'] = item_id
    lista.append(item)
    print(f'Item com ID {item_id} incluído com sucesso!')

def listar(lista):
    for item in lista:
        print(f"ID: {item['ID']} - Dados: {item}")

def excluir(lista, item_id):
    for i, item in enumerate(lista):
        if item['ID'] == item_id:
            lista.pop(i)
            print(f'Item com ID {item_id} excluído com sucesso!')
            return
    print(f'Item com ID {item_id} não encontrado!')

def alterar(lista, item_id, novo_item):
    for item in lista:
        if item['ID'] == item_id:
            item.update(novo_item)
            print(f'Item com ID {item_id} alterado com sucesso!')
            return
    print(f'Item com ID {item_id} não encontrado!')

# Função para converter a entrada de dados em um dicionário
def converter_para_dicionario(dados_str):
    try:
        item_dict = dict(kv.split('=') for kv in dados_str.split(', '))
        return item_dict
    except ValueError:
        print("Erro: Formato inválido. Use o formato chave=valor, separado por vírgula.")
        return None

# Menu de operações
def submenu(lista, arquivo):
    while True:
        print("\nSubmenu:")
        print("1. Incluir")
        print("2. Listar")
        print("3. Excluir")
        print("4. Alterar")
        print("5. Voltar ao menu principal")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            item_dados = input("Digite os dados do item a ser incluído (ex.: nome=João, idade=20): ")
            item = converter_para_dicionario(item_dados)
            if item:
                incluir(lista, item)
                salvar_dados(arquivo, lista)
        elif opcao == '2':
            listar(lista)
        elif opcao == '3':
            item_id = int(input("Digite o ID do item a ser excluído: "))
            excluir(lista, item_id)
            salvar_dados(arquivo, lista)
        elif opcao == '4':
            item_id = int(input("Digite o ID do item a ser alterado: "))
            novo_item_dados = input("Digite os novos dados do item (ex.: nome=Maria, idade=22): ")
            novo_item = converter_para_dicionario(novo_item_dados)
            if novo_item:
                alterar(lista, item_id, novo_item)
                salvar_dados(arquivo, lista)
        elif opcao == '5':
            break
        else:
            print("Opção inválida!")

# Menu principal
def menu():
    while True:
        print("\nMenu de Opções:")
        print("1. Gerenciar Estudantes")
        print("2. Gerenciar Disciplinas")
        print("3. Gerenciar Professores")
        print("4. Gerenciar Turmas")
        print("5. Gerenciar Matrículas")
        print("6. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            print("Gerenciando Estudantes...")
            submenu(estudantes, 'estudantes.json')
        elif opcao == '2':
            print("Gerenciando Disciplinas...")
            submenu(disciplinas, 'disciplinas.json')
        elif opcao == '3':
            print("Gerenciando Professores...")
            submenu(professores, 'professores.json')
        elif opcao == '4':
            print("Gerenciando Turmas...")
            submenu(turmas, 'turmas.json')
        elif opcao == '5':
            print("Gerenciando Matrículas...")
            submenu(matriculas, 'matriculas.json')
        elif opcao == '6':
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

# Início do programa
menu()
