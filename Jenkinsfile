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
		  bat 'docker compose build'
		}
	  }
	  stage('Run') {
		steps {
		  bat 'docker compose up'
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
		  bat 'docker compose down'
		  bat 'docker compose push'
		}
	  }
	}
}
