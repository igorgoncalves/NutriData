# NutriData

Projeto do obesevatorio e segurança alimentar de Sergipe

## Preparação do client e pasta dist (/client)

Utilize os comandos na pasta client para gerar os arquivos estáticos do front-end, se você já possuir uma pasta dist/, pule essa etapa

    - npm install
    - npm run build

## Passos para execução do projeto (/server)

No seu terminal utilizando a o pip do Python na versao 3 (alguns sistemas pedem o comando pip3)

- pip install -r requeriments.txt

- python run.py initdb  # inicia base e o documento padrão de localidades

- python run.py runserver # executa aplicação


## Planilhas de teste

No diretorio "planilhas_de_teste/" estão exemplos de planilhas para criação dos macroindicadores

## Base de dados pre-carregada
Na pasta data, existe um snapshot do banco de dados, para restaurar, use as ferramentas do mongo-tools

 - mongorestore --verbose data/backup/dbNutridata