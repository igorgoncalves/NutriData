from pymongo import MongoClient

cliente = MongoClient('localhost', 27017)
cliente = MongoClient('mongodb://localhost:27017/')

db = cliente['test-database']