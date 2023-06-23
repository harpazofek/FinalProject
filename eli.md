to run the svc : 
minikube service ping-svc

take the ip and port to the next command

curl -X GET -H "Content-Type: application/json" -d '{"ping": "pong"}' http://localhost:5005/ping


local test 
python3 -m flask --app main run


