import sys, getopt

ProjectName = sys.argv[1]
Username = sys.argv[2]
Password = sys.argv[3]

def my_function(argv):
   print("My First Project:", argv )
   print(ProjectName)
   print(Username)
   print(Password)

def createBitBucketProject():
   print("Creating Bit Bucket Project")

def createJiraProject():
   print("Creating Jira Project")

if __name__ == "__main__":
   my_function(sys.argv[1])
   createBitBucketProject()
   createJiraProject()