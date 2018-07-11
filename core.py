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
    stdin, stdout, stderr = client.exec_command(cmd,get_pty=True)
    tmp = stdout.readlines()
    if len(tmp) > 0:
        return(''.join(tmp))
    else:
        return ("")


def getbgp():
    return("result")

@route('/')
def idx():
    return template('index', active="index", result="")

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
            # result += str(json) + "\n"
            cmd ="ansible-playbook /home/arista/tmp/peer-automation/playbook/eos.yml -i /home/arista/tmp/peer-automation/playbook/hosts -e my_asn=xxxxx -e remote_asn=yyyyy -e remote_ip=aaa.aaa.aaa.aaa -e ix_name=hogeix -e c_name=aaaaaaaa -e v4v6=v4 -e pass=secret > /tmp/test"
            ansible_remote_run(host, user, pw, cmd)
            cmd = "cat /tmp/test"
            result += ansible_remote_run(host, user, pw, cmd)

        elif ipv == "6":
            # result += str(json) + "\n"
            cmd ="ansible-playbook /home/arista/tmp/peer-automation/playbook/eos.yml -i /home/arista/tmp/peer-automation/playbook/hosts -e my_asn=xxxxx -e remote_asn=yyyyy -e remote_ip=aaa.aaa.aaa.aaa -e ix_name=hogeix -e c_name=aaaaaaaa -e v4v6=v4 -e pass=secret"
            result += ansible_remote_run(host, user, pw, cmd)

    return template('index', active="index", result=result)



run(host='0.0.0.0', port=8080, debug=True)