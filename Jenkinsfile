#!/usr/bin/env groovy

pipeline {
    agent { dockerfile true }
    stages {
        stage('Deploy') {
            steps {
                sh "sudo docker push"
            }
        }
    }
}
