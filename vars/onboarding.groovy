#!groovy

import hudson.FilePath;
import jenkins.model.Jenkins;

@Library('jenkins-shared@master') _
def projectCreatorBB = libraryResource 'onboarding.py'
def projectCreatorJira = libraryResource 'onboardingjira.py'
def requirementText = libraryResource 'requirements.txt'
def projectNameBB = "${ProjectNameBB}"
def workspaceID = "${WorkspaceID}"
def project_Key_BB = "${Project_Key_BB}"
def project_Key_Jira = "${Project_Key_Jira}"
def newRepo = "${NewRepo}"
def taskSummary = "${TaskSummary}"
def taskDesciption = "${TaskDesciption}"
def projectNameJira = "${ProjectNameJira}"

pipeline {
    agent {
        docker {
            image 'python:3.7.2'
        }
    }
    stages {
        stage('BitBucket Project Creation') {
            steps {
                writeFile file: 'onboardingscriptbb.py', text: "${projectCreatorBB}"
                writeFile file: 'requirements.txt', text: "${requirementText}"
                sh 'python3 -m pip install -r requirements.txt'
                withCredentials([usernamePassword(credentialsId: 'BBId', passwordVariable: 'bbpassword', usernameVariable: 'bbusername')]) {
                    sh 'python3 -u ./onboardingscriptbb.py ${ProjectNameBB} ${bbusername} ${bbpassword} ${WorkspaceID} ${NewRepo} ${Project_Key_BB}'
                }
            }
        }
        stage('Jira Project Creation') {
            steps {
                writeFile file: 'onboardingscriptjira.py', text: "${projectCreatorJira}"
                withCredentials([string(credentialsId: 'LeadAccountId', variable: 'LeadAccountId')]) {

                    withCredentials([usernamePassword(credentialsId: 'JiraId', passwordVariable: 'jiraapikey', usernameVariable: 'jirausername')]) {
                        sh 'python3 -u ./onboardingscriptjira.py ${Project_Key_Jira} ${TaskSummary} ${TaskDesciption} ${jirausername} ${jiraapikey} ${LeadAccountId} ${ProjectNameJira}'
                    }


                }

            }
        }
    }
}
