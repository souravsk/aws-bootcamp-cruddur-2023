# Week 0 — Billing and Architecture

## Monolithic Architecture

A monolithic application is a software application that is built as a single, self-contained unit, where all the components are tightly coupled and run on a single platform.

**Q;-** **What are the advantages of a monolithic application?**
Monolithic applications are simpler to develop and deploy, and they have lower operational overhead compared to more complex distributed systems.

**Q:- What are the disadvantages of a monolithic application?**
Monolithic applications can become difficult to maintain and scale as they grow in size and complexity, and they can suffer from a lack of flexibility in terms of technology choices.

## Microservice  Architecture

A microservices architecture is an architectural style for building software applications as a collection of small, independent services that work together to form a larger application.

**Q:- What are the advantages of a microservices architecture?**
Microservices architectures offer better scalability, fault tolerance, and flexibility in terms of technology choices. They also enable teams to develop and deploy services independently, which can speed up development cycles.

**Q:-  What are the disadvantages of a microservices architecture?**
Microservices architectures are more complex to develop and deploy compared to monolithic applications. They also require additional overhead for managing and monitoring the different services that make up the application.

Reg

## Application Layers

- User interface
- Business Logic
- Data access

## Iron Triangle

The Iron Triangle is a project management concept that refers to the three constraints that are commonly considered to be the most important in determining the success or failure of a project. The three constraints are:

1. Time: Refers to the amount of time available to complete a project. The project needs to be completed within a specific timeframe, and any delays can have a significant impact on the project's success.


2. Cost: Refers to the budget available to complete a project. The project needs to be completed within the allocated budget, and any cost overruns can have a significant impact on the project's success.

3. Scope: Refers to the goals, deliverables, and features of a project. The project needs to meet the agreed-upon scope, and any changes or deviations from the scope can have a significant impact on the project's success.

# Architecting Your Cloud

## what is Good Architecture?

### Meet the requirement

- You have to meet or achieve the technical or business requirement

### Addresses the risks, assumptions and constraints

**Risks**:- Risks can prevent the project from being successful like Late Delivery, User Commitment

**Assumptions**:- Assumptions are factors held as true for the planning and implementation phases like the budget is approved and sufficient network bandwidth.

**Constraints:-** Constraints are policy or technical limitations for the project like Time, Budget.

## It’s Important to Develop a common Dictionary

- As a “Dumb Question”
- Play be-the-packet
- Document Everything

## What is TOGAF?

TOGAF is an architecture framework that provides the method and tools for assisting in the acceptance, production, use, and maintenance of an enterprise architecture. It is based on an iteration process model supported by best practices and a re-used set of existing architecture assets.

- The most popular framework for EA
- Common Dictionary of work to convey desired outcomes
- a meta-model for the creation of the underlying projects
- maps closely to the well-architecture tool

## AWS Well-Architecture Framework

- Workload = collection of resources and code the make up a cloud application
- ask the right question
- Naturally, fall into the R/R/A/C buckets
- a powerful tool in the architecture toolbelt

### The 6 Pillars:

1. Operation Excellence
2. Security
3. Reliability
4. Performance Efficiency
5. Cost Optimization
6. Sustainability

### Conceptual Diagram
![](img/week-0/week%200%20(1).png)

Link :- https://lucid.app/lucidchart/379b3727-6734-497c-86d3-2f8159a8c014/edit?viewport_loc=-1016%2C3%2C3605%2C1607%2C0_0&invitationId=inv_5a0ff381-553e-4cc5-bf37-610046c97317

### Logical Diagram
![](img/week-0/week%200%20(2).png)

Link:- https://lucid.app/lucidchart/379b3727-6734-497c-86d3-2f8159a8c014/edit?viewport_loc=-588%2C-30%2C3225%2C1437%2C91LAZ4vW6ftb&invitationId=inv_5a0ff381-553e-4cc5-bf37-610046c97317


# AWS Cloud Security Best Practices

## What is Cloud Security?

Cybersecurity protects the data, applications and services associated with the cloud environments from both external and internal security threats.

In simple terms when you host your application on a cloud platform and the job of cloud security is to protect your data and application from any threats.

**Why We care about cloud security**

- it Reduces the Impact of a breach
- Protecting networks, applications, and services in cloud environments against malicious data theft
- Reducing the human error responsible for data leaks.

**Cloud Security need Practice**

- Just having the certification is not enough you need to practice because it is complex.
- Bad hackers are improving their skill

## AWS Organizations

- Management  Account
- Automate vending Accounts with a Designated owner for each AWS Account

![](img/week-0/week%200%20(5).png)
## AWS Cloud Trail

- Monitor Data Security and Residence
- Understand the region vs Availability zone vs Global Services Concepts
- audit logs for IR/Forensics

## AWS IAM

AWS IAM stands for Amazon Web Services Identity and Access Management, which is a service provided by AWS for managing users, groups, and permissions within an AWS account. Some short answers related to AWS IAM are:

1. **What is AWS IAM?**

AWS IAM is a service provided by AWS for managing access to AWS resources.
2. **What are the benefits of using AWS IAM?**

Using AWS IAM allows you to manage access to AWS resources, enforce security policies, and audit access to resources.
![](img/week-0/week%200%20(7).png)

3. **What are IAM users?**

IAM users are entities within an AWS account that represent people, applications, or services that interact with AWS resources.
![](img/week-0/week%200%20(7).png)

4. **What are IAM groups?**

IAM groups are collections of IAM users that share the same permissions to access AWS resources.
![](img/week-0/week0(14).png)

5. **What are IAM roles?**

IAM roles are a way to grant temporary permissions to an entity, such as an AWS service or an IAM user from another AWS account.
![](img/week-0/week%200%20(8).png)

6. **What are IAM policies?**

IAM policies are documents that define permissions for IAM users, groups, and roles. Policies are written in JSON and specify what actions are allowed or denied for specific AWS resources.
![](img/week-0/week0(13).png)

## AWS Organization SCP

AWS Organization SCPs are policies that allow you to centrally manage permissions for multiple AWS accounts in an AWS organization.

**Q. How do AWS Organization SCPs work?**

AWS Organization SCPs are applied at the root level of an AWS organization and can be used to control what actions are allowed or denied for accounts or groups of accounts within the organization.

**Q. What can be controlled using AWS Organization SCPs?**

Using AWS Organization SCPs, you can control access to specific AWS services, API actions, and resources. You can also set conditions on when actions are allowed or denied, such as by IP address or time of day.

**Q. How are AWS Organization SCPs different from IAM policies?**

While IAM policies control access to resources within a single AWS account, AWS Organization SCPs allow you to control access across multiple accounts within an AWS organization.

**Q. How do you create and manage AWS Organization SCPs?**

AWS Organization SCPs are created and managed in the AWS Organizations console or using the AWS Organizations API. You can apply SCPs to individual accounts or groups of accounts within an organization, and you can use the AWS Organizations policy simulator to test your policies before applying them.

### Use CloudShell, Generate AWS Credentials, Installed AWS CLI

![](img/week-0/week%200%20(11).png)

![](img/week-0/week%200%20(12).png)

### Create a Billing Alarm

![](img/week-0/week%200%20(6).png)

![](img/week-0/week%200%20(4).png)

### Create a Budget

![](img/week-0/week%200%20(3).png)