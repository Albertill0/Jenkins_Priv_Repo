pipeline {
    agent {
        label 'pyAgent'
    }
    stages {
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
