# Week 3 — Decentralized Authentication

Decentralized authentication simply means that there is no central authority needed to verify your identity, i.e., decentralized identifiers. DIDs (Decentralized Identifiers) are a special type of identifier that allows for decentralized, verified digital identification.

# what is Cognito?

Amazon Cognito provides authentication, authorization, and user management for your web and mobile apps. Your users can sign in directly with a username and password, or through a third party such as Facebook, Amazon, Google or Apple.

The two main components of Amazon Cognito are user pools and identity pools. User pools are user directories that provide sign-up and sign-in options for your app users. Identity pools enable you to grant your users access to other AWS services. You can use identity pools and user pools separately or together.

## **Features of Amazon Cognito**

### **User pools**

A user pool is a user directory in Amazon Cognito. With a user pool, your users can sign in to your web or mobile app through Amazon Cognito, or federate through a third-party identity provider (IdP). Whether your users sign in directly or through a third party, all members of the user pool have a directory profile that you can access through an SDK.

### **Identity pools**

With an identity pool, your users can obtain temporary AWS credentials to access AWS services, such as Amazon S3 and DynamoDB. Identity pools support anonymous guest users, as well as the following identity providers that you can use to authenticate users for identity pools

## AWS Amplify

AWS Amplify provides services and libraries for web and mobile developers. With Amplify, you can build apps that integrate with backend environments that AWS services compose. To provision your backend environment, and to integrate AWS services with your client code, use the Amplify *framework*. The framework provides an interactive command line interface (CLI) that helps you configure AWS resources for features that are organized into categories. These categories include analytics, storage, and authentication, among many others. The framework also provides high-level SDKs and libraries for web and mobile platforms, including iOS, Android, and JavaScript. The JavaScript frameworks include React, React Native, Angular, Ionic, and Vue. Each of the SDKs and libraries includes authentication operations that you can use to implement the authentication workflows that Amazon Cognito drives. 

First, we will install AWS amplify on the frontend folder. using the command `npm i aws-amplify --save` 

### Setup Cognito User Pool

![](img/week-3/week3%20(1).png)

### Implement a Sign in Page with the help of UI

![](img/week-3/week3%20(2).png)

![](img/week-3/week3%20(3).png)

As we can see the showing is because it was not verified and the UI is not given the option to verify manually.
So we will create the user using the CLI command.

![](img/week-3/week3%20(4).png)

Yes! it worked. As you can see I have login successfully but as you can see on the left-hand side my name is not showing. We have to Implement the custom sign-in page.
let's sign out and implement the code

![](img/week-3/week3%20(5).png)

### Implement Custom Signup Page

Now we have implemented all the code and also I have to delete and created the user pool so many times because every time make some kind of mistake while creating it.

let's check does it work or not.

click on the join button.

![](img/week-3/week3%20(6).png)

Fill in all the details.

![](img/week-3/week3%20(19).png)

Yes!!!!! we got our email confirmation page. 

### Implement Custom Confirmation Page

![](img/week-3/week3%20(8).png)

Now let's go and check for the email did we receive and which content is the confirmation code.

![](img/week-3/week3%20(9).png)

Yes!! we did get the email now put the code

Let's login

![](img/week-3/week3%20(10).png)

![](img/week-3/week3%20(11).png)

Yes!!! it worked perfectly.

Now let's go to the AWS Cognito page and how it stores the data.

![](img/week-3/week3%20(12).png)

As you can see it has created its user name and the user is showing confirmed.

### Implement a Custom Recovery Page

Now we will work on the recovery page so that if someone got the password then they can recover their password.

Now page is read let's intern the email ID.

![](img/week-3/week3%20(13).png)

Let's again go to the email again and check whether we got the code or not.

![](img/week-3/week3%20(14).png)
 
 YES!!! Now let's enter the code and password to restore the account.

 ![](img/week-3/week3%20(15).png)

![](img/week-3/week3%20(16).png)

The UI need a little change but it is working.

Now login again and check whether the new password is working or not.

![](img/week-3/week3%20(17).png)

IT worked.

# Cognito JWT Server Side Verify

![](img/week-3/week3%20(18).png)

![](img/week-3/week3%20(19).png)

# UI Changes

![](img/week-3/week3%20(20).png)

# Amazon RDS PostGres

PostgreSQL has become the preferred open-source relational database for many enterprise developers and start-ups, powering leading business and mobile applications. Amazon RDS makes it easy to set up, operate, and scale PostgreSQL deployments in the cloud. With Amazon RDS, you can deploy scalable PostgreSQL deployments in minutes with cost-efficient and resizable hardware capacity. Amazon RDS manages complex and time-consuming administrative tasks such as PostgreSQL software installation and upgrades; storage management; replication for high availability and read throughput; and backups for disaster recovery.

![](img/week-3/week3%20(21).png)

![](img/week-3/week3%20(22).png)