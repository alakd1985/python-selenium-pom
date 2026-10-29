
pipeline {
    agent any

    options {
        timestamps()
        timeout(time: 90, unit: 'MINUTES')
        skipDefaultCheckout(true)
    }

    environment {
        HEADLESS = 'true'
        PYTHONUNBUFFERED = '1'

        // Demo credentials for the MediShop test application
        MEDISHOP_USERNAME = 'trainer@way2automation.com'
        MEDISHOP_PASSWORD = 'way2automation'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install dependencies') {
            steps {
                sh '''
                    set -eu

                    /Library/Frameworks/Python.framework/Versions/3.11/bin/python3.11 --version

                    rm -rf venv
                    /Library/Frameworks/Python.framework/Versions/3.11/bin/python3.11 -m venv venv

                    venv/bin/python -m pip install --upgrade pip
                    venv/bin/python -m pip install -r requirements.txt
                    venv/bin/python -m pip install ruff

                    mkdir -p reports
                '''
            }
        }

        stage('Lint') {
            steps {
                sh 'venv/bin/python -m ruff check .'
            }
        }

        stage('Firefox tests') {
            steps {
                catchError(
                    buildResult: 'UNSTABLE',
                    stageResult: 'FAILURE'
                ) {
                    sh '''
                        BROWSER=firefox HEADLESS=true \
                        venv/bin/python -m pytest tests/medishop/ \
                        --browser=firefox --headless \
                        -v -ra --color=yes \
                        --junitxml=reports/firefox.xml
                    '''
                }
            }
        }

        stage('Chrome tests') {
            steps {
                catchError(
                    buildResult: 'UNSTABLE',
                    stageResult: 'FAILURE'
                ) {
                    sh '''
                        BROWSER=chrome HEADLESS=true \
                        venv/bin/python -m pytest tests/medishop/ \
                        --browser=chrome --headless \
                        -v -ra --color=yes \
                        --junitxml=reports/chrome.xml
                    '''
                }
            }
        }
    }

    post {
        always {
            junit(
                allowEmptyResults: true,
                testResults: 'reports/*.xml'
            )
        }

        success {
            echo 'All pipeline stages completed successfully.'
        }

        unstable {
            echo 'One or more test stages failed. Check the JUnit reports.'
        }

        failure {
            echo 'The pipeline failed. Check the failed stage in Console Output.'
        }
    }
}
