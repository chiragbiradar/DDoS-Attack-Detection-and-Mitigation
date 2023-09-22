#### Documentation under process!!!

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


# DDoS Attack Detection and Mitigation using Machine learning

A distributed denial-of-service (DDoS) attack is a malicious attempt to disrupt the normal traffic of a targeted server, service, or network by overwhelming the target or its surrounding infrastructure with a flood of internet traffic.
DDoS attacks achieve effectiveness by utilizing multiple compromised computer systems as sources of attack traffic. Exploited machines can include computers and other networked resources such as IoT devices.
From a high level, a DDoS attack is like an unexpected traffic jam clogging up the highway, preventing regular traffic from arriving at its destination. It's critical to act soon after discovering a DDoS attack since it provides you the chance to avert significant disruption. The server can start to crash on waiting too long, and a full recovery might take hours.
The hardest part about mitigating a DDoS attack is that often it’s virtually impossible to do so without impacting legitimate traffic. This is because attackers go to great lengths to masquerade fake traffic as real.

## Motivation
For enterprises operating at the edge with mission-critical activities that cannot afford downtime, DDoS mitigation as a protective layer is crucial. DDoS mitigation contributes to maintaining such activities' and services' ongoing availability. SDN allows for network design, construction, and operation. Attacks via distributed denial-of-service (DDoS) represent a serious risk to data centers.
New security concerns and assaults, particularly Distributed Denial of Service (DDoS) attacks, are frequently launched against SDN networks.

##  Objectives: 
* To implement a network using mininet and Ryu controller
* To generate the dataset
* To apply Random Forest Machine learning algorithm to detect DDoS attack
* To add mitigation module

## Literature Survey
[1] This paper proposed a model which is able to detect and mitigate DDoS attacks automatically in SDN networks using ML.All of the switches' traffic flow entries are periodically collected by the model, which then extracts the native flow features and expands them by incorporating new features. A detection module uses five features to categorize each flow as normal or anomalous. When an attack is discovered, its source is prevented. Six ML algorithms were assessed with regard to the classification ML method utilized in the detection module, including LR, NB, KNN, SVM, DT, and RF. The outcomes of the experiment demonstrated that RF is the best classifier for the generated network. Without losing typical performance, the model was able to swiftly and effectively identify and block attacks. 

[2] This work proposes a method of DDoS attack detection based on deep belief network feature extraction and LSTM model.  This technique uses deep learning to extract IP packet attributes, builds an LSTM traffic prediction model, and then recognises DDoS attacks using the built-in LSTM model. Technology for detecting DDoS attacks is appropriate for this system. The model can effectively forecast the pattern of typical network traffic, spot irregularities brought on by DDoS attacks, and be used to develop more DDoS attack detection techniques in the future.

[3] In this work, the authors proposed a model which analyzes the correlation information of flows in data centers. It offers a reliable method of detecting DDoS attacks based on CKNN (K-nearest neighbors traffic categorization with correlation analysis).

[4] This paper proposes a new model to detect DDoS attacks in SDN based on SVM . Firstly a trained Support Vector Machine (SVM) approach is used by the model to extract numerous important features from the packet-in messages and measure the distribution of each feature using entropy. Studies reveal that this technique is highly effective at both real-time DDoS mitigation and security event detection.

## Implemented System
![image](https://github.com/chiragbiradar/DDoS-Attack-Detection-and-Mitigation/assets/78417411/c6c46e97-7845-4a5e-8446-95be2821ff68)

### Description of the Implemented system
To achieve the  goal of detection of DDoS attack and mitigation model for SDN networks, a model is build on the application plane. The architecture of implemented method consists of the flow collector module, feature extender module, anomaly detection module, and anomaly mitigation module. The task of the flow collector is to regularly collect information on traffic flow from the flow tables of each switch. These flow entries will be delivered to the feature extender, which will produce new features for each entry. 	

The anomaly detection module will receive the gathered data and use machine learning (ML) to perform flow-based detection and classify each flow as normal or abnormal. An aberrant flow  will be sent to the Mitigation module in order to stop the source of the attack, else no action will be taken.

In order to obtain traffic data, the flow collector first contacts the controller. When the controller receives a request for traffic information, it employs 

To gather data from flow tables,  openflow protocol is used. Every switch connected to the controller receives a flow-stats request from the controller, which asks the switch for flow statistics. As a result, each switch responds with a flow-stats reply message that includes all flow entries from all flow tables, each entry of which includes the flow description and any associated counters. The controller then replies to this component after compiling the traffic data from all the switches.

The flow collector parses the flow information after receiving it and discards any unnecessary data. The flow identifier (flow-id) and the flow counters are the pertinent data that are kept. The source IP address, destination IP address, source MAC address, destination MAC address, TCP/UDP source port, TCP/UDP destination port, and transport protocol identification make up the seven-tuple that is  referred to as the flow-id (protocol). It's crucial to remember that this tuple can be modified to meet the requirements of the network infrastructure.

##  Software requirements specification
### Overview of SRS:
Software Requirement Definition (SRS) is a comprehensive specification and description of the software requirements that must be met for the software systems to be developed successfully. Depending on the sort of demand, they may be both functional and non-functional. In order to thoroughly grasp the demands of consumers, contact between various customers and contractors is done.

### Requirement Specification:
#### Functional Requirement:
* Machine learning model should be able to detect DDoS attacks
* Communicate with the controller to request traffic information
* Mitigate the DDoS attack without restricting the normal traffic

#### Non-Functional Requirement:
* Detect DDoS attack within 20 seconds
* Analyze traffic data every 5 seconds to classify traffic as normal or abnormal.
* Mitigate the malicious traffic in 2 minutes to detect its port number.

###  Software and Hardware requirement specification:
* Windows/ Linux/ macOS
* Virtualization software (VMware/virtual box)
* Ryu controller
* Mininet software
* Wire shark (for network monitoring)

## System Design
### Architecture of the System
Software-Defined Networking (SDN) is a network architecture approach that enables the network to be intelligently and centrally controlled, or 'programmed,' using software applications

#### SDN architecture includes three layers: 
#### Application layer:
The application layer is where the network applications, such as network management, traffic engineering, and security, are implemented.

#### Control layer:
The control layer represents the centralized SDN controller software that acts as the brain of the 
software-defined networking. This controller resides on a server and manages policies and traffic flows throughout the network.

#### Infrastructure layer:
The infrastructure layer is made up of the physical switches or routers in the network which forward traffic according to the instructions from the control plane.

### Activity Diagram


### Dataset Features Description:
Dataset is generated using python scripts for malicious traffic and legitimate traffic
* Dataset size = 22 columns x 2667523 rows
* Data description:
* Ip_source - source IP address
* Ip_dst - destination IP address
* Icmp_type 
* Flow duration 
* Idle time 
* Packet_count 
* Label - classify malicious or legitimate traffic(1=legitimate & 0=malicious)

## Implementation
### Implemented Methodology



#### Explanation:
The Implemented system consists of a detection module and a mitigation module. The model is trained  on the dataset that is  generated .

To generate the dataset, a topology in SDN using mininet. simulated network traffic(normal traffic and anomalous traffic) is created. Then feature's source IP, destination IP, port number, and timestamp from the packets using the RYU controller are extracted.


### Network topology:



### Module Description
#### Traffic Control module:
In order to obtain traffic data, the Flow Collector first contacts the controller. When the controller receives a request for traffic information, it employs To gather data from flow tables, 1use OpenFlow protocol. Every switch connected to the controller receives a flow-stats request from the controller, which asks the switch for flow statistics. As a result, each switch responds with a flow-stats reply message that includes all flow entries from all flow tables, each entry of which includes the flow description and any associated counters. The controller then answers this component after compiling the traffic data from all the switches. The Flow Collector parses the flow information after receiving it and discards any unnecessary data. The flow identifier (flow-id) and the flow counters are the pertinent data that are kept. The source IP address, destination IP address, source MAC address, destination MAC address, TCP/UDP source port, TCP/UDP destination port, and transport protocol identification make up the seven-tuple that is referred to as the flow-id (protocol). It's crucial to remember that this tuple can be modified to meet the requirements of the network infrastructure. Only three counters—the packet count, byte count, and duration—are included in the OpenFlow flow counters.

#### Detection module:
Depending on the source of the data to be studied or the method used to identify anomalous occurrences, there are several categories that might be used to classify intrusion detection. Flow-based or packet-based detection is employed depending on the data to be processed, and depending on the detection method, signature-based or anomaly-based detection can be utilized.

Flow-based detection was selected based on the source of the data to be evaluated since it would be more suited for high-speed networks and more effective than packet-based detection in terms of processing and memory overhead.

Anomaly-based intrusion detection is implemented  as a detection method, and more specifically, detection with ML.

#### Mitigation module:
Once a malicious flow has been verified by the anomaly detection module, the Anomaly Mitigation module is in charge of implementing mitigation measures to prevent network disruption or performance degradation. In the  framework, attack at its source is stopped. The preventing attacks caused by IP spoofing does not necessarily involve banning the attackers' IP addresses. For proof-of-concept purposes, in this case,   attacker's Ethernet address is blocked.


## Testing
### Test Plan and Test Cases:

## Results & Discussion
After designing the attack detection and mitigation method,the results are tested and evaluated.  The evaluation of the framework includes the evaluation of the different ML algorithms, and a comparison of the different models used. The below table shows the accuracies of different models used:


From the above table, it can be seen that random forest gives the best accuracy to categorize normal and malicious traffic.

In order to evaluate the performance of the model,  a test is performed by process of online traffic classification and attack mitigation. For mitigating attacks, firewall rules were set to block attacks that were detected. Thus, for every flow detected as malicious, a firewall rule is installed to block the Ethernet address from which the attack is launched.  The Python code of the generated prototype is implemented , and then normal traffic is generated as background traffic, and DDoS attack is detected.

Results from the below graph shows that after the traffic is launched it is collected and detected and firewall rules were installed to block the source attack.After this point all the attacks generated from the source were blocked without affecting normal traffic.

## Conclusion
In this work, a random forest machine learning algorithm is used to develop a model that can automatically identify and mitigate DDoS assaults in SDN networks. All of the traffic flow entries are regularly collected by the model, which then extracts the native flow features and expands them by including additional features. A detection module uses five criteria to categorize each flow as normal or anomalous. When an attack is discovered, its source is prevented. Three ML algorithms were assessed with regard to the classification ML method utilized in the detection module, including random forest, SVM, and KNN.
The outcomes of the experiment demonstrated that RF is the best classifier for the generated network. Without disrupting regular traffic, the implemented methodology proved effective at swiftly and correctly identifying and thwarting threats.

## References

Here are some related papers

[[1] Dong Li,Chang Yu, Qizhao Zhou and Junqing Yu .”Using SVM to Detect DDoS Attacks in SDN Network.” 2018 IOP Conf. Ser.: Mater. Sci. Eng. 466 012003,2018 .](https://iopscience.iop.org/article/10.1088/1757-899X/466/1/012003/meta)

[[2] Yijie Li, Boyi Liu, Shang Zhai and Mingrui Chen ,”DDoS attack detection method based on feature extraction of deep belief networks.”,IOP Conference Series: Earth and Environmental Science, Volume 252, Issue 3,2019.](https://iopscience.iop.org/article/10.1088/1755-1315/252/3/032013/met)

[[3] Peng Xiao,Wenyu Qu,Heng Qi ,Zhiyang Li.”Detecting DDoS attacks against data centers with correlation analysis.”,Computer Communications 67,2015.](https://www.sciencedirect.com/science/article/abs/pii/S0140366415002285)

[[4] Fatima Khashab, Joanna Moubarak, Antoine Feghali , and Carole Bassil.”DDoS Attack Detection and Mitigation in SDN using Machine Learning”,IEEE 7th International Conference on Network Softwarization (NetSoft),2021.](https://ieeexplore.ieee.org/abstract/document/9492558/)

[[5] Bawany NZ, Shamsi JA, Salah K. DDoS attack detection and mitigation  using
 SDN:     methods, practices, and solutions. Arabian Journal for Science and 
 Engineering. 2017 Feb;42(2):425-41.](https://link.springer.com/article/10.1007/s13369-017-2414-5)


[[6] Dharma, N.G., Muthohar, M.F., Prayuda, J.A., Priagung, K. and Choi, D., 2015,
August. Time-based DDoS detection and mitigation for SDN controller. In 
2015 17th Asia-Pacific Network Operations and Management Symposium (APNOMS) (pp. 550-553). IEEE.](https://ieeexplore.ieee.org/abstract/document/7275389/)
            
[[7]  da Silveira Ilha, A., Lapolli, A.C., Marques, J.A. and Gaspary, L.P., 2020. Euclid: A fully in-network, P4-based approach for real-time DDoS attack detection and mitigation. IEEE Transactions on Network and Service Management, 18(3), pp.3121-3139.](https://ieeexplore.ieee.org/abstract/document/9311137/)

    
[8] Singh, J. and Behal, S., 2020. Detection and mitigation of DDoS attacks in SDN: A comprehensive review, research challenges and future directions. Computer Science Review, 37, p.100279.


[9] Mihoub A, Fredj OB, Cheikhrouhou O, Derhab A, Krichen M. Denial of service attack detection and mitigation for internet of things using looking-back-enabled machine learning techniques. Computers & Electrical Engineering. 2022 Mar 1;98:107716.


[10] Miao, R., Yu, M. and Jain, N., 2014. Nimbus: cloud-scale attack detection and mitigation. Acm sigcomm computer communication review, 44(4), pp.121-122.


[11] Srinivasan, Karthik, Azath Mubarakali, Abdulrahman Saad Alqahtani, and A. Dinesh Kumar. "A survey on the impact of DDoS attacks in cloud computing: prevention, detection and mitigation techniques." In Intelligent Communication Technologies and Virtual Mobile Networks, pp. 252-270. Springer, Cham, 2019.


[12] Kautish, Sandeep, A. Reyana, and Ankit Vidyarthi. "SDMTA: Attack Detection and Mitigation Mechanism for DDoS Vulnerabilities in Hybrid Cloud Environment." IEEE Transactions on Industrial Informatics (2022).


[13] Gadze, James Dzisi, Akua Acheampomaa Bamfo-Asante, Justice Owusu Agyemang, Henry Nunoo-Mensah, and Kwasi Adu-Boahen Opare. "An investigation into the application of deep learning in the detection and mitigation of DDOS attack on SDN controllers." Technologies 9, no. 1 (2021): 14.


[14] Jaramillo, L.E.S., 2018. Malware detection and mitigation techniques: lessons learned from Mirai DDOS attack. Journal of Information Systems Engineering & Management, 3(3), p.19.


[15] Al-Duwairi, B., Al-Kahla, W., AlRefai, M.A., Abedalqader, Y., Rawash, A. and Fahmawi, R., 2020. SIEM-based detection and mitigation of IoT-botnet DDoS attacks. International Journal of Electrical and Computer Engineering, 10(2), p.2182.



## Appendix
### Glossary
* DDoS:It is a type of cyber attack that is carried out by flooding the target website or network with a large amount of traffic from multiple sources, with the aim of overwhelming the system and making it unavailable to users 
* Network Virtualization:Network virtualization is a technology that allows multiple virtual networks to be created and run on top of a physical network infrastructure.
* SDN:Network virtualization is a technology that allows multiple virtual networks to be created and run on top of a physical network infrastructure.
* Data Plane:the part of a network that is responsible for forwarding traffic between devices.
* Network Plane:it often refers to be as control plane
* Routers:device that is responsible for forwarding traffic between different networks.
* MAC address:It is a hardware address that is burned into the network interface during the manufacturing process, and it is used to identify the device on a network
* IP Address:it provides the location of the host in the network
* SYN Flood which is used to initiate a TCP connection, but not completing the final step of the process.
* ICMP Floodan ICMP echo request is a message that is sent to a network device to determine whether it is reachable and responding.
* SMURF Flood:sending large number of of icmpv4 flood
* UDP Flood:it and making it unavailable to legitimate users

### Description of Tools & Technology used
* Mininet:Mininet is a tool for software-defined networks.
* RYU controller:Ryu Controller is an open, software-defined networking (SDN) Controller designed to increase the agility of the network by making it easy to manage and adapt how traffic is handled.
* Virtual Box:Virtualization software
* Linux:Operating system
* Python:Programming Language
* Wireshark:Network Monitoring tool


