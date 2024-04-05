pipeline {
    agent {
        label 'pyAgent'
    }
    stages {
        stage('Ejecutar python3 hola-mundo.py') {
            steps {
                script {
                    // Aquí se ejecuta el archivo hola-mundo.py
                    sh 'python3 hola-mundo.py'
                }
            }
        }
    }
}
