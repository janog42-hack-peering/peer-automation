from bottle import route, run
from socket import gethostname, gethostbyname

def bgpsummary():
    return("result")


@route('/bgp')
def bgp():
    return("TEST")

run(host='localhost', port=8080, debug=True)