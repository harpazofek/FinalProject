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
        sh "docker build -t eli41/ping-pong:latest ./app"  
    }

    stage('Push image') {
        withDockerRegistry([ credentialsId: "docker_hub_cred", url: "" ]) {
        sh "docker push eli41/ping-pong:latest"
        }     
    }

    stage('deploy image') {
        withKubeConfig([credentialsId: 'jenkins-kub2',
                    // caCertificate: '<ca-certificate>',                    
                    serverUrl: ' https://192.168.49.2:8443',
                    //contextName: '<context-name>',
                    clusterName: 'minikube',
                    namespace: 'default'
                    ]) {
        sh 'kubectl apply -f ./K8S/ping-pong-deploy.yaml'
        sh 'sleep 15'
      }
    }
    
    stage ('expose to www') { 
        // sh 'kubectl port-forward --address 0.0.0.0 deployment.apps/server-deploy 5005:5005 '
        echo "Minikube port-forward stage - test only"
    }

    stage('K8s checkout') {
      withKubeConfig([credentialsId: 'jenkins-kub2',
                  // caCertificate: '<ca-certificate>',                    
                  serverUrl: ' https://192.168.49.2:8443',
                  //contextName: '<context-name>',
                  clusterName: 'minikube',
                  namespace: 'default'
                  ]) {
        // Checking if minikube is running
        def minikubeStatus = sh(script: 'minikube status --format={{.APIServer}}', returnStatus: true).trim()
        if (minikubeStatus == 'Running') {
          echo "Minikube is running. \nStarting Shutdown Process"
          sh 'minikube stop'
        } 
        else {
          echo "Shutdown Process has ben Compleated minikube is not running"
        }
        }
  }
}
