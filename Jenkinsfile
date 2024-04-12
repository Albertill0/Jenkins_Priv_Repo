pipeline {
    agent {
        label 'agentePi'
    }
    stages {
        stage('Ejecutar python3 hola-mundo.py') {
            steps {
                script {
                    // Hola de reconocimiento con Hook
                    sh 'echo "Hola"'
                    // Aquí se ejecuta el archivo hola-mundo.py
                    sh 'python3 holamundo.py'
                }
            }
        }
    }
}
