from ingest_breach import ingest_new_breach
from logscale_breach_list import logscale_breach_list
import requests

def add_new_breaches():
    ls_breach_list = logscale_breach_list()
    
    url = "https://haveibeenpwned.com/api/v3/breaches"
    pwned_breach_list = requests.get(url).json()
    
    for breach in pwned_breach_list:
        if breach["Name"] not in ls_breach_list.keys():
            try:
                if ls_breach_list[breach["Name"]] != breach["BreachDate"]:
                    ingest_new_breach(breach)
                else:
                    continue
            except:
                ingest_new_breach(breach)
