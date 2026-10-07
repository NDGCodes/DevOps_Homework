# EC2 -- Compute

| Topic | Meaning |
| --- | --- |
| EC2 | Virtual servers called instances, with selectable CPU, memory, storage, and networking. |
| AMI | An operating-system and software image used to launch instances. |
| Instance types | Hardware profiles suited to general, compute, memory, or other workloads. |
| Key pairs | Public/private keys used for supported instance login methods; keep the private key secure. |
| Security Groups | Stateful allow rules controlling inbound and outbound traffic. |
| EBS | Persistent block volumes attached to instances; snapshots back them up. |
| Public/private IP | Public addresses enable internet addressing; private addresses serve internal networking. Routes and security rules still control reachability. |
| Lifecycle | Pending -> running -> stopping/stopped -> running, or shutting-down -> terminated. |
| Use cases | Web servers, build runners, batch processing, and self-managed services. |

Sources: [AWS documentation 1](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html), [AWS documentation 2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-lifecycle.html).
