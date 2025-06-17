#Gerenciador de Lista de Compras
#Objetivo: Criar um sistema interativo para gerenciar itens de compras.
#Funcionalidades:

#Adicionar item (evitar duplicatas).

#Remover item (verificar existência).

#Exibir lista atual.

#Sair do programa.
#Observação: O menu deve ser exibido em loop até que o usuário escolha sair.

def lista_compras():
    lista = set() #set para evitar duplicatas
    while True:
        print("\nMenu: 1-Adicionar 2-Remover 3-Exibir 4-Sair")
        op = input("Escolha: ")
        if op == '1':
            item = input("Item a adicionar: ")
            lista.add(item) #add adiciona o item
            print("Item adicionado.")
        elif op == '2':
            item = input("Item a remover: ")
            lista.discard(item) #discard para evitar erros
            print("Item removido.")
        elif op == '3':
            print("Lista de compras:", lista)
        elif op == '4':
            print("Saindo.")
            break







lista_compras()