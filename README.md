# DDoS Attack Detection and Mitigation using Machine Learning


[![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/chiragbiradar/DDoS-Attack-Detection-and-Mitigation-using-Machine-Learning?logo=github&style=for-the-badge)](https://github.com/chiragbiradar/) 
[![GitHub last commit](https://img.shields.io/github/last-commit/chiragbiradar/DDoS-Attack-Detection-and-Mitigation-using-Machine-Learning?style=for-the-badge&logo=git)](https://github.com/chiragbiradar/) 
[![GitHub stars](https://img.shields.io/github/stars/chiragbiradar/DDoS-Attack-Detection-and-Mitigation-using-Machine-Learning?style=for-the-badge)](https://github.com/chiragbiradar/DDoS-Attack-Detection-and-Mitigation-using-Machine-Learning/stargazers) 
[![My stars](https://img.shields.io/github/stars/chiragbiradar?affiliations=OWNER%2CCOLLABORATOR&style=for-the-badge&label=My%20stars)](https://github.com/chiragbiradar/DDoS-Attack-Detection-and-Mitigation-using-Machine-Learning/stargazers) 
[![GitHub forks](https://img.shields.io/github/forks/chiragbiradar/DDoS-Attack-Detection-and-Mitigation-using-Machine-Learning?style=for-the-badge&logo=git)](https://github.com/chiragbiradar/DDoS-Attack-Detection-and-Mitigation-using-Machine-Learning/network)
[![Code size](https://img.shields.io/github/languages/code-size/chiragbiradar/DDoS-Attack-Detection-and-Mitigation-using-Machine-Learning?style=for-the-badge)](https://github.com/chiragbiradar/DDoS-Attack-Detection-and-Mitigation-using-Machine-Learning)
[![Languages](https://img.shields.io/github/languages/count/chiragbiradar/DDoS-Attack-Detection-and-Mitigation-using-Machine-Learning?style=for-the-badge)](https://github.com/chiragbiradar/DDoS-Attack-Detection-and-Mitigation-using-Machine-Learning)
[![Top](https://img.shields.io/github/languages/top/chiragbiradar/DDoS-Attack-Detection-and-Mitigation-using-Machine-Learning?style=for-the-badge&label=Top%20Languages)](https://github.com/chiragbiradar/DDoS-Attack-Detection-and-Mitigation-using-Machine-Learning)
[![Issues](https://img.shields.io/github/issues/chiragbiradar/DDoS-Attack-Detection-and-Mitigation-using-Machine-Learning?style=for-the-badge&label=Issues)](https://github.com/chiragbiradar/DDoS-Attack-Detection-and-Mitigation-using-Machine-Learning)
[![Watchers](https://img.shields.io/github/watchers/chiragbiradar/DDoS-Attack-Detection-and-Mitigation-using-Machine-Learning?label=Watch&style=for-the-badge)](https://github.com/chiragbiradar/DDoS-Attack-Detection-and-Mitigation-using-Machine-Learning/) 

`DDoS Attack Detection and Mitigation using Machine Learning`

![image](https://user-images.githubusercontent.com/78417411/204220907-67fb2338-1023-4404-8320-b7c2967bd0a3.png)

## 1) Project Description

### 1.1 Problem Statement
To detect and mitigate DDoS attack using Machine Learning
Apply machine model to classify attack traffic and normal traffic
Apply mitigation module for detected attack traffic source ports

## 1.2 Motivation
SDN enables to design, build and operate network.
SDN networks are often exposed to new security threats and attacks, especially Distributed Denial of Service (DDoS) attacks
More vulnerable DDoS attack due to centralized nature of SDN.
Distributed denial-of-service (DDoS) attacks pose a great threat to the data centers

## 1.3 Objective
Implementation of network using mininet and ryu controller
Generating the own dataset
Attack detection:Using machine learning technique distinguish between normal or malicious traffic flow
Adding the mitigation module(main purpose to be the reduce the attack on the system/host)


### 1.4 Objectives:
To implement the network(for LAN) using mininet RYU controller
To generate datasets for normal traffic and attack traffic
To detect attack using suitable ML model
To add the mitigation module


### 1.5 Technical Challenges:
Excess time for Dataset generation.
Finding an optimal trade off between prediction accuracy and delay.


### 1.6 Dataset Details:
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


### 1.7 Measurable Outputs

### 1.7.1 Observations:
Load on victim machine increases when ICMP,SYN,UDP,SMRUF flood is being sent to victim machine
Flood attack is sent from random ip adresses

## 1.8 Functional and Non-Functional Requirements
### Functional  Requirements
Machine learning model should be able to detect DDoS attacks
Communicate with the controller to request traffic information
Provide security to the website or application from your networks
Mitigate the DDoS attack without restricting the normal traffic

### Non Functional Requirements:
Detect DDoS attack within 20 seconds
Analyze traffic data every 5 seconds to classify traffic as normal or abnormal
Mitigate the malicious traffic  in two minutes to detect its port number


# 2) Architecture
Software-Defined Networking (SDN) is a network architecture approach that enables the network to be intelligently and centrally controlled, or 'programmed,' using software applications

![image](https://user-images.githubusercontent.com/78417411/200639379-74f382c3-3084-47fc-b1fc-515b0bfd10c5.png)

## 2.1 SDN architecture includes three layers: 
### The application layer:
The application layer contains the typical network applications or functions organizations use. This can include intrusion detection systems, load balancing or firewalls. A software-defined network replaces the appliance with an application that uses a controller to manage data plane behavior

### The control layer:
The control layer represents the centralized SDN controller software that acts as the brain of the software-defined network. This controller resides on a server and manages policies and traffic flows throughout the network.

This made up of the physical switches in the network. These switches forward the network traffic to their destinations.

## 2.2 Description of target User
In a distributed denial-of-service (DDoS) attack, multiple compromised  computer systems attack a target and cause a denial of service for users of the targeted resource. The target can be a server, website or other  network resource. The flood of incoming messages, connection  requests or malformed packets to the target system forces it to slow down or even crash and shut down, thereby denying service to legitimate users or systems

## 2.3 Scope
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

### 3.2.2 Non Functional requirement
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



## Installation
### Setup
Step-1
install [Virtual box](https://www.virtualbox.org/wiki/Downloads) or VM-ware workstation

Step-2 
install [Mininet-VM](https://github.com/mininet/mininet/releases/)

Step-3
install [Ubuntu](https://ubuntu.com/download/desktop) in virtual box

Step-4
install [ryu-controller](https://ryu.readthedocs.io/en/latest/getting_started.html) in ubuntu vm

Step-5
Use git clone to install the code files
```bash
git clone https://github.com/chiragbiradar/DDoS-Attack-Detection-and-Mitigation-using-Machine-Learning.git
```

### Go to Mininet-vm

```bash
# change working directory to mininet folder
cd mininet

# change controller ip address
nano topology.py

# run topology
sudo python topology.py
```

### Go to Ubuntu vm

```bash
# change working directory to controller folder
cd controller

# switch on the ryu-controller
ryu-manager controller.py


