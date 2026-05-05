pipeline {
    agent any
    
    environment {
        // Environment variables available to all stages
        PROJECT_NAME = 'ETL_Pipeline'
        PYTHON_VERSION = 'python'
    }
    
    stages {
        stage('Setup') {
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
                // Execute the ETL script
                bat 'python etl.py'
            }
        }
        
        stage('Run Tests') {
            steps {
                echo '🧪 Running data quality tests...'
                // Run test suite
                bat 'python test_data.py'
            }
        }
        
        stage('Archive Results') {
            steps {
                echo '📦 Archiving artifacts...'
                // Archive the output files
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
        always {
            echo '🧹 Cleaning up workspace...'
            // Clean up can be added here if needed
        }
    }
}
