pipeline {
    agent {
        label 'agentePi' // El correcto es con agentePi3
    }
    stages {
    //     stage('OWASP Dependency-Check Vulnerabilities') {
    //   steps {
    //     dependencyCheck additionalArguments: ''' 
    //                 -o './*'
    //                 -s './*'
    //                 -f 'HTML' 
    //                 --prettyPrint''', odcInstallation: 'OWASP Dependency-Check Vulnerabilities'
        
    //     dependencyCheckPublisher pattern: 'dependency-check-report.xml'
    //   }
    // }
        stage('Ejecutar python3 hola-mundo.py') {
            steps {
                script {
                    // Hola de reconocimiento con Hook
                    sh 'echo "Hola"'
                    sh 'echo "Hook2"'
                    // Aquí se ejecuta el archivo hola-mundo.py
                    // sh 'python3 holamundo.py'
                }
            }
        }
    }
}
