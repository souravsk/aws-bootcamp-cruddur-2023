# Week 6 - 7 — Serverless Containers

# What is Fargate?

AWS Fargate is a technology that you can use with Amazon ECS to run [containers](https://aws.amazon.com/what-are-containers) without having to manage servers or clusters of Amazon EC2 instances. With Fargate, you no longer have to provision, configure, or scale clusters of virtual machines to run containers. This removes the need to choose server types, decide when to scale your clusters, or optimize cluster packing.

When you run your Amazon ECS tasks and services with the Fargate launch type or a Fargate capacity provider, you package your application in containers, specify the Operating System, CPU and memory requirements, define networking and IAM policies, and launch the application. Each Fargate task has its own isolation boundary and does not share the underlying kernel, CPU resources, memory resources, or elastic network interface with another task.

![36](img/week-6-7/week6-7%20(36).png)

# AWS ECR

Amazon Elastic Container Registry (Amazon ECR) is an AWS-managed container image registry service that is secure, scalable, and reliable. Amazon ECR supports private repositories with resource-based permissions using AWS IAM. This is so that specified users or Amazon EC2 instances can access your container repositories and images. You can use your preferred CLI to push, pull, and manage Docker images, Open Container Initiative (OCI) images, and OCI-compatible artifacts.

## Created Python Repo

We need to create a Python Repo in ECR because if pull images from docker it may sometime not pull the image. So we will pull that image in Python and store it on ECR so that we can call it anytime we need.

### Creating Repo for Python

![4](img/week-6-7/week6-7%20(4).png)

![3](img/week-6-7/week6-7%20(3).png)

### Pulling the Pythone images and then pushing it to the newly created repo on ECR

![5](img/week-6-7/week6-7%20(5).png)

![6](img/week-6-7/week6-7%20(6).png)

## Created Backend Repo

First, we will create a repo for the Backend as we did for Python.

![7](img/week-6-7/week6-7%20(7).png)

We will build the images and then push the image to the repo.

![9](img/week-6-7/week6-7%20(9).png)

Now it is pushed let's see them on AWS.

![8](img/week-6-7/week6-7%20(8).png)

# **AWS Systems Manager**

AWS Systems Manager is the operations hub for your AWS applications and resources and a secure end-to-end management solution for hybrid cloud environments that enable secure operations at scale.

## **AWS Systems Manager Parameter Store**

Parameter Store, a capability of AWS Systems Manager, provides secure, hierarchical storage for configuration data management and secrets management. You can store data such as passwords, database strings, Amazon Machine Image (AMI) IDs, and license codes as parameter values. You can store values as plain text or encrypted data. You can reference Systems Manager parameters in your scripts, commands, SSM documents, and configuration and automation workflows by using the unique name that you specified when you created the parameter.

### Now we will push all those secrets that our backend needs

![10](img/week-6-7/week6-7%20(10).png)

![11](img/week-6-7/week6-7%20(11).png)

# Added Policy and Roles

![12](img/week-6-7/week6-7%20(12).png)

# AWS ECS

Amazon Elastic Container Service (Amazon ECS) is a fully managed container orchestration service that helps you easily deploy, manage and scale containerized applications. As a fully managed service, Amazon ECS comes with AWS configuration and operational best practices built-in. This also means that you don't need to manage the control planes, nodes, or add-ons. It's integrated with AWS and third-party tools, such as Amazon Elastic Container Registry and Docker. This integration makes it easier for teams to focus on building the applications, not the environment. You can run and scale your container workloads across AWS Regions in the cloud, and on-premises, without the complexity of managing a control plane or nodes.

The following are key features of Amazon ECS:

- A serverless option with AWS Fargate. With AWS Fargate, you don't need to manage servers, handle capacity planning, or isolate container workloads for security. Fargate handles the infrastructure management aspects of your workload for you. You can schedule the placement of your containers across your cluster based on your resource needs, isolation policies, and availability requirements.
- An external instance option with ECS Anywhere. With ECS Anywhere, you can use the Amazon ECS console and AWS CLI to manage your on-premises container workloads.
- An Amazon EC2 option. With EC2, you can use the Amazon ECS console and AWS CLI to manage your EC2 instances.
- Integration with AWS Identity and Access Management (IAM). You can assign granular permissions for each of your containers. This allows for a high level of isolation when building your applications. In other words, you can launch your containers with the security and compliance levels that you've come to expect from AWS.
- AWS managed container orchestration.
- Continuous integration and continuous deployment (CI/CD). This is a common process for microservice architectures that are based on Docker containers. You can create a CI/CD pipeline that takes the following actions:
    - Monitors change to a source code repository
    - Builds a new Docker image from that source
    - Pushes the image to an image repository such as Amazon ECR or Docker Hub
    - Updates your Amazon ECS services to use the new image in your application
- Support for service discovery. This is a key component of most distributed systems and service-oriented architectures. With service discovery, your microservice components are automatically discovered as they're created and terminated on a given infrastructure.
- Support for sending your container instance log information to CloudWatch Logs. After you send this information to Amazon CloudWatch, you can view the logs from your container instances in one convenient location. This prevents your container logs from taking up disk space on your container instances.

## **Clusters**

An Amazon ECS *cluster* is a logical grouping of tasks or services. You can use clusters to isolate your applications. When your tasks are run on Fargate, your cluster resources are also managed by Fargate.

### Cluster with AWS CLI

![1](img/week-6-7/week6-7%20(1).png)

![2](img/week-6-7/week6-7%20(2).png) 

## **Task definitions**

A *task definition* is a text file that describes one or more containers that form your application. It's in JSON format. You can use it to describe up to a maximum of ten containers. The task definition functions as a blueprint for your application.

### Creating task definitions for the backend

![14](img/week-6-7/week6-7%20(14).png)

![15](img/week-6-7/week6-7%20(15).png)

we will do the same for the frontend part the process is just like the backend.

## **Tasks**

A *task* is the instantiation of a task definition within a cluster. After you create a task definition for your application within Amazon ECS, you can specify the number of tasks to run on your cluster. You can run a standalone task, or you can run a task as part of a service.

## **Services**

You can use an Amazon ECS *service* to run and maintain your desired number of tasks simultaneously in an Amazon ECS cluster. How it works is that, if any of your tasks fail or stop for any reason, the Amazon ECS service scheduler launches another instance based on your task definition. It does this to replace it and thereby maintain your desired number of tasks in the service.

## Backend ECS

### Created a Security group for services

![16](img/week-6-7/week6-7%20(16).png)

### Created services for the backend

![17](img/week-6-7/week6-7%20(17).png)

### The container is ready for the Backend

![18](img/week-6-7/week6-7%20(18).png)

### Let’s connect to the backend and check it is working or not.

![19](img/week-6-7/week6-7%20(19).png)

We are in we have successfully created the Backend ECS

Let’s visit the health check route.

![20](img/week-6-7/week6-7%20(20).png)

It is working.

## Frontend ECS

We will have to just follow the same step that we have to do for creating the backend container serves. Let's do that for the fronted.

So after creating the fronted ECR repo, we build the frontend container images and then we push that images to the ECR.

Then we will create the services for the fronted.

# AWS Certificates Manager

AWS Certificate Manager (ACM) handles the complexity of creating, storing, and renewing public and private SSL/TLS X.509 certificates and keys that protect your AWS websites and applications. You can provide certificates for your [integrated AWS services](https://docs.aws.amazon.com/acm/latest/userguide/acm-services.html)
 either by issuing them directly with ACM or by [importing](https://docs.aws.amazon.com/acm/latest/userguide/import-certificate.html)
 third-party certificates into the ACM management system. ACM certificates can secure singular domain names, multiple specific domain names, wildcard domains, or combinations of these. ACM wildcard certificates can protect an unlimited number of subdomains. You can also [export](https://docs.aws.amazon.com/acm/latest/userguide/export-private.html)
 ACM certificates signed by AWS Private CA for use anywhere in your internal PKI.

We have to created the certification.

![37](img/week-6-7/week6-7%20(37).png)

# AWS Route 53

Amazon Route 53 is a highly available and scalable Domain Name System (DNS) web service. You can use Route 53 to perform three main functions in any combination: domain registration, DNS routing, and health checking.

## **How internet traffic is routed to your website or web application**

All computers on the internet, from your smartphone or laptop to the servers that serve content for massive retail websites, communicate with one another by using numbers. These numbers, known as *IP addresses*, are in one of the following formats:

- Internet Protocol version 4 (IPv4) format, such as 192.0.2.44
- Internet Protocol version 6 (IPv6) format, such as 2001:0db8:85a3:0000:0000:abcd:0001:2345

When you open a browser and go to a website, you don't have to remember and enter a long string of characters like that. Instead, you can enter a domain name like example.com and still end up in the right place. A DNS service such as Amazon Route 53 helps to make that connection between domain names and IP addresses.

![35](img/week-6-7/week6-7%20(35).png)

## Purchased a Domain name for the Project

This is the first time I have purchased a domain name it was really very exciting. I think I got lucky to get this domain name which is **cruddur.fun** .

![39](img/week-6-7/week6-7%20(39).png) 

## Creating **Hosted zones**

So when we create the hosted zone it provides as the DNS or nameserver we have to take those DNS and put it on the DNS of the domain name from where you have purchased the domain name.

To took 5 min for me.

![40](img/week-6-7/week6-7%20(40).png)

# AWS Load Balancers

Elastic Load Balancing automatically distributes your incoming traffic across multiple targets, such as EC2 instances, containers, and IP addresses, in one or more Availability Zones. It monitors the health of its registered targets, and routes traffic only to the healthy targets. Elastic Load Balancing scales your load balancer as your incoming traffic changes over time. It can automatically scale to the vast majority of workloads.

Elastic Load Balancing supports the following load balancers: 

- Application Load Balancers
- Network Load Balancers
- Gateway Load Balancers
- Classic Load Balancers.

Created Load balancers

## AWS Application Load Balancer

We will be using AWS Application Load Balancer. An Application Load Balancer functions at the application layer, the seventh layer of the Open Systems Interconnection (OSI) model. After the load balancer receives a request, it evaluates the listener rules in priority order to determine which rule to apply and then selects a target from the target group for the rule action. You can configure listener rules to route requests to different target groups based on the content of the application traffic. Routing is performed independently for each target group, even when a target is registered with multiple target groups. You can configure the routing algorithm used at the target group level. The default routing algorithm is round robin; alternatively, you can specify the least outstanding requests routing algorithm.

You can add and remove targets from your load balancer as your needs change, without disrupting the overall flow of requests to your application. Elastic Load Balancing scales your load balancer as traffic to your application changes over time. Elastic Load Balancing can scale to the vast majority of workloads automatically.

You can configure health checks, which are used to monitor the health of the registered targets so that the load balancer can send requests only to the healthy targets.

### Creating the ALB

![41](img/week-6-7/week6-7%20(41).png)

## **Listeners for your Application Load Balancers**

Before you start using your Application Load Balancer, you must add one or more *listeners*
. A listener is a process that checks for connection requests, using the protocol and port that you configure. The rules that you define for a listener determine how the load balancer routes request to its registered targets.

![34](img/week-6-7/week6-7%20(34).png)

### Create 2 Listerers for Backend and Frontend

![38](img/week-6-7/week6-7%20(38).png)

# Target Group

Target groups route requests to one or more registered targets, such as EC2 instances, using the protocol and port number that you specify. You can register a target with multiple target groups. You can configure health checks on a per-target group basis. Health checks are performed on all targets registered to a target group that is specified in a listener rule for your load balancer.

Each target group is used to route requests to one or more registered targets. When you create each listener rule, you specify a target group and conditions. When a rule condition is met, traffic is forwarded to the corresponding target group. You can create different target groups for different types of requests. For example, create one target group for general requests and other target groups for requests to the microservices for your application. You can use each target group with only one load balancer.

### Created Target Group for Frontend and Backend

![21](img/week-6-7/week6-7%20(21).png)

# Everything is Ready

Now that everything is ready all things are on the please first let’s check for the health of the ECS

![22](img/week-6-7/week6-7%20(22).png)

It’s health that’s good.

### Check for the Backend

To check for the backend we will go the health-check route.

![23](img/week-6-7/week6-7%20(23).png)

Yes!! it’s working. Nocie

### Check For the Backend

So it is time to hit the domain name which is [cruddur.fun](http://cruddur.fun) 

![24](img/week-6-7/week6-7%20(24).png)

Yesssss!!!!!!!!! it working.

# Add Custome Network on Docker-compose file

We need to create a customer network for the docker-compose file so that every container can communicate with each other.

![25](img/week-6-7/week6-7%20(25).png)

We the docker network

![29](img/week-6-7/week6-7%20(29).png)

# Adding AWS XRay

First, we have added the x-ray to the task definition file for both the frontend and backend

### Then we will push those changes with AWS CLI

![26](img/week-6-7/week6-7%20(26).png)

### After that, we will build and push the images for both the frontend and backend.

![27](img/week-6-7/week6-7%20(27).png)

![28](img/week-6-7/week6-7%20(28).png)

### Now we will go check if x-ray is deployed or not

![31](img/week-6-7/week6-7%20(31).png)

![32](img/week-6-7/week6-7%20(32).png)

# **Container Insights**

Now we will enable the container insights for ECS so that we can get he log on CloudWatch

![33](img/week-6-7/week6-7%20(33).png)

# Summary

These 2 weeks are really nice we are getting close to our goals.

- Completed all the to-do lists.
- The most exciting part of this week was that I purchased a domain name which I Have never done before. I don’t know why it was so exciting but it was.
- The domain name I purchased is [cruddur.fun](http://cruddur.fun)
- So these weeks you introduced so many AWS functions and features I read about those on AWS docs. To understand how they work.
- I run into an error which is still not solved I’m trying to solve that as soon as possible.