pipeline {
    agent any
    
    environment {
        PROJECT_NAME = 'ETL_Pipeline'
    }
    
    stages {
        stage('Checkout') {
            steps {
                echo '📂 Cloning from GitHub...'
                checkout scm
            }
        }
        
        stage('Install Dependencies') {
            steps {
                echo '📦 Installing dependencies...'
                sh '''
                    python3 --version
                    pip3 install --break-system-packages -r requirements.txt
                '''
            }
        }
        
        stage('Run ETL') {
            steps {
                echo '🚀 Running ETL Pipeline...'
                sh 'python3 etl.py'
            }
        }
        
        stage('Run Tests') {
            steps {
                echo '🧪 Running data quality tests...'
                sh 'python3 test_data.py'
            }
        }
        
        stage('Archive Results') {
            steps {
                echo '📦 Archiving artifacts...'
                archiveArtifacts artifacts: 'output/**/*', allowEmptyArchive: false
            }
        }
    }
    
    post {
        success {
            echo '✅ Pipeline completed successfully!'
        }
        failure {
            echo '❌ Pipeline failed! Check logs above.'
        }
    }
}
