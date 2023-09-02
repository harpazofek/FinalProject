node (){
    def version = null; 
    def tag = null;
    def gitCommit = null;
    def hostfix = null;
    def release = null;
    def minikubeStatus = 'floppp';
    def deployStatus = 'big bose is falupen';
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

    stage('deploy to minikube') {
      withKubeConfig([credentialsId: 'jenkins-kub2',
                    // caCertificate: '<ca-certificate>',                    
                    serverUrl: ' https://192.168.49.2:8443',
                    //contextName: '<context-name>',
                    clusterName: 'minikube',
                    namespace: 'default'
                    ]) { 
              minikubeStatus = sh(returnStdout: true, script: 'kubectl get node -n minikube -o name').trim() 
             if (minikubeStatus == "node/minikube") {
               echo "* Minikube is running.  minikub node is = $minikubeStatus *"
               echo "\n **** Deploying ping-pong ******"  
               sh 'kubectl apply -f ./K8S/ping-pong-deploy.yaml,./K8S/ping-service.yml'
               sh 'sleep 20'
              } 
              else {
                echo "minikube is not running , minikubeStatus = $minikubeStatus"
              }       
      }
    }

    // stage ('expose to www') {
    //   withKubeConfig([credentialsId: 'jenkins-kub2',
    //                 // caCertificate: '<ca-certificate>',                    
    //                 serverUrl: ' https://192.168.49.2:8443',
    //                 //contextName: '<context-name>',
    //                 clusterName: 'minikube',
    //                 namespace: 'default'
    //                 ]) {
    //           deployStatus = sh(returnStdout: true, script: ' kubectl get deploy server-deploy -o name').trim() 
    //          if (deployStatus == "deployment.apps/server-deploy") {
    //            echo  "* ping-pong is Deployed - deploy is = $deployStatus *"
    //            echo " *****  Minikube enable service  ***** "  
    //           //  sh 'kubectl port-forward --address 0.0.0.0 deployment.apps/server-deploy 5005:5005 '

    //           } 
    //           else {
    //             echo " !!!! ping-pong is NOT Deployed !!!, deployment is  = $deployStatus"
    //           }       
    //   } 
    // }

  //   stage('stop minikube') {
  //     withKubeConfig([credentialsId: 'jenkins-kub2',
  //                   // caCertificate: '<ca-certificate>',                    
  //                   serverUrl: ' https://192.168.49.2:8443',
  //                   //contextName: '<context-name>',
  //                   clusterName: 'minikube',
  //                   namespace: 'default'
  //                 ]) {
  //       // Checking if minikube is running
  //       minikubeStatus = sh(returnStdout: true, script: 'kubectl get node -n minikube -o name').trim() 
  //       if (minikubeStatus == "node/minikube") {
  //         echo "Minikube is running. \nStarting Shutdown Process minikubeStatus = " + $minikubeStatus
  //         sh 'minikube stop'
  //       } 
  //       else {
  //         echo "Shutdown Process has ben Compleated minikube is not running"
  //       }
  //   }
  // }

}