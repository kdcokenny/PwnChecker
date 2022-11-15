# PwnChecker - Automated Email and Domain Breach Checking
PwnChecker helps you keep your data safe by checking if your emails and/or domains have been exposed to a data breach every 24 hours.

## Prerequisites
1. [Falcon Logscale (Humio) repository](https://www.crowdstrike.com/products/observability/falcon-logscale/)
2. Default  Ingestion Token | [Learn how to create a default ingestion token.](https://library.humio.com/humio-server/ingesting-data-tokens.html)
3. [HaveIBeenPwned Active API Key](https://haveibeenpwned.com/API/v3)
4. Python3 installed | [Link to python download page](https://www.python.org/downloads/)

## Quick Start
Download files and open "config.py". Input all data that contains empty strings. Once the information has been entered, select the pwnchecker folder in the terminal and run ```nohup python3 main.py &```. This will run PwnChecker in the background, just make sure to re-run the prgram again whenever the machine is restarted.

## Adding/Removing Domains
Add a new line with the domain to check in the file, "domains_to_check.txt". If you want to remove a domain, simply remove the line containing the domain.

## Adding/Removing Emails
Add a new line with the email to check in the file, "emails_to_check.txt". If you want to remove an email, simply remove the line containing the email.
