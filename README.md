# Wireless-Penetration-Testing-WEP-WPA2-Cracking-Rogue-AP-Simulation

## Table of Contents  
- [Overview](#overview)  
- [Key Topics Covered](#key-topics-covered)  
- [Files Included](#files-included)  
- [Tools & Technologies Used](#tools--technologies-used)  
- [Methodology](#methodology)  
- [Ethical Considerations](#ethical-considerations)  
- [Learning Outcomes](#learning-outcomes)  
- [Contact](#contact)  

![Status](https://img.shields.io/badge/Status-Completed-green)  
![Tech](https://img.shields.io/badge/Tools-Aircrack--ng%20%7C%20Wireshark%20%7C%20Scapy-blue)  

## Methodology  
### 1. WEP Cracking  
- Captured Initialization Vectors (IVs) using `airodump-ng`.  
- Launched ARP replay attack to accelerate IV collection.  
- Decrypted WEP key using `aircrack-ng`.  

### 2. WPA2 Cracking  
- Captured a 4-way handshake using `airodump-ng`.  
- Used dictionary-based attack with `aircrack-ng`.  
- Decrypted network traffic in Wireshark using recovered keys.  

### 3. Deauthentication Attack  
- Sent deauthentication frames using `aireplay-ng`.  
- Disconnected clients from the target network (CVE-2019-16275).  

### 4. Rogue Access Point Simulation  
- Configured a fake access point using `hostapd`.  
- Redirected traffic and captured data packets.  

# Enable Monitor Mode
sudo airmon-ng start wlan0

# Capture WPA2 Handshake
sudo airodump-ng -c 6 --bssid XX:XX:XX:XX:XX:XX -w capture wlan0mon
