pipeline {
    agent {
        label 'jenkins-python-agent'
    }
    stages {
        stage('Python build of file') {
            steps {
                //Ya lo clona el pipeline
                sh 'CLONADO'
                // Ejecuta el archivo hola-mundo.py
                sh 'python3 hola-mundo.py'
            }
        }
    }
}
