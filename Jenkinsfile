pipeline {
    agent {
        label 'agentePi'
    }
    stages {
        
        stage('ZAP') {
            steps {
                sh 'echo "estoy aqui"'
                dependencyCheck additionalArguments:'',odcInstallation: 'dependency-check'
                dependencyCheckPublisher pattern: '**/dependency-check-report.html'
                sh 'echo "termino"'
            }
        }
        
        stage('Ejecutar python3 hola-mundo.py') {
            steps {
                script {
                    // Hola de reconocimiento con Hook
                    sh 'echo "Hola"'
                    sh 'echo "Hook2"'
                    // Aquí se ejecuta el archivo hola-mundo.py
                    sh 'python3 holamundo.py'
                }
            }
        }
    }
}
