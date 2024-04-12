pipeline {
    agent {
        label 'agentePi'
    }    
    stages {
        stage('Configurar y compilar proyecto C++ con CMake') {
            steps {
                // Crear un directorio de compilación separado
                dir('build') {
                    // Configurar el proyecto con CMake desde el directorio de compilación
                    sh 'cmake ../ .'
                    
                    // Compilar el proyecto con make desde el mismo directorio de compilación
                    sh 'cd /home/jenkins/agent/workspace/agentePi-Cmake && make'
                }
            }
        }
    }
}
