pipeline {
  agent any
  stages {
    stage('stage1') {
      parallel {
        stage('stage1') {
          steps {
            echo 'test starts'
          }
        }

        stage('stage 1.1') {
          steps {
            sh '''echo "stage 1.1"
'''
          }
        }

      }
    }

    stage('stage 2.1') {
      steps {
        sh 'echo "2.1"'
      }
    }

  }
}