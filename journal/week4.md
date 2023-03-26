# Week 4 — Postgres and RDS

# What is Relational Database Service (RDS)

Amazon Relational Database Service (Amazon RDS) is a web service that makes it easier to set up, operate, and scale a relational database in the AWS Cloud. It provides cost-efficient, resizable capacity for an industry-standard relational database and manages common database administration tasks.

## **Amazon RDS for PostgreSQL**

Amazon RDS supports DB instances running several versions of PostgreSQL

You can create DB instances and DB snapshots, point-in-time restores and backups. DB instances running PostgreSQL support Multi-AZ deployments, read replicas, and Provisioned IOPS, and can be created inside a virtual private cloud (VPC). You can also use Secure Socket Layer (SSL) to connect to a DB instance running PostgreSQL.

Amazon RDS for PostgreSQL is compliant with many industry standards. For example, you can use Amazon RDS for PostgreSQL databases to build HIPAA-compliant applications and to store healthcare-related information. This includes storage for protected health information (PHI) under a completed Business Associate Agreement (BAA) with AWS. Amazon RDS for PostgreSQL also meets Federal Risk and Authorization Management Program (FedRAMP) security requirements. Amazon RDS for PostgreSQL has received a FedRAMP Joint Authorization Board (JAB) Provisional Authority to Operate (P-ATO) at the FedRAMP HIGH Baseline within the AWS GovCloud (US) Regions.

Created Database using `Schema.sql`

![1](img/week-4/week4%20(1).png)

Stopped the Postgres so that it won’t charge when it is not being used.

![2](img/week-4/week4%20(2).png)

Set the env for the database so that it can be used to get connected with the database.

![3](img/week-4/week4%20(3).png)

# What is Sed

SED command in UNIX stands for stream editor and it can perform lots of functions on file like searching, finding and replacing, insertion or deletion. Though most common use of the SED command in UNIX is for a substitution or for find and replace. By using SED you can edit files even without opening them, which is a much quicker way to find and replace something in a file, than first opening that file in VI Editor and then changing it.

- SED is a powerful text stream editor. Can do insertion, deletion, search and replace(substitution).
- SED command in UNIX supports regular expression which allows it to perform complex pattern matching.

Now I have created the different bash files for create, drop and schema 

![4](img/week-4/week4%20(4).png)

## db-create

![6](img/week-4/week4%20(6).png)

## db-drop

![5](img/week-4/week4%20(5).png)

## db-schema-load

![8](img/week-4/week4%20(8).png)

## db-seed

![10](img/week-4/week4%20(10).png)

This is the table that has users and activities.

![9](img/week-4/week4%20(9).png)

### DATABASE EXPLORER

Used the database explorer to see view the connection has formed properly or not.

![11](img/week-4/week4%20(11).png)

![12](img/week-4/week4%20(12).png)

## db-sessions

![13](img/week-4/week4%20(13).png)

## db-setup

![14](img/week-4/week4%20(14).png)

Now we are able to see the seed that we have inputted

![15](img/week-4/week4%20(15).png)

![16](img/week-4/week4%20(16).png)

# Cognito Post Confirmation

First, we have to form a connection with AWS RDS

![17](img/week-4/week4%20(17).png)

Now we will create an AWS Lambda Function 

![19](img/week-4/week4%20(19).png)

we need a VPC so that we can get connected with Lambda. we will use the  AWS CLI command. 

![18](img/week-4/week4%20(18).png)

![22](img/week-4/week4%20(22).png)

Now we will add Lambda Triggers

![21](img/week-4/week4%20(21).png)

![20](img/week-4/week4%20(20).png)

Now everything is set then let’s create any user.

the most annoying error is this one it took me a day to figure it out.

![23](img/week-4/week4%20(23).png)

you can see how many times have to delete the user from the user pool

![24](img/week-4/week4%20(24).png)

So after solving this error there is another error that annoys me too much but thanks to the discord community there help me to finger it out the problem.

![26](img/week-4/week4%20(26).png)

But after a long waiting for help, I get the help and I solve the issue.

![25](img/week-4/week4%20(25).png)

![28](img/week-4/week4%20(28).png)

![27](img/week-4/week4%20(27).png)

# Creating Activities

We have to write so much code in the section so the when user writes something that needs to be stored in the table name `activities`

But I’m stuck right now on this one error.
## Worked

it is working now the problem was on the user name. 

Create a crud as  you can see.
![](img/week-4/week4%20(29).png)

Now it is also on the database

![](img/week-4/week4%20(30).png)