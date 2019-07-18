"""
Created on Tue July 16 09.39.45 2019
@author: Chiranjeevi
"""

import sys, getopt , requests
import json
from requests.auth import HTTPDigestAuth

ProjectName = str(sys.argv[1])
Consumer_Key = str(sys.argv[2])
Consumer_Secret = str(sys.argv[3])
Team = str(sys.argv[4])
NewRepo = str(sys.argv[5])
ProjKey = str(sys.argv[6])

class APIException(Exception) :
   pass

def createBitBucketProject():
   print("Creating Bit Bucket Project")
   request = {
     'has_wiki': 'true',
     'is_private': 'true',
     'project': {
       'key': ProjKey
     }
   }
   print(json.dumps(request,indent=4,sort_keys=True))
   URL_USER_INFO = 'https://api.bitbucket.org/2.0/user'
   r = requests.get(URL_USER_INFO, auth=(Consumer_Key, Consumer_Secret))
   print(r.status_code)
   print(json.dumps(r.json(),indent=4,sort_keys=True))   
   URL_CREATE_REPO='https://api.bitbucket.org/2.0/repositories/'+ Team +'/'+ NewRepo
   resp = requests.post(URL_CREATE_REPO, json=request, auth=(Consumer_Key, Consumer_Secret), headers={"content-type":"application/json"})
   print(resp.status_code)
   if resp.status_code == 200:
       print("BitBucket Project has been created successfully")
       print(json.dumps(resp.json(),indent=4,sort_keys=True))
   elif resp.status_code == 400:
       print("BitBucket Project already exits")
       print(json.dumps(resp.json(),indent=4,sort_keys=True))
   else:
       raise APIException("Unable to Create BitBucket Project",resp)
  

def createJiraProject():
   print("Creating Jira Project")

if __name__ == "__main__":
   createBitBucketProject()
   createJiraProject()