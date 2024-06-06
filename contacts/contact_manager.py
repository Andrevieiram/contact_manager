lista_contatos = []

def adicionar_contato(nome,telefone,email):
    contato = {
        "Nome":nome,
        "Telefone":telefone,
        "Email":email
    }
    
    lista_contatos.append(contato)
    return lista_contatos

def listar_contatos():
    todos_os_contatos = ""
    for contato in lista_contatos:
        for chave, valor in contato.items():
            todos_os_contatos += (f"{chave}: {valor}")
            todos_os_contatos += "\n"

    return todos_os_contatos

def remove_contato():
    nome = input("Digite o nome do contato a ser excluido: ")
    for contato in lista_contatos:
        if contato["Nome"] == nome:
            lista_contatos.remove(contato)

            return lista_contatos
        
    print("Contato não encontrado!")
    return lista_contatos

    