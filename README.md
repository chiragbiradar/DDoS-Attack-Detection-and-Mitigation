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

## Proposed System
![image](https://user-images.githubusercontent.com/78417411/200159701-04f8242d-0887-4329-8987-1801a0cfb885.png)

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


## SDN architecture includes three layers: 
### The application layer:
The application layer contains the typical network applications or functions organizations use. This can include intrusion detection systems, load balancing or firewalls. A software-defined network replaces the appliance with an application that uses a controller to manage data plane behavior

### The control layer:
The control layer represents the centralized SDN controller software that acts as the brain of the software-defined network. This controller resides on a server and manages policies and traffic flows throughout the network.

This made up of the physical switches in the network. These switches forward the network traffic to their destinations.


# Flow chart

# Activity Diagram

# Gantt Chart





