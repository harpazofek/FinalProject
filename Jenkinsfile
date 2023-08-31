node (){
    def version = null; 
    def tag = null;
    def gitCommit = null;
    def hostfix = null;
    def release = null;
    stage ('Checkout') {
      checkout scm
      sh 'env'
      gitCommit = sh(returnStdout: true, script: 'git rev-parse --short HEAD').trim()
      release = env.BRANCH_NAME ;
      version = "${env.BRANCH_NAME}.${env.BUILD_NUMBER}"
      tag = "${release}.${env.BUILD_NUMBER}";
      latest = "${env.BRANCH_NAME}-latest";

    }

    stage ('Build') { 
        sh "docker build  -t eli41/ping-pong:latest ."  
    }

 stage('Push image') {
        withDockerRegistry([ credentialsId: "docker_hub_cred", url: "" ]) {
        sh "docker push eli41/ping-pong:latest"
        }     
    }

 stage('List pods') {
    withKubeConfig([credentialsId: 'jenkins-kub2',
                    // caCertificate: '<ca-certificate>',                    
                    serverUrl: ' https://192.168.49.2:8443',
                    //contextName: '<context-name>',
                    clusterName: 'minikube',
                    namespace: 'default'
                    ]) {
      sh 'kubectl apply -f ping-pong-deploy.yaml'
    //   sh 'kubectl apply -f ping-service.yml'
      sh 'sleep 15'
      sh 'kubectl port-forward --address 0.0.0.0 deployment.apps/server-deploy 5005:5005 '
    }
  }




    // stage ('deploy') { 
    //     // sh "ssh -i ~/.ssh/id_rsa  eli@172.17.0.1 /home/eli/jenkins/restart_all.sh" 
    //     sh "kubectl apply -f ping-pong-deploy.yaml" 
    // }
}