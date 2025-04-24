FROM python:3.12-slim-bookworm
# Serve como se fosse uma pasta virtual para o DOCKER copiar o projeto

WORKDIR /API-PROJETO
#Serve para baixar todas os pacotes e dependencias que o projeto precisa que fica dentro do arquivo Requeriments
COPY requeriments.txt .
RUN pip install -r requeriments.txt --no-cache-dir
#Serve para "copiar" o restante do projeto para o conteiner
COPY . .
#Serve para passar em qual porta a api vai estar disponivel
EXPOSE 8000
#É o passo final, tem como objetivo passar para o conteiner o que tem que ser executado
["python", "app-py", "--host-0.0.0.0*. --port-8000]