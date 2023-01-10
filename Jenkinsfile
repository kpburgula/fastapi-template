pipeline{
    agent any
    stages{
        stage('Checkout'){
                steps{
                    git url: 'https://github.com/kpburgula/fastapi-template.git',
                    branch: 'main'
        }
    }
        stage('Unit testing'){
                steps{
                    sh 'uvicorn main:app &'
                    sh 'python3 test_fastapi.py'
                }
            }
        stage('SonarQube Analysis') {
                steps{
                    script{
                        def scannerHome = tool 'SonarScanner';
                        withSonarQubeEnv() {
                        sh "${scannerHome}/bin/sonar-scanner"
                    }
                }
            }
        }
        stage('Build Docker Image'){
            steps{
                sh "docker build . -t kpburgula/fastapi-python-app -f deployment/app_image/Dockerfile"
            }
        }
        stage('Push Docker Image'){
            steps{
                sh "docker push kpburgula/fastapi-python-app"
            }
        }
        stage('Acceptance tests'){
            steps{
                // this is under development
                echo "Acceptance tests"
            }
        }
    }
}
