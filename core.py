from bottle import route, run,template,post,request
from pdb import get_peer_info
import paramiko
from paramiko import SSHClient

host="35.201.2.132"
user="arista"
pw="arista123"

def ansible_remote_run(host,user,password,cmd):
    client = SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, username=user, password=password)
    stdin, stdout, stderr = client.exec_command(cmd)
    return(stdout.readlines()[0])


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
        if ipv == "4":
            result += str(json) + "\n"
            # cmd ="echo 1"
            # result += ansible_remote_run(host, user, pw, cmd)

        elif ipv == "6":
            result += str(json) + "\n"
            # cmd ="echo 1"
            # result += ansible_remote_run(host, user, pw, cmd)



    return(result)

run(host='0.0.0.0', port=8080, debug=True)