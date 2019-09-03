# ci-pipeline

## Jenkins Crumb Example (CURL)

```bash
curl -u "usernmae:password" 'JenkinsURL/crumbIssuer/api/xml?xpath=concat(//crumbRequestField,":",//crumb)'
curl -X POST -u "usernmae:password" -H "Jenkins-Crumb:xxxxxxxxxxxxxxxxxxxx" "JenkinsURL/job/JobName/build"
curl -X POST -u "usernmae:password" -H "Jenkins-Crumb:xxxxxxxxxxxxxxxxxxxx" "JenkinsURL/job/JobName/buildWithParameters" --data-urlencode json='{"parameter": [{"Proj_Key":"MDC", "NewRepo":"demo"}]}'
```
