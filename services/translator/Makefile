run:
	cp -r ~/.aws .
	docker build -t zigzigcheers/private_translator:v1 .
	rm -rf .aws
start:
	docker run -d -p 8080:8080 --name private_translator zigzigcheers/private_translator:v1

push:
	docker push zigzigcheers/private_translator:v1

clean:
	docker stop private_translator
	docker container prune
	# docker rmi zigzigcheers/private_translator:v1