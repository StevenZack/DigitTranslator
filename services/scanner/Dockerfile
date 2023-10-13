FROM python:3.10.13-slim

WORKDIR /app

ADD scanner.py .
ADD handwriting.keras .
ADD index.html .

RUN pip install "uvicorn[standard]" fastapi tensorflow keras Pillow numpy

EXPOSE 8080
CMD [ "python3","./scanner.py" ]