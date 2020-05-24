from mongoengine import connect

connect(
    'dbNutridata',
    host='mongo',
    port=27017,
    username='root',
    password='example',
    authentication_source='admin')
