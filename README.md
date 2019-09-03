# ci-pipeline

## Jenkins Crumb Example (CURL)

```bash
curl -u "usernmae:password" 'JenkinsURL/crumbIssuer/api/xml?xpath=concat(//crumbRequestField,":",//crumb)'
curl -X POST -u "usernmae:password" -H "Jenkins-Crumb:xxxxxxxxxxxxxxxxxxxx" "JenkinsURL/job/JObName/build"
```
