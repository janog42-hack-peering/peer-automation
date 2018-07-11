from bottle import route, run,template,post,request
from pdb import get_peer_info

def getbgp():
    return("result")

@route('/')
def idx():
    return template('index', active="index")

@route('/manage')
def manage():
    return template('manage', active="manage")

@post('/auto')
def auto():
    target = request.forms.TARGET
    asn = request.forms.ASN
    ix_id = request.forms.IXID
    password = request.forms.PASSWORD
    inpolicy = request.forms.INPOLICY
    ipv = request.forms.IPV
    result = ""

    for json in get_peer_info(int(asn),int(ix_id)):
        result += "OK"

    return(result)

run(host='0.0.0.0', port=8080, debug=True)