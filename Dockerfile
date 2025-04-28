# Usar uma imagem base do Python 3.12
FROM python:3.12-slim-bookworm

# Definir o diretório de trabalho no container
WORKDIR /API-PROJETO

# Copiar o arquivo de requisitos para o container
COPY requirements.txt .

# Instalar as dependências do projeto
RUN pip install -r requirements.txt --no-cache-dir

# Copiar o restante do código para o container
COPY . .

# Expor a porta em que a API estará disponível
EXPOSE 8000

# Comando para rodar a aplicação Flask
CMD ["python", "app.py", "--host=0.0.0.0", "--port=8000"]