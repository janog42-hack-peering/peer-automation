# playbook

```
ansible-playbook eos.yml -i hosts \
  -e my_asn=xxxxx \
  -e remote_asn=yyyyy \
  -e remote_ip=aaa.aaa.aaa.aaa \
  -e ix_name=hogeix \
  -e c_name=aaaaaaaa \
  -e v4v6=v4 \
  -e pass=secret
```
