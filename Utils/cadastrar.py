
from Database.conect import conect
from Utils.idGenerator import gerarId


def cadastrar(colletion):
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
    nome = input('Nome: ')
    email = input('Email: ')
    telefone = input('Telefone: ')

    # montando objeto
    vendedor = {
        'cpf': cpf,
        'nome': nome,
        'email': email,
        'telefone': telefone
    }

    # Inserindo usando a classe do mongo cliente
    mongo = conect()
    # selecionando database mercado livre
    db = mongo['mercado_livre']
    # selecionando a collection vendedor
    collection = db['vendedor']
    # vendo se ja existe pelo cpf
    if (collection.find_one({'cpf': cpf})):
        print('CPF já cadastrado!')
    else:
        # inserindo o objeto
        collection.insert_one(vendedor)
        # fechando a conexão
        mongo.close()
        print('Vendedor cadastrado com sucesso!')


def cliente():
    cpf = input('CPF: ')
    nome = input('Nome: ')
    email = input('Email: ')
    telefone = input('Telefone: ')

    # montando objeto
    cliente = {
        'cpf': cpf,
        'nome': nome,
        'email': email,
        'telefone': telefone,
        'favoritos': []
    }

    # Inserindo usando a classe do mongo cliente
    mongo = conect()
    # selecionando database mercado livre
    db = mongo['mercado_livre']
    # selecionando a collection vendedor
    collection = db['cliente']
    # vendo se ja existe pelo cpf
    if (collection.find_one({'cpf': cpf})):
        print('CPF já cadastrado!')
    else:
        # inserindo o objeto
        collection.insert_one(cliente)
        # fechando a conexão
        mongo.close()
        print('Cliente cadastrado com sucesso!')


def produto():
    # pegando dados do vendedor
    mongo = conect()
    # selecionando database mercado livre
    db = mongo['mercado_livre']
    # selecionando a collection vendedor
    collection = db['vendedor']
    # pegando todos os vendedores
    vendedores = collection.find()
    # mostrando todos os vendedores
    for vendedor in vendedores:
        print('CPF: ' + vendedor['cpf'])
        print('Nome: ' + vendedor['nome'])
        print('Email: ' + vendedor['email'])
        print('Telefone: ' + vendedor['telefone'])
        print('-----------------------')
    
    vend = input('CPF do vendedor que vai vender o produto: ')
    # verificando se o vendedor existe
    if (collection.find_one({'cpf': vend})):
        vendedor = collection.find_one({'cpf': vend})
        nome = input('Nome: ')
        descricao = input('Descrição: ')
        preco = input('Preço: ')
        quantidade = input('Quantidade: ')

        # montando objeto
        produto = {
            'id': gerarId('produto'),
            'nome': nome,
            'descricao': descricao,
            'preco': preco,
            'quantidade': quantidade,
            'vendedor' : vendedor
        }

        # Inserindo usando a classe do mongo cliente
        collection = db['produto']
        # inserindo o objeto
        collection.insert_one(produto)
        # fechando a conexão
        mongo.close()
        print('Produto cadastrado com sucesso!')
    else:
        print('Vendedor não encontrado!')

def favorito():
    # pegando dados do vendedor
    mongo = conect()
    # selecionando database mercado livre
    db = mongo['mercado_livre']
    # selecionando a collection vendedor
    collection = db['cliente']
    # pegando todos os vendedores
    clientes = collection.find()
    # mostrando todos os vendedores
    for cliente in clientes:
        print('CPF: ' + cliente['cpf'])
        print('Nome: ' + cliente['nome'])
        print('Email: ' + cliente['email'])
        print('Telefone: ' + cliente['telefone'])
        print('-----------------------')
    
    cli = input('CPF do cliente que vai favoritar o produto: ')
    # verificando se o vendedor existe
    if (collection.find_one({'cpf': cli})):
        # pegando todos os produtos
        collection = db['produto']
        produtos = collection.find()
        # mostrando todos os produtos
        for produto in produtos:
            print('ID: ' + str(produto['id']))
            print('Nome: ' + produto['nome'])
            print('Descrição: ' + produto['descricao'])
            print('Preço: ' + produto['preco'])
            print('Quantidade: ' + produto['quantidade'])
            print('-----------------------')
        
        prod = input('ID do produto que vai ser favoritado: ')
        # verificando se o produto existe

        if (collection.find_one({'id': int(prod)})):
            produto = collection.find_one({'id': int(prod)})
            # adicionando o produto no objeto de favoritos do cliente
            collection = db['cliente']
            # inserindo o objeto
            collection.update_one({'cpf': cli}, {'$push': {'favoritos': produto}})
            # fechando a conexão
            mongo.close()
            print('Produto favoritado com sucesso!')
        else:
            print('Produto não encontrado!')
    else:
        print('Cliente não encontrado!')
    
    input('Pressione enter para continuar...')


def compra():
    # pegando dados do vendedor
    mongo = conect()
    # selecionando database mercado livre
    db = mongo['mercado_livre']
    # selecionando a collection vendedor
    collection = db['cliente']
    # pegando todos os vendedores
    clientes = collection.find()
    # mostrando todos os vendedores
    for cliente in clientes:
        print('CPF: ' + cliente['cpf'])
        print('Nome: ' + cliente['nome'])
        print('Email: ' + cliente['email'])
        print('Telefone: ' + cliente['telefone'])
        print('-----------------------')
    
    cli = input('CPF do cliente que vai comprar o produto: ')
    # verificando se o vendedor existe
    if (collection.find_one({'cpf': cli})):
        # pegando todos os produtos
        collection = db['produto']
        produtos = collection.find()
        # mostrando todos os produtos
        for produto in produtos:
            print('ID: ' + str(produto['id']))
            print('Nome: ' + produto['nome'])
            print('Descrição: ' + produto['descricao'])
            print('Preço: ' + produto['preco'])
            print('Quantidade: ' + produto['quantidade'])
            print('-----------------------')
        
        prod = input('ID do produto que vai ser comprado: ')
        # verificando se o produto existe

        if (collection.find_one({'id': int(prod)})):
            # pegando o produto
            produto = collection.find_one({'id': int(prod)})
            # pegando o cliente
            collection = db['cliente']
            cliente = collection.find_one({'cpf': cli})
            # pegando o vendedor
            collection = db['vendedor']
            vendedor = collection.find_one({'cpf': produto['vendedor']['cpf']})
            # inserindo compra na colletion compra
            collection = db['compra']
            # montando objeto
            compra = {
                'id': gerarId('compra'),
                'produto': produto,
                'cliente': cliente,
                'vendedor': vendedor
            }

            # inserindo o objeto
            collection.insert_one(compra)
            # fechando a conexão
            mongo.close()
            print('Compra realizada com sucesso!')
        else:
            print('Produto não encontrado!')
    else:
        print('Cliente não encontrado!')
    
    input('Pressione enter para continuar...')