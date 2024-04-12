pipeline {
    agent {
        label 'agentePi'
    }    
        stages {
        
        stage('Configurar y compilar proyecto C++ con CMake') {
            steps {
                // Crear un directorio de compilación separado
                dir('build') {
                    // Configurar el proyecto con CMake
                    sh 'cmake ../CMakeLists.txt'
                    
                    // // Compilar el proyecto
                    // sh 'make'
                }
            }
        }
    }
}
