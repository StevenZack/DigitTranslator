FROM zigzigcheers/keras-fastapi

WORKDIR /root

ADD scanner.py .
ADD handwriting.keras .
ADD index.html .

EXPOSE 8080
CMD [ "python3","./scanner.py" ]