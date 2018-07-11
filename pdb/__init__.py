import requests

base_url = 'https://www.peeringdb.com/api/'


def get_peer_info(asn=0, ix_id=0):
    if asn == 0 or ix_id == 0:
        return None
    params = {'asn': asn}
    r = requests.get(base_url+'net', params)
    id = r.json()['data'][0]['id']
    r = requests.get(base_url+'net/'+str(id))
    for ix in r.json()['data'][0]['netixlan_set']:
        if ix['ix_id'] == ix_id:
            return ix
