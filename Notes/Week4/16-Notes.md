# Cloud Identity and Access Management (IAM) with AWS


## What were the three commands used for the attack?
Get Credentials- First command, when executed obtained security credentials known as -WAF- Roleaccount (anIAMaccount) for an elevated role access AWS Web Application Firewall (WAF)  

List Buckets- Second command,when executed,used the security credentials -WAF- Role account to list files and folders(akaS3buckets)  

Download Files- Third command, when executed used the WAF-Role account to download files that were accessible by the credentials.


## What misconfiguration of AWS components allowed the attacker to access sensitive data?
The attacker identified a misconfigured WAF that enabled accessing the corresponding AWSEC2 instance/ ECStask *metadata* using Server-side Request Forgery (SSRF) and call the metadata service endpoint

## What are two of the AWS Governance practices that could have prevented such attack?
Don't allow EC2 instances to have IAM roles that allow attaching or replacing role policies in any production environment
Clean up unused cloud resources (especiallyEC2instancesandS3buckets)left over from prior development or production debugging efforts