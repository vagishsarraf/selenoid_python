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
        stage('Sonar Analysis') {
            steps {
                sh 'sonar-scanner'
            }
        }
        stage(' Code Setup') {
            steps {
                sh 'sh execute.sh'
            }
        }
        stage('Stop docker containers') {
            steps {
                sh 'docker-compose down'
            }
        }
    }
}