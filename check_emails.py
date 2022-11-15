import requests
from time import sleep
from pwned_api import api_url_base, headers, payload
from ingest_breach import ingest_email_breach

def check_emails():
    with open('emails_to_check.txt') as f:
        for line in f:
            account = line.replace("\n","")

            breach_url = f"{api_url_base}breachedaccount/{account}"
            response = requests.request("GET", breach_url, headers = headers, data = payload)
            if response.status_code == 200:
                print(f"Breaches found for account: {account}\n{response.json()}")
                ingest_email_breach(account, response.json(), "breach")
            elif response.status_code == 429:
                print("Too many requests")
            else:
                print(f"No breaches found for account: {account}")
            sleep (1.6)

            paste_url = f"{api_url_base}pasteaccount/{account}"
            response = requests.request("GET", paste_url, headers = headers, data = payload)

            if response.status_code == 200:
                print(f"Pastes found for account: {account}\n{response.json()}\n")
                ingest_email_breach(account, response.json(), "paste")
            elif response.status_code == 429:
                print("Too many requests\n")
            else:
                print(f"No pastes found for account: {account}\n")
            sleep(1.6)
    