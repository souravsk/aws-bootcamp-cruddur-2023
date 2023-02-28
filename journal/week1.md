# Week 1 — App Containerization
# **Containers**

Containers are packages of software that contain all of the necessary elements to run in any environment. In this way, containers virtualize the operating system and run anywhere, from a private data centre to the public cloud or even on a developer’s personal laptop.

## **Containers and Virtual Machines**

Containers and virtual machines have similar resource isolation and allocation benefits but function differently because containers virtualize the operating system instead of the hardware. Containers are more portable and efficient.

![https://cdn.hashnode.com/res/hashnode/image/upload/v1660815597814/tYxaxuaUw.png?auto=compress,format&format=webp](https://cdn.hashnode.com/res/hashnode/image/upload/v1660815597814/tYxaxuaUw.png?auto=compress,format&format=webp)

(I created this fig when I was writing a blog on docker )

# Docker

Docker is a container platform that allows you to build, test and deploy applications quickly. A developer defines all the application and its dependencies in a Dockerfile which is used to build Docker images that define containers

**Docker Containers:-** is a running instance of a Docker Image as. they hold the entire package needed to run the application. So, these are basically the ready application created from docker Images which is the ultimate utility of docker

**Docker Images:-** A container image is a lightweight, Standalone, executable package of software that includes everything needed to run an application's code, runtime, system tools, system libraries, and settings, container image becomes container runtime. In layman's terms, Docker Image can be compared to the template which is used to create a docker container. So their read-only template is the building block of a container you can use `docker run`
 to run the image and create a container.

**Dockerfile:-** A Dockerfile is a text document that contains all the commands the user can call on the Command line to assemble an image. so Docker can build Images automatically by reading the instructors from a Dockerfile. you can use docker build to create an automated build to execute several command-Line instructions in succession

**Docker hub:-**  Docker Hub repositories allow you to share container images with your team, customers, or the Docker community at large. Docker images are pushed to Docker Hub through the `[docker push](https://docs.docker.com/engine/reference/commandline/push/)` command. A single Docker Hub repository can hold many Docker images

# Creating Dockerfile for Backend

So I did all thing will watching the video of week 1.

So after opening the gitpod I opened the terminal and change the directory and move to the backed-flask directory so we can install all the requirements that need to run the backend. So we used the command `pip3 install - r requirements.txt` this requirements.txt file have all the required file needed to run the backend. After running this command it got installed successfully. We can also run the backend by using python command which is `python3 -m flask run --host=0.0.0.0 --port=4567`     

![](img)

![](img)

Now it is time to create the dockerfile so first created a file named `dockerfile` with no extension. after that, I pasted the file content from the repo that is provided to us. Now we can build the docker image with the dockerfile that I just created. 

![](img)

As you can see the image is built successfully. To see the built image we can use the command `docker images` now we can run the docker image with the help of the docker command that is `docker run --rm -p 4567:4567 -it backend-flask`

The backend server did start but it was showing the error. So I show on the live stream it happens because of the env our environment is not set so we will set the env while running the docker image. which is `docker run --rm -p 4567:4567 -it -e FRONTEND_URL="*" -e BACKEND_UR="*" backend-flask` 

![](img)

yes! it worked now if go to the docker address which I show on the port session of he vs code and if go you get the link make sure unlock the link .

![](img)

# Creating the Dockerfile for the frontend

Now change the directory to the frontend-react-js directory and on first I install the npm with the command `npm i`  

![](img)

Now created the dockerfile and pasted the content. Then i build and run the docker image as we did on the backend.

# Creating the Docker-compose file

Compose is a tool for defining and running multi-container Docker applications. With Compose, you use a YAML file to configure your application’s services. Then, with a single command, you create and start all the services from your configuration.

Compose works in all environments: production, staging, development, testing, as well as CI workflows. It also has commands for managing the whole lifecycle of your application

So with the help of the docker-compose, we can don’t have to run both the frontend and backend servers one by one on different terminals and we have to manage ourselves.

So I’m using the docker-compose to create the compose file go to the root directory and create a file name `docker-compose.yml` in this file paste the code from the repo.

Now we have to run the docker-compose file we can do with a different way I just right-click on the docker-compose file and it has the option to compose up which will run the docker-compose file 

![](img)

![](img)

![](img)