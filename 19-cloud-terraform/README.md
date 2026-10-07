# Session 19: Cloud & Terraform in Action

Student: Nishant Dasgupta  
Roll number: **24bcs10451**

## Terraform project

## Architecture

```mermaid
flowchart TD
    TF[Terraform AWS provider] --> VPC[VPC: 10.20.0.0/16]
    VPC --> Subnet[Public subnet: 10.20.1.0/24]
    VPC --> IGW[Internet gateway]
    VPC --> RT[Public route table]
    RT -->|0.0.0.0/0| IGW
    RT --> Association[Route table association]
    Association --> Subnet
    VPC --> SG[Security group: HTTP 80 / HTTPS 443]
```

| Terraform concept | Project example |
| --- | --- |
| Provider | AWS `~> 6.0`, configured in `versions.tf`. |
| Variables | `aws_region` selects the region. |
| Resources | VPC, subnet, gateway, route table, association, security group. |
| Outputs | VPC ID/CIDR, subnet ID, and security group ID. |
| Dependencies | Resource references determine creation and deletion order. |
| State | Tracks resources in `terraform.tfstate`; inspected with `terraform state list`. |
| Commands | Plan previews changes; apply creates resources; destroy removes them. |

## AWS execution

I executed the project in AWS CloudShell, Mumbai (`ap-south-1`). Init selected AWS provider 6.67.0; validation passed and apply created all six resources.

I used the following Terraform commands:

```bash
terraform init
terraform fmt
terraform validate
terraform plan
terraform apply
terraform output
terraform state list
terraform show
terraform destroy
```

### Init, format, and validate

![Init and validate](evidence/terraform-init-validate_24bcs10451.png)

### Plan

![Planned resources](evidence/terraform-plan-details_24bcs10451.png)

![Six-resource plan](evidence/terraform-plan_24bcs10451.png)

### Apply and outputs

![Successful apply and resource outputs](evidence/terraform-apply_24bcs10451.png)

### VPC in AWS

![VPC name and available state](evidence/aws-vpc_24bcs10451.png)

![VPC CIDR](evidence/aws-vpc-cidr_24bcs10451.png)

![VPC properties](evidence/aws-vpc-properties_24bcs10451.png)

### Terraform state

All six managed resources are listed.

![Terraform state list](evidence/terraform-state_24bcs10451.png)

### Subnet and internet gateway

![Public subnet](evidence/aws-subnet_24bcs10451.png)

![Attached internet gateway](evidence/aws-internet-gateway_24bcs10451.png)

### Route table and resource map

The public route table is associated with the subnet. The resource map shows its internet gateway connection.

![Route table association](evidence/aws-route-table_24bcs10451.png)

![AWS architecture resource map](evidence/aws-resource-map_24bcs10451.png)

### Security group

Inbound rules allow TCP ports 80 and 443.

![HTTP and HTTPS rules](evidence/aws-security-group_24bcs10451.png)

### Destroy

All six lab resources were destroyed successfully.

![Successful destroy](evidence/terraform-destroy_24bcs10451.png)
