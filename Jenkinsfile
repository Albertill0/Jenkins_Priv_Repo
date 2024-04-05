pipeline {
    agent {
        label 'pyAgent'
    }
    stages {
        stage('Ejecutar hola-mundo.py') {
            steps {
                script {
                    // Aquí se ejecuta el archivo hola-mundo.py
                    sh 'python hola-mundo.py'
                }
            }
        }
    }
}
