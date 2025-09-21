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

1.  **Clone the repository:**
    `git clone https://docs.github.com/en/repositories/creating-and-managing-repositories/deleting-a-repository`
2.  **Install Python dependencies:**
    `pip install -r requirements.txt`
3.  **Set up your environment variables:**
    * Create a `.env` file in the project's root directory.
    * Add your VirusTotal API key: `VIRUSTOTAL_API_KEY=your_api_key_here`
4.  **Configure Splunk log paths:**
    * Modify the `config.py` file to specify the exact path to your Splunk logs.

---

## Usage

* **Manual Execution:**
    `python your_script_name.py`
* **Automated Execution (Cron Job):**
    * To run the script every 5 minutes, add the following line to your crontab:
    `*/5 * * * * python /path/to/your_script_name.py`

---

## Repository Structure

```
```

* `your_script_name.py`: Main script for detection and blocking.
* `requirements.txt`: List of Python libraries needed.
* `config.py`: File for configuration variables.
* `.env.example`: Example file for environment variables.

---

## Author

* **[Tu Nombre]** - [Tu perfil de GitHub](URL de tu perfil)

---

## License

This project is licensed under the [**MIT**](/LICENSE) license.
