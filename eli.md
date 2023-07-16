to run the svc : 
minikube service ping-svc

take the ip and port to the next command

curl -X GET -H "Content-Type: application/json" -d '{"ping": "pong"}' http://localhost:5005/ping


local test 
python3 -m flask --app main run


##### Enable the Ingress controller  ###
minikube addons enable ingress
#### Verify that the NGINX Ingress controller is running
kubectl get pods -n ingress-nginx


##### How to change the default nodeport range
minikube start --extra-config=apiserver.service-node-port-range=5000-32000