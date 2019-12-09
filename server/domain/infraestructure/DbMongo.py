from mongoengine import connect

connect(
    'dbNutridata',
    host='localhost',
    port=27017,
    username='root',
    password='example',
    authentication_source='admin')
