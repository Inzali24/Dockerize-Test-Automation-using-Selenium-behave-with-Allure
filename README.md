# Dockerize-Test-Automation-using-Selenium-behave-with-Allure
Automate Testing JavaScript Programming Problems
## Set up & Installation.
## Run the application with Docker
## Clone/Fork the git repo
### 1. Navigate to the project directory

`cd Features`

### 2. Docker Build using Dockerfile in project

**Windows**

`docker build -t features .`
<br>

**macOS/Linux**

`docker build -t features .`

### 3. See the docker image
          
**Windows** 

```docker images```
          
**macOS/Linux**

```$docker images```

You will see your image like this .
REPOSITORY      TAG       IMAGE ID       CREATED              SIZE
features        latest    936610d64c75   About a minute ago   1.37GB

### 4 .Run docker image

`docker run -dp 5000:5000 features`

### 5 .Run docker image
Now the system is running in port:5000 and you can access from browser via localhost:5000

## Congratulations! You can now proceed with the system.