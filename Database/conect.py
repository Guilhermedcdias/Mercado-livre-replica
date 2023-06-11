import pymongo
from urllib.parse import quote_plus
import os
from dotenv import load_dotenv


def conect():
    load_dotenv()
    pswd = os.getenv('PASSWORD')
    us = os.getenv('us')
    username = quote_plus(us)
    password = quote_plus(pswd)
    cluster = 'guilhermedcdias.4woklyl.mongodb.net'
    uri = 'mongodb+srv://' + username + ':' + password + \
        '@' + cluster + '/?retryWrites=true&w=majority'
    client = pymongo.MongoClient(uri)

    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)

    return client
