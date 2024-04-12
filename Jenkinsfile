pipeline {
    agent {
        label 'agentePi2'
    }
    stages {
        stage('Ejecutar python3 hola-mundo.py') {
            steps {
                script {
                    // Hola de reconocimiento
                    sh 'echo "Hola"'
                    // Aquí se ejecuta el archivo hola-mundo.py
                    sh 'python3 hola-mundo.py'
                }
            }
        }
    }
}
