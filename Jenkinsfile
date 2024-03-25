pipeline {
    agent any
    
    environment {
        GIT_COMMITTER_NAME = 'Albertill0'
        GIT_COMMITTER_EMAIL = 'Alberto.Quintana@alu.uclm.es'
    }
    
    stages {
        stage('Clonar Repositorio') {
            steps {
                // Clona el repositorio desde GitHub utilizando las credenciales
                git credentialsId: 'GithubUsrPass', url: 'https://github.com/Albertill0/Jenkins_Priv_Repo.git'
            }
        }
        stage('Build') {
            steps {
                // Genera el archivo README_BUILD
                sh 'echo "HOLA PIPELINA" > README_BUILD'
                // Agrega y commitea el archivo README_BUILD
                sh 'git add README_BUILD'
                sh 'git commit -m "Añadir README_BUILD generado por la pipeline"'
            }
        }
        stage('Pruebas') {
            steps {
                // Muestra el contenido de README_BUILD
                sh 'cat README_BUILD'
            }
        }
        stage('Despliegue') {
            steps {
                // Empuja los cambios al repositorio
                sh 'git push origin master'
            }
        }
    }
}
