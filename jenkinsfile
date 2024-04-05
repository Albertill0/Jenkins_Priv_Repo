pipeline {
    agent {
        label 'CMake'
    }

podTemplate(containers: [
    containerTemplate(
        name: 'jnlp', 
        image: 'jenkins/inbound-agent:latest'
        ),
    containerTemplate(
        name: 'python', 
        image: 'python:latest', 
        command: 'sleep', 
        args: '30d')
  ]) {

node(POD_LABEL){
    stages {
        stage('Clonar repositorio privado de python') {
            steps {
                script {
                    // Clonar el repositorio utilizando las credenciales específicas
                    git credentialsId: 'GithubUsrPass', url: 'https://github.com/Albertill0/Jenkins_Priv_Repo.git', branch: 'python'
                    
                    // Establecer la identidad del usuario para este repositorio
                    sh 'git config user.email "Alberto.Quintana@alu.uclm.es"'
                    sh 'git config user.name "Albertill0"'
                }
                container('python') {
                stage('Compile python file') {
                    sh '''
                    python3 hola-mundo.py
                    '''
                }
            }
            }
        }
      }
    }
  }
}
