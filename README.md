![conny-schneider-xuTJZ7uD7PI-unsplash](https://github.com/user-attachments/assets/7f51e31b-1f0c-4e44-8cf5-63f270a62f38)

# Firewall-rule-automated-response-with-Python
This repository provides a Python script that automates a security response by parsing malicious IP addresses from Splunk logs, verifying them with VirusTotal, and blocking them with firewall rules.


## Index

* [Introduction](#introduction)
* [Features](#features)
* [Prerequisites](#prerequisites)
* [Configuration](#configuration)
* [Workflow](#workflow)
* [Usage](#usage)
* [Repository Structure](#repository-structure)
* [Lesson Learned](#lesson-learned)
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
To keep your credentials secure, this script uses environment variables. Before running, set the following variables in your system's environment:
- `SPLUNK_HOST`: The hostname or IP address of your Splunk instance.
- `SPLUNK_PORT`: The Splunk management port (default is `8089`).
- `SPLUNK_USER`: Your Splunk username.
- `SPLUNK_PASSWORD`: Your Splunk password.
- `VIRUSTOTAL_API_KEY`: Your API key from VirusTotal.
- `SMTP_SERVER`: The SMTP server you'll use (e.g., smtp.gmail.com).
- `SMTP_PORT`: The port for the SMTP server (e.g., `587`).
- `SMTP_USER`: Your email address or API key.
- `SMTP_PASSWORD`: The password or API key for your email account.
- `SSH_HOST`: The hostname or IP address of the machine you're connecting to via SSH.
- `SSH_USER`: The username for the SSH connection.
- `SSH_PASSWORD`: The password for the SSH connection.
3. Get your API key:
- Visit [VirusTotal](https://docs.virustotal.com/docs/please-give-me-an-api-key) to get your API key.

Note:
Ensure that TCP port 8089 allows inbound communication on the Splunk server. This port is needed for the splunk-sdk module to establish a connection as a client and access the Splunk API.
Additionally, on the machine where you are running the script, port 587 must be open to allow outbound connections to the SMTP server. This is necessary for the script to be able to send notification emails.

---

## Workflow

1. Splunk Connection: The script connects to the Splunk API using the [splunk-sdk](https://dev.splunk.com/enterprise/docs/devtools/python/sdk-python/) and runs a predefined search to find attack logs.
2. IP Extraction: It analyzes the Splunk results and extracts a list of IP addresses.
3. VirusTotal Verification: It sends each IP to the VirusTotal API to check if it has a high-risk score.
4. Automated Response: If an IP is confirmed as malicious, the script creates an iptables rule to block it on the system's firewall.
5. Notification: It sends an email notification to the administrator with the details of the blocked IPs.
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
|
├── README.md
├── requirements.txt
├── ip-block.py
└── LICENSE
```

* `ip-block.py`: Main script for detection and blocking.
* `requirements.txt`: List of Python libraries needed.

---

## Lesson Learned

This project was a valuable opportunity to gain hands-on experience with automated security responses in a real-world environment. It challenged me to broaden my understanding of REST APIs and their application in security automation.
By leveraging AI tools to accelerate development, I was able to efficiently debug errors and grasp complex concepts. This allowed me to focus on the core logic and cybersecurity principles, transforming the project into a powerful demonstration of both technical skill and my ability to utilize modern tools for problem-solving.

---

## Author

[nachogtan](https://github.com/nachogtan)

---

## License

This project is licensed under the [**MIT**](/LICENSE) license.
