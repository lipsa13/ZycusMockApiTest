# Standard library imports...
try:
    from urllib.parse import urljoin
except ImportError:
    from urlparse import urljoin

# Third-party imports...
import requests
from customerApi.urlDetail import URL

Customer_URL = urljoin(URL,"/api/users/2")

def get_customer_details():
    """Get list of users"""
    response = requests.get(Customer_URL)
    if response.ok:
        return response
    else:
        return None


