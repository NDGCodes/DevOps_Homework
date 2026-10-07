# Session 18: Terraform & Infrastructure as Code

Student: Nishant Dasgupta  
Roll number: **24bcs10451**

## Task 1: S3 demo

## Execution screenshots

Init, fmt, and validation succeeded.

![Init and validation](evidence/terraform-init-validate_24bcs10451.png)

The apply preview showed one resource to add; apply created the bucket successfully.

![Plan and apply](evidence/terraform-apply_24bcs10451.png)

`terraform show` displays the created bucket and its tags.

![Terraform state](evidence/terraform-show_24bcs10451.png)

Outputs show the bucket name, ARN, and Mumbai region.

![Terraform outputs](evidence/terraform-output_24bcs10451.png)

The bucket was visible in the AWS S3 console.

![S3 console](evidence/aws-s3-console_24bcs10451.png)

Terraform confirmed destruction of the lab bucket.

![Bucket destruction](evidence/terraform-destroy_24bcs10451.png)

## Task 2: AWS research

- [IAM](aws-services/01-iam/README.md)
- [EC2](aws-services/02-ec2/README.md)
- [S3](aws-services/03-s3/README.md)
- [VPC](aws-services/04-vpc/README.md)
- [DynamoDB & RDS](aws-services/05-dynamodb-rds/README.md)
