# IAM -- Governance

| Topic | Meaning |
| --- | --- |
| IAM | Controls who can access AWS resources and which actions they can perform. |
| Users | Identities for people or applications; can have console or API access. |
| Groups | Collections of users that share policies; roles are not group members. |
| Roles | Assumed identities providing temporary credentials to users or workloads. |
| Policies | JSON rules that allow or deny actions on resources, optionally with conditions. |
| Permissions | Effective access depends on applicable policies; an explicit deny overrides an allow. |
| Least privilege | Grant only the actions and resources needed for a task. |
| Best practices | Prefer federation and temporary role credentials, enable MFA, protect root, and review unused access. |
| Use cases | Team access, EC2 access to S3, and cross-account administration. |

Sources: [AWS documentation 1](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html), [AWS documentation 2](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html).
