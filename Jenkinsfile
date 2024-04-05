pipeline {
    agent {
        label 'CMake'
    }    
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
        
        stage('Configurar y compilar proyecto C++ con CMake') {
            steps {
                // Crear un directorio de compilación separado
                dir('build') {
                    // Configurar el proyecto con CMake
                    sh '/usr/local/bin/cmake ../CMakeLists.txt'
                    
                    // Compilar el proyecto
                    sh '/usr/local/bin/make'
                }
            }
        }
    }
}
