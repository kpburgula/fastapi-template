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
                    sh 'python3 testing/unit_tests/test_fastapi.py'
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
        stage('Build Docker Image or Packaging Phase'){
            steps{
                // This is Build phase
                // sh "docker build . -t kpburgula/fastapi-python-app -f deployment/app_image/Dockerfile"
                echo 'This is Build/Packaging phase[Under development]'
            }
        }
        stage('Pushing artifact to Docker hub/Nexus repo'){
            steps{
                // Pushing the artifact to docker registry or any artifact repository
                // sh "docker push kpburgula/fastapi-python-app"
                echo 'Pushing the artifact to docker hub/Nexus repo [Under development]'
            }
        }
        stage('QA or Staging deployment'){
            steps{
                // Deploying the image and starting the container in the QA or Staging environment
                echo 'This is Staging deployment [Under development]'
            }
        }
        stage('Acceptance tests'){
            steps{
                // Running the acceptance tests
                echo "Acceptance tests using BDD framework like cucumber or behave [Under development]"

            }
        }
    }
}
