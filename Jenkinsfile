pipeline {
    agent any
     stages {
        stage('Prepare Selenoid') {
            steps {
                sh 'docker-compose up -d'
        }
     }
     stage('Verifying Grid') {
                 steps {
                     sh 'curl http://localhost:8083/#/'
                     }
             }
     stage('Stop docker containers'){
     steps{
     sh 'docker stop $(docker ps -a -q)'
     }
     }
          }
}