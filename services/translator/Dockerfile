FROM zigzigcheers/aws-fastapi

WORKDIR /root

ADD translator.py .
ADD index.html .
ADD .aws .aws

EXPOSE 8080

CMD [ "python3","./translator.py" ]