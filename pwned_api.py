from config import PWNED_BASE_URL, PWNED_API_KEY

api_url_base = PWNED_BASE_URL
hibp_api_key = PWNED_API_KEY
payload = {}
headers = {
    'hibp-api-key': str(hibp_api_key),
    'format': 'application/json',
    'timeout': '2.5',
    'HIBP': str(hibp_api_key),
}