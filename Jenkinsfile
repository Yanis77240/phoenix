pipeline {
    agent { 
        node {
            label 'docker-tdp-builder'
            }
      }
    triggers {
        pollSCM '0 1 * * *'
      }
    stages {
        stage('clone') {
            steps {
                echo "Cloning..."
                git branch: '5.1-TDP-alliage', url: 'https://github.com/Yanis77240/phoenix'
            }
        }
        stage('Build') {
            steps {
                echo "Building..."
                sh '''
                mvn clean install -DskipTests -Dhbase.profile=2.1
                '''
            }
        }
        stage('Test') {
            steps {
                echo "Testing..."
                sh '''
                mvn clean test -Dhbase.profile=2.1 --fail-never
                '''
            }
        }
        stage("Publish to Nexus Repository Manager") {
            steps {
                echo "Deploy..."
                withCredentials([usernamePassword(credentialsId: '4b87bd68-ad4c-11ed-afa1-0242ac120002', passwordVariable: 'pass', usernameVariable: 'user')]) {
                    sh 'mvn clean deploy -DskipTests -Dhbase.profile=2.1 -s settings.xml'
                }
            }        
        }
    }
}