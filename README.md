# Wi-Fi Security Lab (CY 4760/6760)  
**Course:** Wireless and Mobile Network Security  
**Instructor:** Prof. Aanjhan Ranganathan  
**Semester:** Fall 2024  
**Author:** Pranav S.  

![Status](https://img.shields.io/badge/Status-Completed-green)  
![Tech](https://img.shields.io/badge/Tools-Aircrack--ng%20%7C%20Wireshark%20%7C%20Scapy-blue)  

## 📌 Overview  
This repository contains my submission for **Lab 4: Wi-Fi Security**, where I explored vulnerabilities in wireless networks, including:  
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
- [Ethical Considerations](#ethical-considerations)  
- [Learning Outcomes](#learning-outcomes)  
- [Screenshots](#screenshots)  
- [Resume Description](#resume-description)  
- [Contact](#contact)  

---

## 🛠 Key Topics Covered  
- **Cracking WEP Encryption**: Used `aircrack-ng` to recover WEP keys by analyzing captured IVs.  
- **Breaking WPA2-PSK Encryption**: Captured WPA2 handshake and used dictionary attacks.  
- **Deauthentication Attacks**: Exploited CVE-2019-16275 to disconnect clients from a Wi-Fi network.  
- **Rogue Access Point Attack**: Set up a fake AP and captured victim traffic.  

---

## 📂 Files Included  
| File Name | Description |  
|-----------|------------|  
| `Group11_Lab4.pdf` | Detailed report with methodology and findings |  
| `Lab4_wifi_Fall2024.pdf` | Original lab instructions |  
| `scripts/deauth-students.py` | Python script for deauthentication attack |  
| `captures/wep_crack.pcap` | Packet capture file used for WEP cracking |  
| `captures/wpa_handshake.pcap` | Packet capture file containing WPA handshake |  
| `wordlists/passwords.txt` | Wordlist used for WPA cracking |  

---

## 🔧 Tools & Technologies Used  
- **Aircrack-ng Suite** (`Airmon-ng`, `Airodump-ng`, `Aircrack-ng`, `Aireplay-ng`)  
- **Wireshark** – Network packet analysis  
- **Scapy** – Packet manipulation & forging  
- **Python** – Scripting for automated attacks  
- **Linux CLI (Ubuntu VM)** – Running security tools  

---

## 🔍 Methodology  

### **1️⃣ Cracking WEP Encryption**  
- Enabled **monitor mode** using `airmon-ng`.  
- Captured packets using `airodump-ng`.  
- Used **IVs** to decrypt the key with `aircrack-ng`.  

```bash
# Start monitor mode
sudo airmon-ng start wlan0

# Capture packets
sudo airodump-ng -w wep_capture wlan0mon

# Crack WEP key
sudo aircrack-ng -b XX:XX:XX:XX:XX:XX wep_capture.pcap
