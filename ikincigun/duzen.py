#apt install python-ldap

import ldap
import ldap.modlist as modlist

l = ldap.open("192.168.59.4")
l.protocol_version = ldap.VERSION3	
username = "cn=alorak,dc=pardus,dc=lab"
password  = "secret"
l.simple_bind(username, password)

dn="cn=ornek01,ou=iki,dc=pardus,dc=lab" 
old = {'sn':'soyad'}
new = {'sn':'degismissoyad'}

ldif = modlist.modifyModlist(old,new)

l.modify_s(dn,ldif)
l.unbind_s()
