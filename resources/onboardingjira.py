"""
Created on Tue July 17 09.39.45 2019
@author: Chiranjeevi
"""

import sys, getopt, requests
import json
from requests.auth import HTTPBasicAuth 

ProjKey = str(sys.argv[1]) 
TaskSummary = str(sys.argv[2])
TaskDesciption = str(sys.argv[3])
UserEmail = str(sys.argv[4])
APIKey = str(sys.argv[5])
LeadAccountId = str(sys.argv[6])
ProjectName = str(sys.argv[7])


class APIException(Exception):
  pass

def createJiraProject():
   print("Creating Jira Project")

   url1 = "https://chiranjeevivc.atlassian.net/rest/api/2/project"

   payload = json.dumps( {
      'description': 'Created Through Automation Script',
      'url': 'http://atlassian.com',
      'projectTemplateKey': 'com.atlassian.jira-core-project-templates:jira-core-simplified-project-management',
      'name': ProjectName,
      'assigneeType': 'UNASSIGNED',
      'projectTypeKey': 'business',
      'key': ProjKey,
      'leadAccountId': LeadAccountId
    })

   response  = requests.post( url1, data = payload, auth=(UserEmail,APIKey), headers={"content-type":"application/json"} )
   print(response.status_code)
   print(json.dumps(response.json(),indent=4,sort_keys=True))
   if response.status_code == 201:
       print("Jira Project has been created successfully")
       print(json.dumps(response.json(),indent=4,sort_keys=True))
   elif response.status_code == 400:
       print("Invalid Project Inputs")
       print(json.dumps(response.json(),indent=4,sort_keys=True))
   else:
       raise APIException("Unable to Create Jira Project",response)

def createJiraIssue():
   print("Creating Jira Project")
   url2 = "https://chiranjeevivc.atlassian.net/rest/api/2/issue"
   payload = json.dumps( {
       'fields':{
           'project':{
               'key': ProjKey,
           },
           'summary':TaskSummary,
           'description':TaskDesciption,
           'issuetype':{
               'name':'Task'
           }
       }
   } )
   response  = requests.post( url2, data = payload, auth=(UserEmail,APIKey), headers={"content-type":"application/json"} )
   print(response.status_code)
   if response.status_code == 201:
       print("Jira Issue has been added successfully")
       print(json.dumps(response.json(),indent=4,sort_keys=True))
   elif response.status_code == 400:
       print("Invalid Project Inputs")
       print(json.dumps(response.json(),indent=4,sort_keys=True))
   else:
       raise APIException("Unable to Create Jira Project",response)


if __name__ == "__main__":
   createJiraProject()
   createJiraIssue()