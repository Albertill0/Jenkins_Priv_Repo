pipeline {
    agent {
        label 'agentePi' // Cambiado a agentePi3
    }
    options {
        // Opciones adicionales para asegurar el correcto manejo de credenciales
        skipDefaultCheckout(true) // Evita el checkout por defecto
    }
    stages {
        stage('Git Clone and Dependency Scan') {
            steps {
                script {
                    // Realizar git clone con las credenciales
                    checkout([$class: 'GitSCM',
                        branches: [[name: 'master']], // Puedes cambiar el nombre de la rama si es necesario
                        userRemoteConfigs: [[
                            url: 'https://github.com/Albertill0/Jenkins_Priv_Repo.git',
                            credentialsId: 'Github']]]) // Reemplaza con tu ID de credenciales
                }
            }
        }
        stage('OWASP Dependency-Check Vulnerabilities') {
            steps {
                // Cambiar al directorio del clon antes de ejecutar el escaneo de dependencias
                dir('nombre_del_directorio_clonado') { // Reemplaza 'nombre_del_directorio_clonado' con el nombre correcto del directorio
                    dependencyCheck additionalArguments: ''' 
                        -o './'
                        -s './'
                        -f 'HTML' 
                        --prettyPrint''', odcInstallation: 'OWASP Dependency-Check Vulnerabilities'
                    dependencyCheckPublisher pattern: 'dependency-check-report.xml'
                }
            }
        }
        stage('Ejecutar python3 hola-mundo.py') {
            steps {
                script {
                    // Hola de reconocimiento con Hook
                    sh 'echo "Hola"'
                    sh 'echo "Hook2"'
                    // Aquí se ejecuta el archivo hola-mundo.py
                    sh 'python3 holamundo.py'
                }
            }
        }
    }
}

