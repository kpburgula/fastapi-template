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
                    bash "run_install.sh"
                    bash "run_start.sh"
                    bash "run_tests.sh"
                }
            }
    }
}