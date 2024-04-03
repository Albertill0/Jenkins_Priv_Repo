pipeline {
    agent any
    
    stages {
        stage('Clonar repositorio privado') {
            steps {
                script {
                    // Clonar el repositorio utilizando las credenciales específicas
                    git credentialsId: 'GithubUsrPass', url: 'https://github.com/Albertill0/Jenkins_Priv_Repo.git'
                    
                    // Establecer la identidad del usuario para este repositorio
                    sh 'git config user.email "Alberto.Quintana@alu.uclm.es"'
                    sh 'git config user.name "Albertill0"'
                }
            }
        }
        --
    }
}
