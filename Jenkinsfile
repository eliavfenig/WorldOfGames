pipeline {
  	agent {
        label 'wog'
    } 

	stages {
	  stage('checkout') {
		steps {
		  git branch: 'wog-4.1',
			url: 'https://github.com/eliavfenig/WorldOfGames.git'
		}
	  }
	  stage('Build') {
		steps {
		  bat 'docker build -t wog:v0.1 .'
		}
	  }
	  stage('Run') {
		steps {
		  bat 'docker run -d -p 8777:5000 wog:v0.1 > a.txt'
		}
	  }
	  stage('Test') {
		steps {
			bat 'C:\\Users\\eliav\\AppData\\Local\\Programs\\Python\\Python39\\scripts\\pip.exe install selenium'
			bat 'C:\\Users\\eliav\\AppData\\Local\\Programs\\Python\\Python39\\python Test\\e2e.py'
		}
	  }
	  stage('Finalize') {
		steps {
		  powershell 'docker stop (cat a.txt)'
		  bat 'docker compose push'
		}
	  }
	}
}
