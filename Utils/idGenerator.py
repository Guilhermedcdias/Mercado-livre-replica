from Database.conect import conect


def gerarId(colletion):
    mongo = conect()
    db = mongo['mercado_livre']
    collection = db[colletion]

    # seleciona tudo do banco
    cursor = collection.find({})
    # se for null é id = 1
    if (cursor == None):
        id = 1
    else:
        id = 0
        # percorre curso pegando o campo id
        for x in cursor:
            ida = x['id']
            if (ida > id):
                id = ida
        
        id += 1

    # fechando a conexão
    mongo.close()
    return id