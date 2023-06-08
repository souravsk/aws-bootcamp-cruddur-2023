# Week 9 — CI/CD with CodePipeline, CodeBuild and CodeDeploy

# AWS CodePipeline

AWS CodePipeline is a continuous delivery service you can use to model, visualize, and automate the steps required to release your software. You can quickly model and configure the different stages of a software release process. CodePipeline automates the steps required to release your software changes continuously.

Creating a code pipeline for our project

![1](img/week-9/week-9%20(1).png)

# AWS CodeBuild

AWS CodeBuild is a fully managed build service in the cloud. CodeBuild compiles your source code, runs unit tests, and produces artifacts that are ready to deploy. CodeBuild eliminates the need to provision, manage, and scale your own build servers. It provides prepackaged build environments for the most popular programming languages and build tools, such as Apache Maven, Gradle, and more. You can also fully customize build environments in CodeBuild to use your own build tools. CodeBuild scales automatically to meet peak build requests. You pay only for the build time you consume.

Now we have to create a code build to build the backend.

![2](img/week-9/week-9%20(2).png)

![3](img/week-9/week-9%20(3).png)

Now we have deployed the build yaml file it’s time to merge the main branch with the prod branch so it will trigger the code build and code pipeline.

![4](img/week-9/week-9%20(4).png)

![5](img/week-9/week-9%20(5).png)

![6](img/week-9/week-9%20(6).png)

Yes it build successfully Now to check it we can go to [api.cruddur.fun/api/health-check](http://api.cruddur.fun/api/health-check)

![7](img/week-9/week-9%20(7).png)

# Summary

This week is the easiest week ever so far. 

Completed all the to-do lists. 

So I have a lot of time to solve some of the bugs that are coming and fine-tune the project a little bit.