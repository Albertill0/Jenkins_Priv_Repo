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
                    sh 'cmake -G "Unix Makefiles" ${WORKSPACE}/'
                    
                    // Compilar el proyecto con make desde el mismo directorio de compilación
                    sh 'make -C ${WORKSPACE}/build'
                }
            }
        }
    }
}
