run:
	docker build -t zigzigcheers/private_scanner:v1 .
start:
	docker run -d -p 8080:8080 --name private_scanner zigzigcheers/private_scanner:v1

push:
	docker push zigzigcheers/private_scanner:v1

clean:
	docker stop private_scanner
	docker container prune
	# docker rmi zigzigcheers/private_scanner:v1