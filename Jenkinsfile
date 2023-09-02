node (){
    def version = null; 
    def tag = null;
    def gitCommit = null;
    def hostfix = null;
    def release = null;
    def minikubeStatus = 'Running kube';
    def deployStatus = null;
    // stage ('Checkout') {
    //   checkout scm
    //   sh 'env'
    //   gitCommit = sh(returnStdout: true, script: 'git rev-parse --short HEAD').trim()
    //   release = env.BRANCH_NAME ;
    //   version = "${env.BRANCH_NAME}.${env.BUILD_NUMBER}"
    //   tag = "${release}.${env.BUILD_NUMBER}";
    //   latest = "${env.BRANCH_NAME}-latest";

    // }    
    // stage ('Build') { 
    //     sh "docker build -t eli41/ping-pong:latest ./app"  
    // }

    // stage('Push image') {
    //     withDockerRegistry([ credentialsId: "docker_hub_cred", url: "" ]) {
    //     sh "docker push eli41/ping-pong:latest"
    //     }     
    // }

    stage('deploy to minikube') {
      withKubeConfig([credentialsId: 'jenkins-kub2',
                    // caCertificate: '<ca-certificate>',                    
                    serverUrl: ' https://192.168.49.2:8443',
                    //contextName: '<context-name>',
                    clusterName: 'minikube',
                    namespace: 'default'
                    ]) { 
          //  script 
          //  { 
             minikubeStatus = sh(returnStdout: true, script: 'minikube status --format="{{.APIServer}}"').trim() 
             echo "Minikube is running. \n Deploying ping-pong : minikubeStatus = ${minikubeStatus}"  
             if (${minikubeStatus} == 'Running') {
               echo "Minikube is running. \n Deploying ping-pong : minikubeStatus = ${minikubeStatus}"  
               sh 'kubectl apply -f ./K8S/ping-pong-deploy.yaml'
               sh 'sleep 15'
              } 
              else {
                echo "minikube is not running"
              }       
          // } 
      }
    }

    stage ('expose to www') {
      withKubeConfig([credentialsId: 'jenkins-kub2',
                    // caCertificate: '<ca-certificate>',                    
                    serverUrl: ' https://192.168.49.2:8443',
                    //contextName: '<context-name>',
                    clusterName: 'minikube',
                    namespace: 'default'
                    ]) {
        // sh 'kubectl port-forward --address 0.0.0.0 deployment.apps/server-deploy 5005:5005 '
        echo "Minikube port-forward stage - test only"
      } 
    }

    stage('stop minikube') {
      withKubeConfig([credentialsId: 'jenkins-kub2',
                    // caCertificate: '<ca-certificate>',                    
                    serverUrl: ' https://192.168.49.2:8443',
                    //contextName: '<context-name>',
                    clusterName: 'minikube',
                    namespace: 'default'
                  ]) {
        // Checking if minikube is running
        minikubeStatus = sh(returnStdout: true, script: 'minikube status --format={{.APIServer}}')
        if (minikubeStatus == 'Running') {
          echo "Minikube is running. \nStarting Shutdown Process minikubeStatus = " + $minikubeStatus
          sh 'minikube stop'
        } 
        else {
          echo "Shutdown Process has ben Compleated minikube is not running"
        }
    }
  }

}