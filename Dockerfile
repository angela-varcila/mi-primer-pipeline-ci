FROM python:3.12-slim
 
WORKDIR /app
 
COPY calculadora.py .
COPY main.py .
 
ENTRYPOINT ["python", "main.py"]