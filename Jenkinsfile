pipeline {
    agent any
    stages {
        stage('build & SonarQube analysis') {
            steps {
                withSonarQubeEnv('My SonarQube Server') {
                    sh 'mvn clean package sonar:sonar'
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