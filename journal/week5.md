# Week 5 - NoSQL and Caching

# NoSQL

NoSQL is a type of database management system (DBMS) that is designed to handle and store large volumes of unstructured and semi-structured data. Unlike traditional relational databases that use tables with pre-defined schemas to store data, NoSQL databases use flexible data models that can adapt to changes in data structures and are capable of scaling horizontally to handle growing amounts of data.

The term NoSQL originally referred to “non-SQL” or “non-relational” databases, but the term has since evolved to mean “not only SQL,” as NoSQL databases have expanded to include a wide range of different database architectures and data models.

### NoSQL databases are generally classified into four main categories:

1. Document databases: These databases store data as semi-structured documents, such as JSON or XML, and can be queried using document-oriented query languages.
2. Key-value stores: These databases store data as key-value pairs, and are optimized for simple and fast read/write operations.
3. Column-family stores: These databases store data as column families, which are sets of columns that are treated as a single entity. They are optimized for fast and efficient querying of large amounts of data.
4. Graph databases: These databases store data as nodes and edges, and are designed to handle complex relationships between data.
5. NoSQL databases are often used in applications where there is a high volume of data that needs to be processed and analyzed in real-time, such as social media analytics, e-commerce, and gaming. They can also be used for other applications, such as content management systems, document management, and customer relationship management.

So we are going to use DynamoDB which is a nosql database.

# DynamoDB

[DynamoDB](https://aws.amazon.com/dynamodb/) is a hosted NoSQL database offered by Amazon Web Services (AWS). It offers:

- *reliable performance* even as it scales;
- a *managed experience*, so you won't be SSH-ing into servers to upgrade the crypto libraries;
- a *small, simple API* allowing for simple key-value access as well as more advanced query patterns.

DynamoDB is a particularly good fit for the following use cases:

**Applications with large amounts of data and strict latency requirements**. As your amount of data scales, JOINs and advanced SQL operations can slow down your queries. With DynamoDB, your queries have predictable latency up to any size, including over 100 TBs!

**Serverless applications using AWS Lambda**. [AWS Lambda](https://aws.amazon.com/lambda/) provides auto-scaling, stateless, ephemeral computing in response to event triggers. DynamoDB is accessible via an HTTP API and performs authentication & authorization via IAM roles, making it a perfect fit for building Serverless applications.

**Data sets with simple, known access patterns**. If you're generating recommendations and serving them to users, DynamoDB's simple key-value access patterns make it a fast, reliable choice.

## Tables, Items, and Attributes

Tables, items, and attributes are the core building blocks of DynamoDB.

A *table* is a grouping of data records. For example, you might have a Users table to store data about your users, and an Orders table to store data about your users' orders. This concept is similar to a table in a relational database or a collection in MongoDB.

An *item* is a single data record in a table. Each item in a table is uniquely identified by the stated [primary key](https://www.dynamodbguide.com/key-concepts#primary-key) of the table. In your Users table, an item would be a particular User. An item is similar to a row in a relational database or a document in MongoDB.

*Attributes* are pieces of data attached to a single item. This could be a simple Age attribute that stores the age of a user. An attribute is comparable to a column in a relational database or a field in MongoDB. DynamoDB does not require attributes on items except for attributes that make up your [primary key](https://www.dynamodbguide.com/key-concepts#primary-key).

## Primary Key

Each item in a table is uniquely identified by a primary key. The primary key definition must be defined at the creation of the table, and the primary key must be provided when inserting a new item.

There are two types of primary key: a **simple primary key** made up of just a partition key, and a **composite primary key** made up of a partition key and a sort key.

Using a **simple primary key** is similar to standard key-value stores like Memcached or accessing rows in a SQL table by a primary key. One example would be a Users table with a Username primary key.

The **composite primary key** is more complex. With a composite primary key, you specify both a partition key and a sort key. The sort key is used to (wait for it) *sort* items with the same partition. One example could be an Orders table for recording customer orders on an e-commerce site. The partition key would be the CustomerId, and the sort key would be the OrderId.

## Secondary Indexes

The primary key uniquely identifies an item in a table, and you may make queries against the table using the primary key. However, sometimes you have additional access patterns that would be inefficient with your primary key. DynamoDB has the notion of **secondary indexes** to enable these additional access patterns.

The first kind of secondary index is a **local secondary index**. A local secondary index uses the same partition key as the underlying table but a different sort key. To take our Order table example from the previous section, imagine you wanted to quickly access a customer's orders in descending order of the amount they spent on the order. You could add a local secondary index with a partition key of CustomerId and a sort key of Amount, allowing for efficient queries on a customer's orders by amount.

The second kind of secondary index is a **global secondary index**. A global secondary index can define an entirely different primary key for a table. This could mean setting an index with just a partition key for a table with a composite primary key. It could also mean using completely different attributes to populate a partition key and sort key. With the Order example above, we could have a global secondary index with a partition key of OrderId so we could retrieve a particular order without knowing the CustomerId that placed the order.

Secondary indexes are a complex topic but are extremely useful in getting the most out of DynamoDB. Check out the section on [secondary indexes](https://www.dynamodbguide.com/secondary-indexes) for a deeper dive.

## Read and Write Capacity

When you use a database like MySQL, Postgres, or MongoDB, you provision a particular server to run your database. You'll need to choose your instance size -- how many CPUs do you need, how much RAM, how many GBs of storage, etc.

Not so with DynamoDB. Instead, you provision *read and write capacity units*. These units allow a given number of operations per second. This is a fundamentally different pricing paradigm than the instance-based world -- pricing can more closely reflect actual usage.

DynamoDB also has [autoscaling](https://www.dynamodbguide.com/autoscaling) of your read and write capacity units. This makes it much easier to scale your application up during peak times while saving money by scaling down when your users are asleep.

# DynamoDB Utility Scrips

## Implement Schema Load Script

we need all those lists of the user that is stored in the AWS Cognito. So we have created a bash script that will collect or get user data from AWS Cognito and then return it.

![](img/week-5/week5%20(1).png)

## Implement Seed Script

In this script, we will feed the conversation data to the table.

![](img/week-5/week5%20(4).png)

## Implement Scan Script

This script helps to scan and get the data that is stored on the table.

![](img/week-5/week5%20(5).png)

## Implement List-table Script

This Script will let's as view whether the table is created or not.

![](img/week-5/week5%20(2).png)

## Implement Drop Script

This Script will drop the table.

![](img/week-5/week5%20(3).png)

## Implement Pattern Scripts for Read and List Conversations

This will list the conversation and whatever happens on that.

![](img/week-5/week5%20(7).png)

## Implement Pattern Scripts for Read and get Conversations

This will show all the conversations that we have stored with the seed script, in this case, we have hard-coded the conversation but when we will deploy the code to the lambda function we will store real conversations.

![](img/week-5/week5%20(6).png)

## Implement List user

This script will list the user who has created an account on the website or signed up for the website. 

![](img/week-5/week5%20(8).png)

# Implement Conversations with DynamoDB

## Implement Update Cognito ID Script for Postgres Database

So With the help of this script, we can get all the user detail which is stored on Cognito specifying the Congito ID

![](img/week-5/week5%20(9).png)

## Implement (Pattern A) Listing Messages in Message Group into Application

First, we will list the conversation that was hard-coded the so that we will get to know that everything is working as it should be.

![](img/week-5/week5%20(10).png)

## Implement (Pattern B) Listing Messages Group into the Application

Now what we have to do is to create a DynamoDB database in our local machine with the help of the script that we already have created and then we will create a table and we will seed all the conversation data to that table after doing so we will able to see the message group.

![](img/week-5/week5%20(11).png)

## Implement (Pattern C) Creating a Message for an existing Message Group into the Application

Now we have to create the message in the existing group I then created a message that message should be stored on the DynamoDB table where all the conversations are already being stored. 

![](img/week-5/week5%20(12).png)

## Implement (Pattern D) Creating a Message for a new Message Group into Application

Now we have to create a new message to a new message group so what we do is will created a new user then we will try to create a message group and see.

![](img/week-5/week5%20(13).png)

# DynamoDB Stream

So in the preview section whatever we have to do it's all on the local machine now it’s time to upstream the data to AWS DynamoDB. 

## Create the DynamoDB Table

So we have to create a DynamoDB Table to do so we can use the website but we don’t have to because the have the script that `Schema-load` this create will create the table on AWS we just have to run the script with `prod` command.

![](img/week-5/week5%20(15).png)

## Create Endpoints

Now we have to create the connection with the DynamoDB and to do that we will use Endpoint which is available on VPC. Endpoints help to connect DynamoDB with the application.

![](img/week-5/week5%20(14).png)

## Create Lambda Function

Now create a Lambda function that will perform the operation.

![](img/week-5/week5%20(18).png)

![](img/week-5/week5%20(19).png)

## Implement (Pattern E) Updating a Message Group using DynamoDB Streams

Now that the last thing left is to run the code and show whether everything is working perfectly or not we will state the docker-compose file then we will go to the frontend page login to the account then go to the message section and then go to the URL section make some change to URL to access a user handle. To do so `messages/new/goku` this is how we do. 

![](img/week-5/week5%20(16).png)

![](img/week-5/week5%20(7).png)