# Terraform S3 Demo

I created one S3 bucket using the supplied demo and removed invalid `type` arguments from outputs.

## Environment

I executed the workflow in AWS CloudShell, Mumbai (`ap-south-1`), with Terraform 1.14.0 and AWS provider 6.66.0. Bucket name is recorded in [terraform.tfvars](terraform.tfvars).

Provider downloads used temporary storage to avoid CloudShell's home-directory limit:

```bash
export TF_DATA_DIR=/tmp/session17-terraform-data
```

The supplied `force_destroy = true` deletes bucket contents during destroy.

## Workflow

I executed these commands:

```bash
terraform init
terraform fmt
terraform validate
terraform plan
terraform apply
terraform show
terraform output
terraform destroy
```



| Command | Purpose |
| --- | --- |
| init | Downloads the AWS provider and initializes the project. |
| fmt | Formats Terraform files. |
| validate | Checks configuration syntax and provider schema. |
| plan | Previews creation of the bucket. |
| apply | Creates the bucket in AWS. |
| show | Displays Terraform state after creation. |
| output | Prints bucket name, ARN, and region. |
| destroy | Deletes the lab bucket and its contents. |

[Execution screenshots](../README.md#execution-screenshots) are in the main assignment README.
