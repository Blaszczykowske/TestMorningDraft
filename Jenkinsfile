pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Blaszczykowske/TestMorningDraft.git'
            }
        }

        stage('Set up virtualenv') {
            steps {
                bat "python -m venv %VENV_DIR%"
                bat ".\\%VENV_DIR%\\Scripts\\pip install --upgrade pip"
                bat ".\\%VENV_DIR%\\Scripts\\pip install -r requirements.txt"
            }
        }

        stage('Run Main Script') {
            steps {
                bat ".\\%VENV_DIR%\\Scripts\\python main.py"
            }
        }

        stage('Run Tests') {
            steps {
                bat ".\\%VENV_DIR%\\Scripts\\pip install pytest"
                bat ".\\
