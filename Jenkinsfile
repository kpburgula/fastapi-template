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
    }
}
