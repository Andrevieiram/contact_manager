from contact_manager import *

print('Lista de contatos.')

menu = True

print("1) Adicionar contato.")
print('2) Listar Contatos.')
print('3) Remover contatos')

opção = int(input("Escolha uma opção: "))

if opção == 1:
    nome = input('Nome do contato: ')
    telefone = input('Telefone: ')
    email = input('Email :')
    
    adicionar_contatos(nome,telefone,email)

if opção == 2:
    
    print(Lista_contatos)

if opção == 3:

    nomeC = input("Digite o nome do contato : ")
    remover_contato(nomeC)
