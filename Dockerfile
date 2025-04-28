# Dockerfile corrigido
FROM python:3.12-slim-bookworm

WORKDIR /API-PROJETO

COPY requirements.txt .
RUN pip install -r requirements.txt --no-cache-dir

COPY . .

EXPOSE 8000

CMD ["python", "app.py"]