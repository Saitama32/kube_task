# kube_task
Это простое приложение для знакомства с kubenetes с помощью minikube.

Для запуска была использована команда minikube: `minikube start --cpus=2 --memory=2000 --nodes=3 --driver=kvm2`.
После чего необходимо применить манифесты из папки manifests с помощью команд `kubectl apply -f web-deployment.yaml` и `kubectl apply -f web-service.yaml`. Service создавался с помощью NodePort с портом 31111.
Далее можно прописать `kubectl describe service web` чтобы получить внешний адрес для веб приложения.
Если все сделано правильно вы увидете следущее:

![image](https://github.com/user-attachments/assets/ce1c9f83-a4df-4241-8069-ccafee36556e)

Данные докер образа могут быть получены по команде `docker pull saitama700/kube-stress:1.0.0`

