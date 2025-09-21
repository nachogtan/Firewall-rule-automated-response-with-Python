![conny-schneider-xuTJZ7uD7PI-unsplash](https://github.com/user-attachments/assets/7f51e31b-1f0c-4e44-8cf5-63f270a62f38)

# Firewall-rule-automated-response-with-Python
This repository provides a Python script that automates a security response by parsing malicious IP addresses from Splunk logs, verifying them with VirusTotal, and blocking them with firewall rules.


## Index

* [Introduction](#introduction)
* [Features](#features)
* [Prerequisites](#prerequisites)
* [Configuration](#configuration)
* [Usage](#usage)
* [Repository Structure](#repository-structure)
* [Author](#author)
* [License](#license)

---

## Introduction

This project serves as an extension of my previous labs. It leverages the security architecture established in my [Home-Lab](https://github.com/nachogtan/Home-Lab-Project-Building-a-Multi-Hommed-Router-and-Firewall-with-Debian) and builds upon the threat detection capabilities developed in my [Splunk-Brute-Force-Detection](https://github.com/nachogtan/Splunk-Brute-force-detection) lab, adding an automated response layer.

---

## Features

* **Automated Threat Detection**: Parses specified logs from **Splunk** to identify malicious IP addresses.
* **Threat Intelligence Integration**: Verifies detected IPs against the **VirusTotal API** to confirm if they are malicious.
* **Automated Response**: Automatically creates and applies **iptables** firewall rules to block confirmed malicious IPs, preventing further attacks.

---

## Prerequisites

* A working **Python 3** environment.
* Access to your **Splunk** logs (ensure the script has the necessary permissions).
* A valid **VirusTotal API key**.
* **iptables** installed on the system where the script will run. The script requires root privileges to modify firewall rules.

---

## Configuration

1.  **Install Python dependencies:**
- `pip install -r requirements.txt`
2.  Edit the script:
- Open the main script file ([your_script_name.py]).
- Locate the variables for the log file path and the VirusTotal API key.
- Replace the placeholder values with your specific information.
3. Get your API key:
- Visit [VirusTotal](https://docs.virustotal.com/docs/please-give-me-an-api-key) to get your API key.

   
---

## Usage

* **Manual Execution:**
    `[python your_script_name.py]`
* **Automated Execution (Cron Job):**
    * To run the script every 5 minutes, add the following line to your crontab:
    `*/5 * * * * python /path/to/[your_script_name.py]`

---

## Repository Structure

```
```

* `ip-block.py`: Main script for detection and blocking.
* `requirements.txt`: List of Python libraries needed.

---

## Author

[nachogtan](https://github.com/nachogtan)

---

## License

This project is licensed under the [**MIT**](/LICENSE) license.
