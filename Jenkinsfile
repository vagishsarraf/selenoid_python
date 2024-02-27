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
     stage('Installing requirements'){
        steps{
            sh 'pip install -r requirement.txt'
            }
            }
     stage('Testing'){
        sh 'pytest'
     }
     stage('Stop docker containers'){
        steps{
        sh 'docker stop $(docker ps -a -q)'
        }
     }
     }
}