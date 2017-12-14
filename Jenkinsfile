#!/usr/bin/env groovy

pipeline {
    agent { dockerfile true }
    stages {
        stage('Deploy') {
            steps {
                sh "sudo docker run -it -p 8000:8090"
            }
        }
    }
}
