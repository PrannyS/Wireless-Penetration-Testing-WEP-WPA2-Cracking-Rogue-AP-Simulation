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

# Crack WEP keykey
sudo aircrack-ng -b XX:XX:XX:XX:XX:XX wep_capture.pcap
```

### **2️⃣ Cracking WPA2 Encryption**  
- Captured **4-way handshake** using `airodump-ng`.  
- Used dictionary attack with `aircrack-ng`.  

```bash
# Capture handshake
sudo airodump-ng -c 6 --bssid XX:XX:XX:XX:XX:XX -w handshake wlan0mon

# Crack WPA2 password
sudo aircrack-ng -w passwords.txt -b XX:XX:XX:XX:XX:XX handshake.pcap
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
sudo hostapd hostapd.conf
```

---

## ⚖️ Ethical Considerations

⚠️ Disclaimer: This project was conducted in a controlled lab environment as part of an academic exercise in cybersecurity. Unauthorized Wi-Fi penetration testing is illegal without explicit permission. The purpose of this lab was to understand security weaknesses and develop skills for ethical hacking and cybersecurity defense."

Key ethical principles followed:
✔️ Responsible Disclosure – Understanding vulnerabilities to help secure networks.
✔️ No Unauthorized Testing – Experiments were performed in a controlled environment with instructor approval.
✔️ Security Awareness – The findings from this lab help reinforce best security practices for network protection.

🎯 Learning Outcomes
By completing this lab, I gained the following skills:

✔️ Hands-on experience with Wi-Fi security – Analyzed encryption flaws in WEP and WPA2.
✔️ Packet Sniffing & Analysis – Used Wireshark to capture and inspect wireless traffic.
✔️ Cracking Encryption Keys – Learned how dictionary attacks and IV collection work against WPA2 and WEP.
✔️ Ethical Hacking Techniques – Performed deauthentication attacks and rogue AP simulations.
✔️ Understanding Countermeasures – Explored network defense strategies, including WPA3, VPNs, and intrusion detection.

🖼️ Screenshots
📌 Cracking WPA2 Handshake

📌 Deauthentication Attack in Action

📄 Resume Description
"Conducted hands-on penetration testing of Wi-Fi networks, assessing vulnerabilities in WEP and WPA2 encryption. Executed packet sniffing, dictionary attacks, and deauthentication exploits using Aircrack-ng, Wireshark, and Scapy. Simulated rogue access points to analyze client behavior and proposed countermeasures to mitigate security risks. Documented findings in a structured report with technical analysis and recommendations."

📩 Contact
For any inquiries, feel free to reach out via:
📌 GitHub: yourusername
📌 LinkedIn: your-linkedin-url
hello