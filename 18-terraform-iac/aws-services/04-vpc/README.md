# VPC -- Networking

| Topic | Meaning |
| --- | --- |
| VPC | A logically isolated virtual network in an AWS Region. |
| CIDR | An IP address range, such as 10.0.0.0/16. |
| Subnets | Address ranges inside the VPC; each subnet belongs to one Availability Zone. |
| Route tables | Rules selecting where traffic for a destination is sent. |
| Internet Gateway | Connects a VPC to the internet when addressing and routes allow it. |
| NAT Gateway | Lets private IPv4 resources initiate external connections; public NAT also needs an internet gateway route. |
| Security Groups | Stateful allow rules applied to network interfaces. |
| Network ACLs | Stateless subnet rules supporting allow and deny; return traffic needs matching rules. |
| Public/private subnet | A public subnet has a direct route to an internet gateway; a private subnet does not. |

Sources: [AWS documentation 1](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html), [AWS documentation 2](https://docs.aws.amazon.com/vpc/latest/userguide/configure-subnets.html).
