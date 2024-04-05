pipeline {
    agent {
        label 'jenkins-python-agent'
    }
    stages {
        stage('Python build of file') {
            steps {
                // Clona el repositorio de GitHub
                git 'https://github.com/tu_usuario/tu_repositorio.git'
                
                // Ejecuta el archivo hola-mundo.py
                sh 'python hola-mundo.py'
            }
        }
    }
}
