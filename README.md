# Neoprospecta - Test


Esse código foi desenvolvido pensando na realização do teste a ser apresentado ao Neoprospecta para avaliação do candidato.

Consiste no Download de um arquivo, descompactação e processamento dos dados, exibição no template e manipulação dos mesmos.

Foi utilizado como tecnologia:
Python 3.7
Django 2.2
django-rq 2.0
djangorestframework 3.9.2
redis 3.2.1
docker

A versão web pode ser acessada em:

``` http://nondasjr.pythonanywhere.com ```

Para ambientação do mesmo deve-se

Criar um virtualenv e ativar o ambiente virtual:

```
 virtualenv --python=python3.7 neoprospecta 
 source neoprospecta/bin/activate
```

Instalar as dependencias
``` pip install -r requirements.txt ```

Instalar e configurar o Redis (opcional), mas server pra solicitar o download e processamento das entry pelo django admin.
Se dejear utilizar o redis deve-se antes de solicitar o processamento tem que ativar com o comando:
```
Com o virtualenv ativado:

python manage.py rqworker
```
Em /admin/parameter/entryparameter/
Você pode configurar o paramentro como url e volume de dados desejado, após selecione o parametro desejado e em ação solicite o processamento.

O processamento pode ser gerado também pelo console via comando, o sistema irá considerar os parametros definidos para a url e volume de dados.

```
Com o virtualenv ativado:

python manage.py processentry

```

Ou utilizar o docker-compose na pasta do projeto rode o comando

```
    docker-compose up -d
```

O comando acima irá montar os ambientes
Web, nginx (respondendo na porta 80) e o redis.
