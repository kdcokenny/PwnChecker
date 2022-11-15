import requests
from pwned_api import api_url_base, headers, payload
from ingest_breach import ingest_domain_breach
from time import sleep

def check_domains():
    with open('domains_to_check.txt') as f:
        for line in f:
            domain = line.replace("\n","")

            api_url = f"{api_url_base}breaches?domain={domain}"
            response = requests.request("GET", api_url, headers = headers, data = payload)
            if response.json() != []:
                print(f"Breaches found for domain: {domain}\n{response.json()}\n")
                ingest_domain_breach(domain, response.json())
            elif response.status_code == 429:
                print("Too many requests\n")
            else:
                print(f"No breaches found for domain: {domain}\n")
            sleep (1.6)

