# DynamoDB & RDS -- Databases

| Topic | Meaning |
| --- | --- |
| DynamoDB / NoSQL | Managed key-value and document database for flexible item data. |
| Tables / Items / Attributes | A table contains items (records); each item contains attributes (fields). |
| Partition key | Required primary-key component used to distribute and retrieve items. |
| Sort key | Optional second primary-key component that orders related items within a partition-key value. |
| DynamoDB use cases | Session stores, shopping carts, event data, and scalable key-based lookups. |
| RDS / Relational | Managed SQL databases with tables, relationships, and transactions. |
| Engines | Includes PostgreSQL, MySQL, MariaDB, Oracle, SQL Server, and Db2; engine availability varies by Region. Aurora is also part of the RDS service family. |
| DB instances | Compute and memory capacity hosting a database, with configurable storage. |
| Security | Use private networking, security groups, authentication, TLS, and encryption at rest. |
| Backups | Automated backups support point-in-time recovery; manual snapshots provide retained recovery points. |
| Multi-AZ | Provides availability and failover; traditional standby instances do not serve read traffic. |
| Read replicas | Separate replicas used to scale reads; replication is generally asynchronous. |
| RDS use cases | Transactional applications, business systems, and existing SQL workloads. |

Sources: [AWS documentation 1](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.CoreComponents.html), [AWS documentation 2](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html).
