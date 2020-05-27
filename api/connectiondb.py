
from pymongo import MongoClient

def connection():
    cliente = MongoClient(host='db-mongo', port=27017)
    db = cliente.get_database('data-geo')
    return db

def get_restaurants():
    db = connection()
    documentos = db.get_collection('restaurant').find({},{'name' : 1, "address.coord" : 2}).limit(4000)
    restaurants = []
    for dato in documentos:
        restaurants.append(dato)
    return restaurants
