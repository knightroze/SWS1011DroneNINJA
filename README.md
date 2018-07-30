# SWS1011DroneNINJA
This project is about how to hack the JJRC_F70447

In this project, we will comparatively analyze the WiFi communications and radio communications of drones, taking JJRC F70447 as a typical example.We conducted a series of experiments to study the communication process of the Wi-Fi communication drone , analyzed its security risks exposed by the implementations and explored possible attacks that can be made. Our analysis is conducted via packet sniffing and based on our findings we identified achievable attack vectors and discussed the protecting measures we can do in the future

<h1>The WiFi connection process</h1>
<p>we found that both TCP and UDP protocols are used, but the main communication protocol is UDP. The communication between the two sides is
as follows. The client first sends a short packet with the value of ’0f’, ’28’,’0A’,’27’ to the 8080 port of the JJRC using the UDP protocol, and it is presumed to be initialization
of the connection. Then the controller sends a packet with a value of "08:ac:10:f7:d1" per second and accepts the response package of "6f:6b:69:70:00".We speculates these are
the packets used by both parties to confirm the other party’s survival status. After the connection is stabilized, the controller starts transmitting a control signal of length 11 at
a frequency of about 0.02 second intervals. The JJRC done will use 4096 ports to send video streams to the 8888 port of the controller.</p>
<p>We focus on the control signal messages of the length 11, that is, focuses on the control information of JJRC, so that we can hijack JJRC later by using them. To this end, we
carry out simple control operations on JJRC, deliberately filter out the above types of messages. Through the observation of its data domain, we finally analyze the meaning of
each bit in the data.</p>

<p>We can get: 1-4 bits and 15-18 bits remain unchanged; 5-8 bits represent the position of the left handle joystick, and 9-12 bits represent the right handle
joystick s position. The 13-14 bits indicate whether the aircraft is in a hovering state, and the 19-20 bits indicate the state of the aircraft engine, including acceleration, emergency stop, and maintain 3 states. The last 2 bits represent
the checksum. After a lot of calculations, we believe that the checksum satisfies the following rule, that is the sum of the hexadecimal numbers represented by every two bits and
divided it by 256, the remainder is equal to the checksum. After sorting it out, it is found that those data are actually the positions of the left and right rocker in their respective
coordinate systems</p>

<h1>Attack</h1>
After the previous analysis, we have now mastered the attack that we hope to achieve is mainly divided into three gradual stages:
1. Sniff, confirm the target drone and get the target address and communication channel .
2. Use DOS attack to paralyze the drone-carried WIFI then the former operator will lose control of the drone.
3. Stop DOS attacks, quickly connect to the drone with computer, and activate hijacking scripts

<h3>Sniffing</h3>
First, set the WiFi dongle to monitor mode, so that we can monitor the WiFi signal. This can be implemented with the following instructions
#ifconfig wlan0 down
#iwconfig wlan0 mode monitor
#ifconfig wlan0 up
Then use Airodump-ng to conduct sniffing, we can use the instruction below to implement. 
#airodump-ng wlan0
The result is shown in the image below. Observe the ESSID on the right, lock our attack target, record the corresponding BSSID and CH(channel), so as to prepare for the next
attack. When we are conducting the DOS attack, we need to ensure that the WiFi dongle and JJRC are in the same channel. The channel can be modified by the following instructions
#airmon-ng start wlan0 X
The parameter X refers to the channel.
<h3>DoS</h3>
DOS is the abbreviation for denial of service, which is aimed to make the target host unable to provide normal service to legitimate users. Here we use Aireplay-ng to launch a
Deauth attack. The principle of Deauth attack is to send a large number of forgery of authentication messages to the network, blocking a connection between a legitimate user
and the access point, And the user can’t reconnect during the attack. This attack can be launched through the command below.
#aireplay-ng -0 0 -a BSSID wlan0
<h3> Hijacking</h3>
Through the previous attack, we have made the drone out of control. Now we can start the hijacking script to control it. Since our goal is controlling, we need to establish
a connection as soon as possible, and then send the control signal to the 8080 port to achieve control. Since the drone will only respond to the terminal that first established the
connection, the original controller can’t control the drone again when we set up a connection.
<h1>DISCUSSIONS</h1>
In this section, we will summarize our research these days and try to find ways to protect our drones. At last, we will figure out what we will be able to study in depth, providing
we have more time to research.
<h3>Limitation</h3>
We are not able to explore more further ways of attacking against the drone for the lack of time. We also can’t conduct more in-depth research on the drones that use the radio to
communicate, and because of the difficulty of building the hardware environment, we have not been able to achieve the attack.
<h3>Defense</h3>
After analyzing the drones and implementing specific attacks, we found that there are many security vulnerabilities and security risks in the drones, but taking some corrective
measures can greatly improve the security of the drones.
1. WiFi Encryption
The WiFi of the drone is open without password and identity authentication, which is contrary to the principle of confidentiality in the CIA principle. Takingmeasures like using WPA/WPA2 will make it safer to
use. WPA is also able to withstand a certain degree of DOS attack rather than WiFi without any protection.
2. Equipment Certification
If the user performs a device authentication process before using drone, the drone could reject the connection request of any other device before the authentication is changed, so the hacker can’t easily complete
the hijacking.
3. Message Encryption
Encrypting packets can greatly increase the difficulty of protocol analysis, but will also affect communication efficiency.
<h1> Future</h1>
In this project, the main content of our research is the interaction between the drone and the controller communicated by WiFi. Due to time constraints, we have just completed
research based on the JJRC model drone, which is not enough for us to find some common security vulnerabilities of drones. Therefore, in the future, we will try to apply the
theory we have discovered to the analysis of many different drones and summarize their vulnerabilities. Another expansion of the project is the study of the radio drone HUBSAN.
At present we have found its working frequency (channel), in the future we want to try to find the format of the packet and decode it, then we will complete the binding phase and
carry out some attacks, such as DOS attack or replay attack. Finally, we will make a more comprehensive comparison and summary of WiFi and radio drones in the future.
<h1>CONCLUSIONS</h1>
After analyzing the drones using WiFi as the communication and control method, we can decode almost all control packets and be able to attack them at multiple levels. In order to achieve the attack, we only need a properly configured
computer and install some very basic software and two WiFi dongles. Once we are able to connect to the drone, DOS and Sniffing can be easy to conduct, in addition, we can even use
our computer to control the drone. It means that a lot of commercial drones are vulnerable to malicious attack. The drone we used doesn’t have a password for its open network,
but for more sophisticated and advanced drones, they may take more protecting measures, such as encrypted packets, making them less vulnerable. But once the packets are
decoded, they are as fragile as ordinary drones.
<h1>ACKNOWLEDGMENTS</h1>
We would like to extend our heartfelt gratitude to Professor Hugh Anderson for his patience, encouragement and guidance during the project time.We are also very grateful to
him and the School of Computing for providing us with the equipment we need for our projects. We would also like to thank Teaching Assistant Ang Ray Yan for his help and
guidance.     
