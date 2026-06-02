# MITRE ATT&CK Mapper — Search Results

**Search query:** lateral movement
**Techniques found:** 46

---

## 1. Scheduled Task

| Field | Value |
|---|---|
| **ID** | T1053.005 |
| **Tactic** | Execution |
| **Reference** | https://attack.mitre.org/techniques/T1053/005 |

**Description:** Adversaries may abuse the Windows Task Scheduler to perform task scheduling for initial or recurring execution of malicious code. There are multiple ways to access the Task Scheduler in Windows. The [schtasks](https://attack.mitre.org/software/S0111) utility can be run directly on the command line, or the Task Scheduler can be opened through the GUI within the Administrator Tools section of the Co...

---

## 2. Container and Resource Discovery

| Field | Value |
|---|---|
| **ID** | T1613 |
| **Tactic** | Discovery |
| **Reference** | https://attack.mitre.org/techniques/T1613 |

**Description:** Adversaries may attempt to discover containers and other resources that are available within a containers environment. Other resources may include images, deployments, pods, nodes, and other information such as the status of a cluster.

These resources can be viewed within web applications such as the Kubernetes dashboard or can be queried via the Docker and Kubernetes APIs.(Citation: Docker API)(...

---

## 3. OS Credential Dumping

| Field | Value |
|---|---|
| **ID** | T1003 |
| **Tactic** | Credential Access |
| **Reference** | https://attack.mitre.org/techniques/T1003 |

**Description:** Adversaries may attempt to dump credentials to obtain account login and credential material, normally in the form of a hash or a clear text password. Credentials can be obtained from OS caches, memory, or structures.(Citation: Brining MimiKatz to Unix) Credentials can then be used to perform [Lateral Movement](https://attack.mitre.org/tactics/TA0008) and access restricted information.

Several of ...

---

## 4. Bypass User Account Control

| Field | Value |
|---|---|
| **ID** | T1548.002 |
| **Tactic** | Privilege Escalation |
| **Reference** | https://attack.mitre.org/techniques/T1548/002 |

**Description:** Adversaries may bypass UAC mechanisms to elevate process privileges on system. Windows User Account Control (UAC) allows a program to elevate its privileges (tracked as integrity levels ranging from low to high) to perform a task under administrator-level permissions, possibly by prompting the user for confirmation. The impact to the user ranges from denying the operation under high enforcement to...

---

## 5. SID-History Injection

| Field | Value |
|---|---|
| **ID** | T1178 |
| **Tactic** | Privilege Escalation |
| **Reference** | https://attack.mitre.org/techniques/T1178 |

**Description:** The Windows security identifier (SID) is a unique value that identifies a user or group account. SIDs are used by Windows security in both security descriptors and access tokens. (Citation: Microsoft SID) An account can hold additional SIDs in the SID-History Active Directory attribute (Citation: Microsoft SID-History Attribute), allowing inter-operable account migration between domains (e.g., all...

---

## 6. Databases

| Field | Value |
|---|---|
| **ID** | T1213.006 |
| **Tactic** | Collection |
| **Reference** | https://attack.mitre.org/techniques/T1213/006 |

**Description:** Adversaries may leverage databases to mine valuable information. These databases may be hosted on-premises or in the cloud (both in platform-as-a-service and software-as-a-service environments). 

Examples of databases from which information may be collected include MySQL, PostgreSQL, MongoDB, Amazon Relational Database Service, Azure SQL Database, Google Firebase, and Snowflake. Databases may inc...

---

## 7. Additional Cloud Roles

| Field | Value |
|---|---|
| **ID** | T1098.003 |
| **Tactic** | Persistence |
| **Reference** | https://attack.mitre.org/techniques/T1098/003 |

**Description:** An adversary may add additional roles or permissions to an adversary-controlled cloud account to maintain persistent access to a tenant. For example, adversaries may update IAM policies in cloud-based environments or add a new global administrator in Office 365 environments.(Citation: AWS IAM Policies and Permissions)(Citation: Google Cloud IAM Policies)(Citation: Microsoft Support O365 Add Anothe...

---

## 8. Network Sniffing

| Field | Value |
|---|---|
| **ID** | T1040 |
| **Tactic** | Credential Access |
| **Reference** | https://attack.mitre.org/techniques/T1040 |

**Description:** Adversaries may passively sniff network traffic to capture information about an environment, including authentication material passed over the network. Network sniffing refers to using the network interface on a system to monitor or capture information sent over a wired or wireless connection. An adversary may place a network interface into promiscuous mode to passively access data in transit over...

---

## 9. Network Share Discovery

| Field | Value |
|---|---|
| **ID** | T1135 |
| **Tactic** | Discovery |
| **Reference** | https://attack.mitre.org/techniques/T1135 |

**Description:** Adversaries may look for folders and drives shared on remote systems as a means of identifying sources of information to gather as a precursor for Collection and to identify potential systems of interest for Lateral Movement. Networks often contain shared network drives and folders that enable users to access file directories on various systems across a network. 

File sharing over a Windows netwo...

---

## 10. Ccache Files

| Field | Value |
|---|---|
| **ID** | T1558.005 |
| **Tactic** | Credential Access |
| **Reference** | https://attack.mitre.org/techniques/T1558/005 |

**Description:** 
Adversaries may attempt to steal Kerberos tickets stored in credential cache files (or ccache). These files are used for short term storage of a user's active session credentials. The ccache file is created upon user authentication and allows for access to multiple services without the user having to re-enter credentials. 

The <code>/etc/krb5.conf</code> configuration file and the <code>KRB5CCNA...

---

