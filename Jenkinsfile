pipeline {
    agent {
        label 'pyAgent'
    }
    stages {
        // stage('Preparar ambiente') {
        //     steps {
        //         script {
        //             // Instalar Git
        //             sh 'apk update && apk add --no-cache git'
        //         }
        //     }
        // }
        stage('Ejecutar hola-mundo.py') {
            steps {
                script {
                    // Aquí se ejecuta el archivo hola-mundo.py
                    sh 'python hola-mundo.py'
                }
            }
        }
    }
}
