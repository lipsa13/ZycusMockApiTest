import requests
import uuid

#local imports
from customerApi.urlDetail import URL

def post_customers(fst_name,lst_name,contact ):
    headers = {
        "Authorization": "/api/users " + URL,
    }
    body = {
        "fst_name": fst_name,
        "lst_name": lst_name,
        "contact": contact,
        "uid":str(uuid.uuid4()),
    }
response = requests.post(
        json=body,
        headers=headers,
        timeout=timeout,
    )

