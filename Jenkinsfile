pipeline {
    agent any
    stages {
        stage('SCM Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/siddhantgawai20/pythonflask.git'
            }
        }
        
        stage ('Docker Image Build') {
            steps {
                sh '/usr/bin/docker image build -t siddhantgawai/newflask .'
            }
        }
        
        stage ('Docker Login') {
            steps {
                sh 'echo dckr_pat_csIQEZRCSBdwthLcZ3SCaQfdmB8 | /usr/bin/docker login -u siddhantgawai --password-stdin'
            }
        }
        
        stage ('Docker Image Push') {
            steps {
                sh '/usr/bin/docker image push siddhantgawai/newflask'
            }
        }
        
        stage ('Confirmation') {
            steps {
                input 'Are You Sure You Want Continue the Deployment ?'
            }
        }
        
        stage('Service Remove') {
            steps {
                sh '/usr/bin/docker service rm service1'
            }
        }
        
        stage('Service Create') {
            steps {
                sh '/usr/bin/docker service create --name service1 -p 4000:4000 siddhantgawai/newflask'
            }
        }
    }
}
