pipeline {
    agent {
        label 'manito'
    }
    stages {
        stage('Instalar Dependencias') {
            steps {
                script {
                    // Instalar Python
                    sh 'apt-get update && apt-get install -y python3'
                    // Puedes agregar más comandos aquí para instalar otras dependencias si es necesario
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
