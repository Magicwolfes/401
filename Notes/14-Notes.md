# Intrusion Detection and Prevention Systems (IDS/IPS)

## List 2 differences between firewalls and an IDS?
Firewalls are designed to prevent unauthorized access to a network, while IDS are designed to detect and respond to potential security breaches that have already occurred.
Firewalls are typically placed at the perimeter of a network, between the internal network and the external Internet, to filter incoming and outgoing traffic. IDS can be placed at various points within the network to monitor and analyze traffic, such as at the network perimeter, on critical servers or endpoints, or within specific network segments.

## Under what circumstances would you choose a network-based IDS over a host-based IDS?
Network-based IDS are more suited to monitor large networks with multiple entry points and a diverse range of endpoints.
In some cases, an organization may not have complete control over all endpoints on their network, such as with bring-your-own-device (BYOD) policies or third-party vendors accessing the network. In these scenarios, network-based IDS can be more effective in detecting threats, as they are not reliant on the security controls of individual endpoints.
Network-based IDS solutions can be less expensive than host-based IDS, especially when considering the number of endpoints that need to be monitored. 

## Name 3 major drawbacks of a NIDS?
A NIDS can only detect and analyze traffic that passes through the network segment where it is deployed. This means that it may miss threats that are present on endpoints that are not monitored by the NIDS, or that use encryption or other techniques to evade detection.

NIDS generate a large number of alerts based on traffic patterns, which can be overwhelming for security teams to triage and investigate.

NIDS can generate false positives, meaning that they identify normal traffic as suspicious or malicious