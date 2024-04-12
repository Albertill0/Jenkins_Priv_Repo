pipeline {
    agent {
        label 'agentePi'
    }
    stages {
        stage('waiting') {
        hook = registerWebhook()
        
        echo "Waiting for POST to ${hook.url}"
        data = waitForWebhook hook
        
        echo "Webhook called with data: ${data}"
    }
        stage('Ejecutar python3 hola-mundo.py') {
            steps {
                script {
                    // Hola de reconocimiento
                    sh 'echo "Hola"'
                    // Aquí se ejecuta el archivo hola-mundo.py
                    sh 'python3 holamundo.py'
                }
            }
        }
    }
}
