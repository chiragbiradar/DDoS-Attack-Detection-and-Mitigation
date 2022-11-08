# DDoS-Attack-Detection-and-Mitigation-using-Machine-Learning
## Project Description

### Problem Statement
To detect and mitigate DDoS attack using Machine Learning
Apply machine model to classify attack traffic and normal traffic
Apply mitigation module for detected attack traffic source ports

## Motivation
SDN enables to design, build and operate network.
SDN networks are often exposed to new security threats and attacks, especially Distributed Denial of Service (DDoS) attacks
More vulnerable DDoS attack due to centralized nature of SDN.
Distributed denial-of-service (DDoS) attacks pose a great threat to the data centers

## Objective
Implementation of network using mininet and ryu controller
Generating the own dataset
Attack detection:Using machine learning technique distinguish between normal or malicious traffic flow
Adding the mitigation module(main purpose to be the reduce the attack on the system/host)


### Problem space:
A DDoS attack is a malicious attempt to disrupt the normal traffic of a targeted server, service or network.
DDos attacks pose a great threat to data centers

### Objectives:
To implement the network(for LAN) using mininet RYU controller
To generate datasets for normal traffic and attack traffic
To detect attack using suitable ML model
To add the mitigation module

### Problem Definition:
To detect and mitigate DDoS attack using Machine Learning
Apply machine model to classify attack traffic and normal traffic
Apply mitigation module for detected attack traffic source ports

### Technical Challenges:
Excess time for Dataset generation.
Finding an optimal trade off between prediction accuracy and delay.


### Dataset Details:
Dataset is generated using python scripts for malicious traffic and legitimate traffic
      Dataset size = 22x2667523
      Data description:
      Ip_source - source ip address
      Ip_dst - destination ip address
      Icmp_type - 
      Flow duration - 
      Idle time -
      Packet_count -
      Label - classify malicious or legitimate traffic(1=legitimate & 0=malicious)


### Measurable Outputs

### Observations:
Load on victim machine increases when ICMP,SYN,UDP,SMRUF flood is being sent to victim machine
Flood attack is sent from random ip adresses

## Functional and Non-Functional Requirements
### Functional  Requirements
Machine learning model should be able to detect DDoS attacks
Communicate with the controller to request traffic information
Provide security to the website or application from your networks
Mitigate the DDoS attack without restricting the normal traffic

### Non Functional Requirements:
Detect DDoS attack within 20 seconds
Analyze traffic data every 5 seconds to classify traffic as normal or abnormal
Mitigate the malicious traffic  in two minutes to detect its port number


# Architecture
Software-Defined Networking (SDN) is a network architecture approach that enables the network to be intelligently and centrally controlled, or 'programmed,' using software applications

![image](https://user-images.githubusercontent.com/78417411/200639379-74f382c3-3084-47fc-b1fc-515b0bfd10c5.png)

## SDN architecture includes three layers: 
### The application layer:
The application layer contains the typical network applications or functions organizations use. This can include intrusion detection systems, load balancing or firewalls. A software-defined network replaces the appliance with an application that uses a controller to manage data plane behavior

### The control layer:
The control layer represents the centralized SDN controller software that acts as the brain of the software-defined network. This controller resides on a server and manages policies and traffic flows throughout the network.

This made up of the physical switches in the network. These switches forward the network traffic to their destinations.

# 2.2 Description of target User
In a distributed denial-of-service (DDoS) attack, multiple compromised  computer systems attack a target and cause a denial of service for users of the targeted resource. The target can be a server, website or other  network resource. The flood of incoming messages, connection  requests or malformed packets to the target system forces it to slow down or even crash and shut down, thereby denying service to legitimate users or systems

# 2.4 Scope
• Security services
• Network intelligence and monitoring
• Compliance and regulation bound application
• High performance applications
• Distributed application control and cloud integration

# 3.System Software Requirement specification
## 3.1 Overview of SRS
• Here is the detailed description of requirements specifications i.e., 
functional requirements, use case diagrams and nonfunctional 
requirements.
• Software and Hardware requirements is also discussed.

## 3.2 Requirement Specification
### 3.2.1 Functional Requirement 
• The model should be able to detect DDoS attack accurately.
• The model should be efficient enough to restore the 
affected server or website as soon as possible.
• The identification process must not stop or restrict the 
incoming traffic, but at the same time, the network must be 
able to identify and resist the attacking node in the network

### 3.2.4 Non Functional requirement
• Mitigate DDoS attack by tracing the source and tracing its 
ethernet address.
• Classify traffic as normal or abnormal.
• It is 24x7 available to user.

### 3.3 Software and Hardware requirement 
### specifications
• Windows/ Linux/ mac os
• Virtualization software (vmware/virtual box)
• Ryu controller 
• Mininet software
• Wireshark (for network monitoring)

# Flow chart
![image](https://user-images.githubusercontent.com/78417411/200639471-57cc2ecc-ef7a-4c5f-9364-056ee55ca53f.png)


# Activity Diagram
![image](https://user-images.githubusercontent.com/78417411/200639554-0238dd97-ada4-4a73-a4eb-ebb312dd34d2.png)

# Network Topology
![image](https://user-images.githubusercontent.com/78417411/200657095-cfac805b-7d1e-4908-857c-3967ca221f61.png)


# Gantt Chart





