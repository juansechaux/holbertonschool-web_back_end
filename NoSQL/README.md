# NoSQL

## Table of Contents

1. [What is NoSQL?](#what-is-nosql)
2. [Difference between SQL and NoSQL](#difference-between-sql-and-nosql)
3. [ACID](#acid)
4. [Document Storage](#document-storage)
5. [Types of NoSQL Databases](#types-of-nosql-databases)
6. [Benefits of NoSQL Databases](#benefits-of-nosql-databases)
7. [Querying Information from a NoSQL Database](#querying-information-from-a-nosql-database)
8. [Insert/Update/Delete Operations in NoSQL](#insert-update-delete-operations-in-nosql)
9. [Using MongoDB](#using-mongodb)

## What is NoSQL? <a name="what-is-nosql"></a>

NoSQL, or "Not Only SQL," refers to a category of database systems that provide a flexible and scalable approach to data storage and retrieval. Unlike traditional relational databases (SQL), NoSQL databases can handle large amounts of unstructured or semi-structured data.

## Difference between SQL and NoSQL <a name="difference-between-sql-and-nosql"></a>

| SQL                           | NoSQL                         |
|-------------------------------|-------------------------------|
| Structured Query Language      | Not Only SQL                  |
| Relational databases           | Non-relational databases       |
| Fixed schema                  | Dynamic schema                |
| ACID transactions             | BASE (Basically Available, Soft state, Eventually consistent)      |
| Vertical scaling              | Horizontal scaling            |
| Examples: MySQL, PostgreSQL    | Examples: MongoDB, Cassandra  |

## ACID <a name="acid"></a>

ACID stands for Atomicity, Consistency, Isolation, and Durability. It is a set of properties that guarantee database transactions are processed reliably.

## Document Storage <a name="document-storage"></a>

Document storage is a NoSQL database model where data is stored in flexible, JSON-like documents. Each document can contain various key-value pairs, and the structure can evolve over time.

## Types of NoSQL Databases <a name="types-of-nosql-databases"></a>

1. **Document Stores:** MongoDB, CouchDB
2. **Key-Value Stores:** Redis, DynamoDB
3. **Column-Family Stores:** Cassandra, HBase
4. **Graph Databases:** Neo4j, ArangoDB

## Benefits of NoSQL Databases <a name="benefits-of-nosql-databases"></a>

1. **Scalability:** NoSQL databases are designed for horizontal scaling, allowing them to handle large amounts of data and traffic.
2. **Flexibility:** NoSQL databases can adapt to changes in data structure without requiring a predefined schema.
3. **Performance:** Improved read and write performance for certain types of applications.
4. **Cost-Effective:** NoSQL databases can often be more cost-effective for large-scale distributed systems.

## Querying Information from a NoSQL Database <a name="querying-information-from-a-nosql-database"></a>

Querying in NoSQL databases is specific to the type of database. For example, in MongoDB, queries are constructed using JSON-like documents.

Example MongoDB Query:
```javascript
db.collection.find({ key: "value" });
```

## Insert/Update/Delete Operations in NoSQL <a name="insert-update-delete-operations-in-nosql"></a>
Operations for inserting, updating, and deleting data vary across NoSQL databases. In MongoDB, for instance:

- `Insert:` db.collection.insertOne({ key: "value" });
- `Update:` db.collection.updateOne({ key: "oldValue" }, { $set: { key: "newValue" } });
- `Delete:` db.collection.deleteOne({ key: "value" });
## Using MongoDB <a name="using-mongodb"></a>
MongoDB is a popular document store NoSQL database. To use MongoDB:

1. Installation: [Download and Install MongoDB](https://www.mongodb.com/docs/manual/installation/)
2. Start MongoDB: Run mongod in the command line.
3. Connect to MongoDB: Use the MongoDB shell or a MongoDB driver for your programming language.

Example MongoDB Shell Commands:
```bash
mongo          # Start MongoDB shell
show dbs       # Show available databases
use mydb       # Switch to or create a database named 'mydb'
db.createCollection("mycollection")  # Create a collection
```