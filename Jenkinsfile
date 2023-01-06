pipeline{
    agent any
    stages('Checkout'){
        steps{
            git url: 'https://github.com/kpburgula/fastapi-template.git',
            branch: 'main'
        }
    }
    stages('Unit testing'){
        steps{
            bash "run_install.sh"
            bash "run_start.sh"
            bash "run_tests.sh"
        }
    }
}