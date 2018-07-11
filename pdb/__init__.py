import requests

base_url = 'https://www.peeringdb.com/api/net'


def get_peer_info(asn=0):
    if asn == 0:
        return None
    params = {'asn': asn}
    r = requests.get(base_url, params)
    return r.json()
