FROM python:3.10.13-alpine

WORKDIR /app

ADD tss.py .

RUN pip install "uvicorn[standard]" fastapi boto3

EXPOSE 8080

CMD [ "python3","./tts.py" ]
