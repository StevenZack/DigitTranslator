FROM zigzigcheers/aws-fastapi

WORKDIR /root

ADD tts.py .
ADD .aws .aws

EXPOSE 8080

CMD [ "python3","./tts.py" ]
