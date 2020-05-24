from mongoengine import connect

connect(
    'dbNutridata',
    host='172.24.0.3',
    port=27017,
    username='root',
    password='example',
    authentication_source='admin')
