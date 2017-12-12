#!/usr/bin/env groovy

pipeline {

    agent {
        docker {
            image: python:3.6
            args '-u root'
        }
    }

    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                docker build -t selingungor/deepyou .
            }
        }
        stage('Push') {
            steps {
                echo 'Push...'
                docker push selingungor/deepyou
            }
        }
    }
}
