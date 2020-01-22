def COLOR_MAP = ['SUCCESS': 'good', 'FAILURE': 'danger', 'UNSTABLE': 'danger', 'ABORTED': 'danger']

pipeline {
  agent any
  options
  {
     timestamps ()
     timeout(time: 1, unit: 'HOURS')
  }
  stages {
    stage('Nofity release start') {
      when {
        branch 'master'
      }
      steps {
        slackSend message: "Start deploying *${LIB_NAME}.*\n More info at: ${env.RUN_DISPLAY_URL}"
      }
    }
    stage('Build') {
      parallel {
        stage('Image build') {
          steps {
            sh '''
              docker build \
              --build-arg REQUIREMENTS=dev \
              -t ${LIB_NAME} .
              '''
          }
        }
      }
    }
    stage('Static code metrics') {
      steps {
        sh '''
          docker run --workdir /home/src/${LIB_NAME} --mount type=bind,source="$(pwd)",target=/home/src/${LIB_NAME} ${LIB_NAME} flake8 .
        '''
      }
    }
    stage('Unit tests') {
      post {
        always {
          junit '**/reports/**/*.xml'
          sh 'rm -rf ${SDK_CONTENT_FOLDER}/reports/*'
        }
      }
      steps {
          sh 'mkdir -p "${SDK_CONTENT_FOLDER}/reports"'
          sh 'docker run --workdir /home/src/${SERVICE_NAME}/ --mount type=bind,source="$(pwd)/${SDK_CONTENT_FOLDER}/reports",target=/home/src/${SERVICE_NAME}/reports ${SDK_DOCKER_TESTS_IMAGE} pytest --verbose --junit-xml reports/unit_tests_results.xml ${SDK_ROOT_FOLDER}'
      }
    }
    stage('PyPi Deploy') {
      when {
        branch 'master'
      }
      steps {
        sh 'docker run --workdir /home/src/${LIB_NAME}/ ${LIB_NAME} poetry publish -u ${PYPI_USER} -p ${PYPI_PWD}'
      }
    }
  }
  post {
    always {
      script {
        if (GIT_LOCAL_BRANCH == 'master')
          slackSend color: COLOR_MAP[currentBuild.currentResult],
            message: "Deploy ${LIB_NAME} *${currentBuild.currentResult}.*\nBuild time:" + currentBuild.duration + " ms\n More info at: ${env.RUN_DISPLAY_URL}"
      }
    }
  }
  environment {
    LIB_NAME = 'nurse'
  }
}