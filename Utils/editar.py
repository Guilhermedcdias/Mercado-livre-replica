from Database.conect import conect


def editar(colletion):
    if (colletion == 'vendedor'):
        vendedor()
    elif (colletion == 'cliente'):
        cliente()
    elif (colletion == 'produto'):
        produto()
    

# criando função assincrona em python

def vendedor():
    cpf = input('CPF: ')
    # descobrindo informações que deseja alterar
    print('Se deseja alterar a informação basta digitar a nova informação, caso não deseje alterar basta apertar enter')
    nome = input('Deseja alterar o nome? ')
    email = input('Deseja alterar o email? ')
    telefone = input('Deseja alterar o telefone? ')

    # selecionando o vendedor do banco
    mongo = conect()

    db = mongo['mercado_livre']

    collection = db['vendedor']

    vend_original = collection.find_one({'cpf': cpf})
    if(vend_original == None):
        print('Vendedor não encontrado!')
    else:
        # verificando o que vai ser alterado
        if (nome == ''):
            nome = vend_original['nome']
        if (email == ''):
            email = vend_original['email']
        if (telefone == ''):
            telefone = vend_original['telefone']
        
        
        # gerando objeto do find_one_and_update
        vendedor = {
            'nome': nome,
            'email': email,
            'telefone': telefone
        }

        
        collection.update_one({'cpf': cpf}, {'$set': vendedor})
        mongo.close()
        print('Vendedor alterado com sucesso!')



def cliente():
    cpf = input('CPF: ')
    # selecionando o cliente do banco
    mongo = conect()
    db = mongo['mercado_livre']
    collection = db['cliente']
    cliente_original = collection.find_one({'cpf': cpf})
    if(cliente_original == None):
        print('Cliente não encontrado!')
    else:
        # descobrindo informações que deseja alterar
        print('Se deseja alterar a informação basta digitar a nova informação, caso não deseje alterar basta apertar enter')
        nome = input('Deseja alterar o nome? ')
        email = input('Deseja alterar o email? ')
        telefone = input('Deseja alterar o telefone? ')

        # verificando o que vai ser alterado
        if (nome == ''):
            nome = cliente_original['nome']
        if (email == ''):
            email = cliente_original['email']
        if (telefone == ''):
            telefone = cliente_original['telefone']
        

        # gerando objeto do find_one_and_update
        cliente = {
            'nome': nome,
            'email': email,
            'telefone': telefone
        }

        collection.update_one({'cpf': cpf}, {'$set': cliente})
        mongo.close()
        print('Cliente alterado com sucesso!')

    input('Aperte enter para continuar...')

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
    # descobrindo informações que deseja alterar
    print('Se deseja alterar a informação basta digitar a nova informação, caso não deseje alterar basta apertar enter')
    nome = input('Deseja alterar o nome? ')
    descricao = input('Deseja alterar a descrição? ')
    preco = input('Deseja alterar o preço? ')
    quantidade = input('Deseja alterar a quantidade? ')

    # selecionando o produto do banco
    produto_original = collection.find_one({'id': int(id)})
    if(produto_original == None):
        print('Produto não encontrado!')
    else:
        # verificando o que vai ser alterado
        if (nome == ''):
            nome = produto_original['nome']
        if (descricao == ''):
            descricao = produto_original['descricao']
        if (preco == ''):
            preco = produto_original['preco']
        if (quantidade == ''):
            quantidade = produto_original['quantidade']
        

        # gerando objeto do find_one_and_update
        produto = {
            'nome': nome,
            'descricao': descricao,
            'preco': preco,
            'quantidade': quantidade
        }

        collection.update_one({'id': int(id)}, {'$set': produto})
        mongo.close()
        print('Produto alterado com sucesso!')