#!/usr/bin/env groovy

pipeline {
    agent { dockerfile true }
    stages {
        stage('Deploy') {
            steps {
                sh "sudo $(which node) docker run -it -p 8000:8000"
            }
        }
    }
}
