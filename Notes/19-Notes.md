# Cloud Detective Controls

## What are some of the IoCs that GuardDuty can detect?
Unauthorized access, Cryptocurrency mining and Malicious activity.

## What are some of the data sources which GuardDuty can use?

AWS CloudTrail logs: CloudTrail logs contain a record of all AWS API calls made within your AWS environment, and GuardDuty can analyze these logs to detect potential security threats.

Amazon VPC Flow Logs: VPC Flow Logs contain information about the traffic flowing through your VPCs, including the source and destination IP addresses, ports, and protocols. GuardDuty can analyze this data to detect network anomalies and potential security threats.

DNS logs: GuardDuty can analyze DNS logs to detect potential DNS-related threats, such as DNS hijacking or domain fronting.

## How does GuardDuty use access behavior to spot potential malicious activity?
GuardDuty uses machine learning algorithms to analyze the access behavior of users within an AWS environment. This includes analyzing patterns of access to resources, such as the frequency of access, the time of day when access occurs, and the type of resources being accessed.
GuardDuty analyzes the IP addresses accessing your AWS environment to determine whether they have a history of malicious activity. This includes checking against known lists of malicious IP addresses and analyzing the reputation of IP addresses based on their historical behavior.
GuardDuty looks for anomalies in access behavior that may indicate potential security threats. This includes looking for patterns of access that deviate from normal behavior, such as access from unusual locations or at unusual times.