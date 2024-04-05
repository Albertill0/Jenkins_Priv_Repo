pipeline {
    agent {
        label 'pyAgent'
    }
    stages {
        stage('Python3 build of file') {
            environment {
                // Define las credenciales de GitHub
                GIT_CREDENTIALS = credentials('GithubUsrPass')
            }
            steps {
                // Clona el repositorio de GitHub desde una rama específica
                script {
                    git branch: 'python',
                        credentialsId: GIT_CREDENTIALS,
                        url: 'https://github.com/Albertill0/Jenkins_Priv_Repo.git'
                }
                
                // Ejecuta el archivo hola-mundo.py
                sh 'python3 hola-mundo.py'
            }
        }
    }
}
