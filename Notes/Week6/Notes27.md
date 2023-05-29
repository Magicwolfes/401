# Persistence
## What is one of the major advantages of PowerShell Empire?
PowerShell is a widely used scripting language on Windows systems, and Empire takes advantage of this by providing a comprehensive set of PowerShell modules and scripts. It allows attackers to utilize the extensive functionality of PowerShell for their offensive operations, including reconnaissance, lateral movement, privilege escalation, and data exfiltration.
Empire provides a modular architecture that allows users to easily extend its capabilities by creating or importing additional PowerShell modules and scripts. This flexibility enables security professionals to tailor their attacks to specific scenarios or environments, making it a versatile tool for offensive security operations.

## What are some of the APT groups that have been known to use PS Empire and into which step of the Cyber Kill Chain does the use of PS Empire fall?
APT29 (Cozy Bear): A Russian-sponsored APT group known for various high-profile cyber espionage campaigns. APT29 has been linked to the use of PowerShell Empire in their operations.
APT32 (OceanLotus): A threat group active in Southeast Asia, believed to be operating on behalf of the Vietnamese government. APT32 has reportedly utilized PowerShell Empire as part of their offensive toolkit.
APT33 (Elfin): An Iranian APT group known for conducting cyber espionage operations primarily targeting the aerospace and energy sectors. PowerShell Empire has been observed as one of the tools employed by APT33.

## What are the four main components needed to pull off an attack using PS Empire?
Listener: A listener is a component that listens for incoming connections from compromised systems. It acts as the command and control (C2) server within PowerShell Empire, allowing the attacker to communicate with and control compromised systems remotely. Listeners define the communication method, such as HTTP, HTTPS, DNS, or other covert channels, and provide an interface for managing the compromised hosts.

Stager: The stager is responsible for establishing an initial foothold on a targeted system. It acts as the initial implant or payload delivered to the compromised system, providing a backdoor for subsequent communication and control. PowerShell Empire offers various stager options, including PowerShell-based stagers, which leverage the capabilities of PowerShell to execute commands and establish a connection with the listener.

Modules: Modules in PowerShell Empire refer to the specific functionalities and capabilities that can be executed on compromised systems. These modules encompass a wide range of offensive operations, such as reconnaissance, privilege escalation, lateral movement, and exfiltration of data. PowerShell Empire comes with a collection of pre-built modules, but users can also create or import their own custom modules to extend its capabilities.

Agents: Agents are the instances of PowerShell Empire that are installed and run on compromised systems. Agents establish a connection to the listener and provide a means for executing modules and commands remotely. Once an agent is established on a compromised system, the attacker can issue commands, run modules, and perform various operations on that system.