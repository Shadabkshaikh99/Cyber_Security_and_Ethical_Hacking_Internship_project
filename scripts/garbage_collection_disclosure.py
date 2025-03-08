# Information Disclosure of Garbage Collection Cycle

import requests

url = "http://localhost:3000/metrics"
response = requests.get(url)

if "garbage collection" in response.text:
    print("[+] Garbage collection info exposed!")
else:
    print("[-] No sensitive data found.")
