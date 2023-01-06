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
                    
                    sh "./run_install.sh"
                    sh "./run_start.sh"
                    sh "./run_tests.sh"
                }
            }
    }
}
