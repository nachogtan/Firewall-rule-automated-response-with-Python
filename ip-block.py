'''
This script is intended to detect malitious IP addresses by checking them 
against a predefined list of known bad IPs and well known databases as Virustotal.
The it creates arule to block that IP address on a debian router/firewall.
Lastly it sends an email notification to the admin.
'''

# Connect to Splunk instance
import os
import splunklib.client as client
import splunklib.results as results 

# print(help(client))
SplunkHost = "localhost"   
SplunkPort = 8089
SplunkUser = "admin"
SplunkPass = os.environ.get("SPLUNK_PASSWORD")

if not SplunkPass:
    print("Error: SPLUNK_PASSWORD environment variable not set.")
else:
    try:
        service = client.connect(
            host=SplunkHost,
            port=SplunkPort,
            username=SplunkUser,
            password=SplunkPass
        )
        print("Connected to Splunk successfully.")
        
        search_query = 'search index="main" sourcetype="access_combined" | stats count by clientip | where count > 100' # Search query. Analyze logs for IP addresses
        
        try:
            search_results_stream = service.jobs.oneshot(search_query)

            reader = results.ResultsReader(search_results_stream)
            
            for result in reader:
                if isinstance(result, dict):
                    print(f"Found IP: {result.get('clientip')} with count: {result.get('count')}")
                else:
                    print(f"Received a non-dictionary event: {result}")

        except Exception as e:
            print(f"Error executing search: {e}")
            
    except Exception as e:
        print(f"Failed to connect to Splunk: {e}")

# Check against Virustotal database
flagged_ips = []

if isinstance(flagged_ips = []

if isinstance(result, dict):
    ip_to_check = result.get('clientip')
    if ip_to_check:
        import requests

        VT_API_KEY = os.environ.get("VT_API_KEY")
        if not VT_API_KEY:
            print("Error: VT_API_KEY environment variable not set.")
            continue
        else:
            vt_url = f"https://www.virustotal.com/api/v3/ip_addresses/{ip_to_check}"
            headers = {
                "x-apikey": VT_API_KEY
            }
            try:
                response = requests.get(vt_url, headers=headers)
                if response.status_code == 200:
                    data = response.json()
                    malicious_votes = data.get('data', {}).get('attributes', {}).get('last_analysis_stats', {}).get('malicious', 0)
                    if malicious_votes > 0:
                        flagged_ips.append(ip_to_check)
                        print(f"IP {ip_to_check} is flagged as malicious with {malicious_votes} votes.")
                    else:
                        print(f"IP {ip_to_check} is clean.")
                else:
                    print(f"Failed to query Virustotal for IP {ip_to_check}: {response.status_code}")
            except Exception as e:
                print(f"Error querying Virustotal: {e}"))

# Create a rule to block the IP on a Debian router/firewall

# notify admin via email 