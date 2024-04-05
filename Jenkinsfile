pipeline {
    agent {
        label 'pyAgent'
    }    
    stages {

        stage('Python build of file') {   
            steps {
                // Ejecuta el archivo hola-mundo.py
                sh 'python3 hola-mundo.py'
            }
            }
        }
    }
