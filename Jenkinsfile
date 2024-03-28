pipeline {
    agent any
    stages {
        stage('build & SonarQube analysis') {
            steps {
                withSonarQubeEnv('sonar') {
                    sh 'sonar-scanner'
                }
            }
        }
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