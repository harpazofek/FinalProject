# FinalProject

1 - BUILD A PYTHON FLASK APP WITH A PING-PONG FUNCTION
    A PING PONG FUNCTION IS A GET FUNCTION THAT RECEIVES THE GET
    REQUEST AS A SERVER
    THE BODY OF THIS REQUEST IS A JSON WITH A CONTENT PING
    THE FLAK APP SHROUD RETURNS A 200 RESPONSE WITH A PONG JSON

2 - BUILD AN IMAGE THAT RUNS THE APPLICATION IN PORT 5005

3 - BUILD A CLUSTER IN MINIKUBE TO RUN 4 INSTANCES OF THIS CONTAINER

4 - THE INSTANCE SHOULD BE A DEPLOYMENT WITH A 4 REPLICAS
    USING ANSIBILE BUILD A CRON JOB IN JENKINS TO ADD 2 REPLICAS AT
    8:00 AND DELETE 2 REPLICAS AT 13:00

asuming 
NAME                            READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/server-deploy   4/4     4            4           8m50s

remove 2 replicas  from 4  to 2
kubectl scale --current-replicas=4 --replicas=2 deployment.apps/server-deploy

add 2 replicas from 2 to 4
kubectl scale --current-replicas=2 --replicas=4 deployment.apps/server-deploy

 kubectl describe deployments server-deploy | grep desired | awk '{print $2}' | head -n1

if the number of replicas is unknowen  and you want 6 replicas
run the foloing command 
  kubectl scale --current-replicas=$(kubectl describe deployments server-deploy | grep desired | awk '{print $2}' | head -n1) --replicas=6 deployment.app
s/server-deploy



