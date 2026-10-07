# S3 -- Storage

| Topic | Meaning |
| --- | --- |
| S3 | Object storage for files, backups, logs, and data lakes. |
| Buckets | Containers for objects; this demo uses a general-purpose bucket with a globally unique name. |
| Objects | Data plus metadata, identified by a key inside a bucket. |
| Storage classes | Standard for frequent access, Intelligent-Tiering for changing access, IA for infrequent access, and Glacier classes for archives. |
| Versioning | Keeps multiple object versions for recovery from overwrites or deletions. |
| Lifecycle policies | Transition objects to other storage classes or expire objects and versions. |
| Encryption | New uploads use server-side encryption by default; SSE-KMS adds KMS key controls. |
| Bucket policies | Resource policies defining access to the bucket and objects; keep public access blocked unless explicitly needed. |
| Use cases | Backups, static assets, artifacts, analytics datasets, and archives. |

Sources: [AWS documentation 1](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html).
