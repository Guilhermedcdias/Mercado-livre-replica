from Database.conect import conect


def read(colletion):
    if(colletion == 'vendedor'):
        vendedor()
    elif(colletion == 'cliente'):
        cliente()
    elif(colletion == 'produto'):
        produto()
    elif(colletion == 'favorito'):
        favoritos()

def vendedor():
    print("Para ver um vendedor em especifico digite o cpf, se não basta apertar enter")
    cpf = input('CPF: ')
    # se o cpf for vazio ele vai mostrar todos os vendedores
    if(cpf == ''):
        # selecionando o vendedor do banco
        mongo = conect()

        db = mongo['mercado_livre']

        collection = db['vendedor']

        vendedores = collection.find()
        for vendedor in vendedores:
            print('CPF: ' + vendedor['cpf'])
            print('Nome: ' + vendedor['nome'])
            print('Email: ' + vendedor['email'])
            print('Telefone: ' + vendedor['telefone'])
            print('-----------------------')
        mongo.close()
    else:
        # selecionando o vendedor do banco
        mongo = conect()

        db = mongo['mercado_livre']

        collection = db['vendedor']

        vendedor = collection.find_one({'cpf': cpf})
        if(vendedor == None):
            print('Vendedor não encontrado!')
        else:
            print('CPF: ' + vendedor['cpf'])
            print('Nome: ' + vendedor['nome'])
            print('Email: ' + vendedor['email'])
            print('Telefone: ' + vendedor['telefone'])
        mongo.close()

    input('Aperte enter para continuar...')

def cliente():
    print("Para ver um cliente em especifico digite o cpf, se não basta apertar enter")
    cpf = input('CPF: ')
    # se o cpf for vazio ele vai mostrar todos os clientes
    if(cpf == ''):
        # selecionando o cliente do banco
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
        mongo.close()
    else:
        # selecionando o cliente do banco
        mongo = conect()
        db = mongo['mercado_livre']
        collection = db['cliente']
        cliente = collection.find_one({'cpf': cpf})
        if(cliente == None):
            print('Cliente não encontrado!')
        else:
            print('CPF: ' + cliente['cpf'])
            print('Nome: ' + cliente['nome'])
            print('Email: ' + cliente['email'])
            print('Telefone: ' + cliente['telefone'])
        mongo.close()

    input('Aperte enter para continuar...')


def produto():
    print("Para ver um produto em especifico digite o id, se não basta apertar enter")
    id = input('ID: ')
    # se o id for vazio ele vai mostrar todos os produtos
    if(id == ''):
        # selecionando o produto do banco
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
        mongo.close()
    else:
        # selecionando o produto do banco
        mongo = conect()
        db = mongo['mercado_livre']
        collection = db['produto']
        produto = collection.find_one({'id': int(id)})
        if(produto == None):
            print('Produto não encontrado!')
        else:
            print('ID: ' + str(produto['id']))
            print('Nome: ' + produto['nome'])
            print('Descrição: ' + produto['descricao'])
            print('Preço: ' + str(produto['preco']))
            print('Vendedor: ' + produto['vendedor']['nome'])
        mongo.close()

    input('Aperte enter para continuar...')


def favoritos():
    print("Para ver os favoritos de um cliente em especifico digite o cpf, se não basta apertar enter")
    cpf = input('CPF: ')
    # se o cpf for vazio ele vai mostrar todos os favoritos
    if(cpf == ''):
        # cliente não encontrado
        print('Cliente não encontrado!')
    else:
        # selecionando o favorito do banco
        mongo = conect()
        db = mongo['mercado_livre']
        collection = db['cliente']
        favoritos = collection.find_one({'cpf': cpf})
        if(favoritos == None):
            print('cliente não encontrado!')
        else:
            for favorito in favoritos['favoritos']:
                print('ID: ' + str(favorito['id']))
                print('Nome: ' + favorito['nome'])
                print('Descrição: ' + favorito['descricao'])
                print('Preço: ' + str(favorito['preco']))
                print('Vendedor: ' + favorito['vendedor']['nome'])
                print('-----------------------')
        mongo.close()

    input('Aperte enter para continuar...') 