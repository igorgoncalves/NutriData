from mongoengine import connect

connect('dbNutridata', host='172.21.0.2', port=27017, username='root', password='example', authentication_source='admin')