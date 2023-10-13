FROM python:3.10.13-slim

WORKDIR /app

ADD translator.py .

RUN pip install "uvicorn[standard]" fastapi boto3

EXPOSE 8080

CMD [ "python3","./translator.py" ]
