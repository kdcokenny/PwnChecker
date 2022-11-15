from logscale_api import client
from get_iso_date import get_iso_date

def ingest_domain_breach(domain, breaches):
    structured_data = [
        {
            "tags": {"breached": "true", "type": "domain"},
            "events": [
                {
                    "timestamp": get_iso_date(),
                    "attributes": {"Domain": domain, "Breaches": breaches}
                }
            ]
        }
    ]
    client.ingest_json_data(structured_data)

def ingest_email_breach(account, breaches, type):
    structured_data = [
        {
            "tags": {"breached": "true", "type": type},
            "events": [
                {
                    "timestamp": get_iso_date(),
                    "attributes": {"Email": account, "Breaches": breaches}
                }
            ]
        }
    ]
    client.ingest_json_data(structured_data)
    
def ingest_new_breach(breach_data):
    structured_data = [
        {
            "tags": {"type": "storage"},
            "events": [
                {
                    "timestamp": get_iso_date(),
                    "attributes": {"breach_info": breach_data}
                }
            ]
        }
    ]
    client.ingest_json_data(structured_data)