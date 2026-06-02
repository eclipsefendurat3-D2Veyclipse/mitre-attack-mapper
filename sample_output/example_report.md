Loading dataset...
Dataset loaded. Attack patterns found: 858
Searching for: phishing
Found 119 technique(s) matching: phishing

Technique:   Exploitation for Defense Impairment
ID:          T1687
Reference:   https://attack.mitre.org/techniques/T1687
Description: Adversaries may exploit vulnerabilities in security software, infrastructure, or defensive components to degrade, disable, or otherwise continue to impair their ability to prevent, detect, or respond to malicious activity. 
 
Adversaries may exploit a system or application vulnerability to directly ...

Technique:   Gather Victim Host Information
ID:          T1592
Reference:   https://attack.mitre.org/techniques/T1592
Description: Adversaries may gather information about the victim's hosts that can be used during targeting. Information about hosts may include a variety of details, including administrative data (ex: name, assigned IP, functionality, etc.) as well as specifics regarding its configuration (ex: operating system, ...

Technique:   Digital Certificates
ID:          T1596.003
Reference:   https://attack.mitre.org/techniques/T1596/003
Description: Adversaries may search public digital certificate data for information about victims that can be used during targeting. Digital certificates are issued by a certificate authority (CA) in order to cryptographically verify the origin of signed content. These certificates, such as those used for encryp...

Technique:   Purchase Technical Data
ID:          T1597.002
Reference:   https://attack.mitre.org/techniques/T1597/002
Description: Adversaries may purchase technical information about victims that can be used during targeting. Information about victims may be available for purchase within reputable private sources and databases, such as paid subscriptions to feeds of scan databases or other data aggregation services. Adversarie...

Technique:   Artificial Intelligence
ID:          T1588.007
Reference:   https://attack.mitre.org/techniques/T1588/007
Description: Adversaries may obtain access to generative artificial intelligence tools, such as large language models (LLMs), to aid various techniques during targeting. These tools may be used to inform, bolster, and enable a variety of malicious tasks, including conducting [Reconnaissance](https://attack.mitre...
Loading dataset...
Dataset loaded. Attack patterns found: 858
Searching for: brute force
Found 15 technique(s) matching: brute force

Technique:   VNC
ID:          T1021.005
Reference:   https://attack.mitre.org/techniques/T1021/005
Description: Adversaries may use [Valid Accounts](https://attack.mitre.org/techniques/T1078) to remotely control machines using Virtual Network Computing (VNC).  VNC is a platform-independent desktop sharing system that uses the RFB (“remote framebuffer”) protocol to enable users to remotely control another comp...

Technique:   Password Guessing
ID:          T1110.001
Reference:   https://attack.mitre.org/techniques/T1110/001
Description: Adversaries with no prior knowledge of legitimate credentials within the system or environment may guess passwords to attempt access to accounts. Without knowledge of the password for an account, an adversary may opt to systematically guess the password using a repetitive or iterative mechanism. An ...

Technique:   LLMNR/NBT-NS Poisoning and Relay
ID:          T1171
Reference:   https://attack.mitre.org/techniques/T1171
Description: Link-Local Multicast Name Resolution (LLMNR) and NetBIOS Name Service (NBT-NS) are Microsoft Windows components that serve as alternate methods of host identification. LLMNR is based upon the Domain Name System (DNS) format and allows hosts on the same local link to perform name resolution for other...

Technique:   Private Keys
ID:          T1145
Reference:   https://attack.mitre.org/techniques/T1145
Description: Private cryptographic keys and certificates are used for authentication, encryption/decryption, and digital signatures. (Citation: Wikipedia Public Key Crypto)

Adversaries may gather private keys from compromised systems for use in authenticating to [Remote Services](https://attack.mitre.org/techni...

Technique:   Private Keys
ID:          T1552.004
Reference:   https://attack.mitre.org/techniques/T1552/004
Description: Adversaries may search for private key certificate files on compromised systems for insecurely stored credentials. Private cryptographic keys and certificates are used for authentication, encryption/decryption, and digital signatures.(Citation: Wikipedia Public Key Crypto) Common key and certificate...
Loading dataset...
Dataset loaded. Attack patterns found: 858
Searching for: lateral movement
Found 46 technique(s) matching: lateral movement

Technique:   Scheduled Task
ID:          T1053.005
Reference:   https://attack.mitre.org/techniques/T1053/005
Description: Adversaries may abuse the Windows Task Scheduler to perform task scheduling for initial or recurring execution of malicious code. There are multiple ways to access the Task Scheduler in Windows. The [schtasks](https://attack.mitre.org/software/S0111) utility can be run directly on the command line, ...

Technique:   Container and Resource Discovery
ID:          T1613
Reference:   https://attack.mitre.org/techniques/T1613
Description: Adversaries may attempt to discover containers and other resources that are available within a containers environment. Other resources may include images, deployments, pods, nodes, and other information such as the status of a cluster.

These resources can be viewed within web applications such as t...

Technique:   OS Credential Dumping
ID:          T1003
Reference:   https://attack.mitre.org/techniques/T1003
Description: Adversaries may attempt to dump credentials to obtain account login and credential material, normally in the form of a hash or a clear text password. Credentials can be obtained from OS caches, memory, or structures.(Citation: Brining MimiKatz to Unix) Credentials can then be used to perform [Latera...

Technique:   Bypass User Account Control
ID:          T1548.002
Reference:   https://attack.mitre.org/techniques/T1548/002
Description: Adversaries may bypass UAC mechanisms to elevate process privileges on system. Windows User Account Control (UAC) allows a program to elevate its privileges (tracked as integrity levels ranging from low to high) to perform a task under administrator-level permissions, possibly by prompting the user ...

Technique:   SID-History Injection
ID:          T1178
Reference:   https://attack.mitre.org/techniques/T1178
Description: The Windows security identifier (SID) is a unique value that identifies a user or group account. SIDs are used by Windows security in both security descriptors and access tokens. (Citation: Microsoft SID) An account can hold additional SIDs in the SID-History Active Directory attribute (Citation: Mi...
