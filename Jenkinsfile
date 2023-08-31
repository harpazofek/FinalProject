node (){
    def version = null; 
    def tag = null;
    def gitCommit = null;
    def hostfix = null;
    def release = null;
    def dockerImage
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
        dockerImage = docker.build("eli41/ping-pong:latest") 
    }
     
    stage('Push image') {
    docker.withRegistry('https://index.docker.io/v1/', 'docker-hub') {
      dockerImage.push()
    }
  }

    stage ('deploy') { 
        // sh "ssh -i ~/.ssh/id_rsa  eli@172.17.0.1 /home/eli/jenkins/restart_all.sh" 
        sh "kubectl apply -f ping-pong-deploy.yaml" 
    }
}