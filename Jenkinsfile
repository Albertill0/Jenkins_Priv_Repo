pipeline {
    agent {
        label 'agentePi'
    }
    stages {
        stage('Launch Agent') {
            steps {
                script {
                    // Ejecutar el comando para cambiar de directorio, dar permisos al script y ejecutarlo
                    sh 'cd ~/bin/agent.jar && chmod +x exec.sh && ./exec.sh'
                }
            }
        }
        stage('Clonar Repositorio') {
            steps {
                script {
                    // Clonar el repositorio
                    git 'https://github.com/Albertill0/Jenkins_Priv_Repo.git'
                }
            }
        }
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
