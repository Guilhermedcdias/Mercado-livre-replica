from Database.conect import conect


def delete(colletion):
    if (colletion == 'vendedor'):
        vendedor()
    elif (colletion == 'cliente'):
        cliente()
    elif (colletion == 'produto'):
        produto()
    elif (colletion == 'favorito'):
        favorito()
    elif (colletion == 'compra'):
        compra()


def vendedor():
    cpf = input('CPF: ')
    # Inserindo usando a classe do mongo cliente
    mongo = conect()
    # selecionando database mercado livre
    db = mongo['mercado_livre']
    # selecionando a collection vendedor
    collection = db['vendedor']
    # vendo se ja existe pelo cpf
    if (collection.find_one({'cpf': cpf})):
        collection.delete_one({'cpf': cpf})
        print('Vendedor deletado com sucesso!')
    else:
        print('Vendedor não encontrado!')
    # fechando a conexão
    mongo.close()


def cliente():
    cpf = input('CPF: ')
    # Inserindo usando a classe do mongo cliente
    mongo = conect()
    # selecionando database mercado livre
    db = mongo['mercado_livre']
    # selecionando a collection vendedor
    collection = db['cliente']
    # vendo se ja existe pelo cpf
    if (collection.find_one({'cpf': cpf})):
        collection.delete_one({'cpf': cpf})
        print('Cliente deletado com sucesso!')
    else:
        print('Cliente não encontrado!')
    # fechando a conexão
    mongo.close()


def produto():
    mongo = conect()
    db = mongo['mercado_livre']
    collection = db['produto']
    produtos = collection.find()
    for produto in produtos:
        print('ID: ' + str(produto['id']))
        print('Nome: ' + produto['nome'])
        print('Descrição: ' + produto['descricao'])
        print('Preço: ' + str(produto['preco']))
        print('Vendedor: ' + produto['vendedor']['nome'])
        print('-----------------------')
    id = input('ID: ')
    # Inserindo usando a classe do mongo cliente
    if (collection.find_one({'id': int(id)})):
        collection.delete_one({'id': int(id)})
        print('Produto deletado com sucesso!')
    else:
        print('Produto não encontrado!')
    # fechando a conexão
    mongo.close()


def favorito():
    # mostrando clientes
    mongo = conect()
    db = mongo['mercado_livre']
    collection = db['cliente']
    clientes = collection.find()
    for cliente in clientes:
        print('CPF: ' + cliente['cpf'])
        print('Nome: ' + cliente['nome'])
        print('Email: ' + cliente['email'])
        print('Telefone: ' + cliente['telefone'])
        print('-----------------------')
    cpf = input('CPF do cliente: ')
    # verificando se o cliente existe
    if (collection.find_one({'cpf': cpf})):
        # mostrando favoritos do cliente e mandando escolher qual quer excluir
        cliente = collection.find_one({'cpf': cpf})
        for favorito in cliente['favoritos']:
            print('ID: ' + str(favorito['id']))
            print('Nome: ' + favorito['nome'])
            print('Descrição: ' + favorito['descricao'])
            print('Preço: ' + str(favorito['preco']))
            print('Vendedor: ' + favorito['vendedor']['nome'])
            print('-----------------------')
        id = input('ID do produto que deseja excluir: ')
        
        # percorrendo array de favoritos do cliente e pegando indice do objeto com id igual ao digitado
        for i in range(len(cliente['favoritos'])):
            if (cliente['favoritos'][i]['id'] == int(id)):
                # deletando o favorito
                cliente['favoritos'].pop(i)
                # atualizando o cliente
                collection.update_one({'cpf': cpf}, {'$set': cliente})
                print('Favorito deletado com sucesso!')
                break
    else:
        print('Cliente não encontrado!')
    # fechando a conexão
    mongo.close()

    input('Pressione enter para continuar...')

def compra():
    # mostrando clientes
    mongo = conect()
    db = mongo['mercado_livre']
    collection = db['cliente']
    clientes = collection.find()
    for cliente in clientes:
        print('CPF: ' + cliente['cpf'])
        print('Nome: ' + cliente['nome'])
        print('Email: ' + cliente['email'])
        print('Telefone: ' + cliente['telefone'])
        print('-----------------------')
    cpf = input('CPF do cliente: ')
    # verificando se o cliente existe
    if (collection.find_one({'cpf': cpf})):
        # findall na colletion de compra where cpf = cpf
        collection = db['compra']
        compras = collection.find({'cpf': cpf})
        for compra in compras:
            print('ID: ' + str(compra['id']))
            print('Produto: ' + compra['produto']['nome'])
            print('Vendedor: ' + compra['vendedor']['nome'])
            print('-----------------------')
        id = input('ID da compra que deseja excluir: ')

        # delete where id = id

        delete = collection.delete_one({'id': int(id)})

        if (delete.deleted_count > 0):
            print('Compra deletada com sucesso!')
        else:
            print('Compra não encontrada!')

    else:
        print('Cliente não encontrado!')
    # fechando a conexão
    mongo.close()

    input('Pressione enter para continuar...')