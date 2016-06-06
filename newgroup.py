import json,urllib
import ldap
import ldap.modlist as modlist
import logging

from collections import namedtuple

#setting log
logger = logging.getLogger('info')
logger.setLevel(logging.INFO)

logeror = logging.getLogger('error')
logeror.setLevel(logging.ERROR)

# create a file handler

handler = logging.FileHandler('update.log')
handler.setLevel(logging.INFO)

errorhandler = logging.FileHandler('error.log')
errorhandler.setLevel(logging.ERROR)

# create a logging format

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

errorformatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
errorhandler.setFormatter(errorformatter)

# add the handlers to the logger

logeror.addHandler(errorhandler)
logger.addHandler(handler)

try:
	data = urllib.urlopen("http://localhost/jsonpy/son.json").read()
	output = json.loads(data)
except Exception as e:
	logeror.error(e)

user = []
dosen = []
tendik = []
dosenFT = []
dosenFIK = []
kajur = [] #kode jabatan = 1
dekan = [] #kode jabatan = 2

try:
	for y in output['data']['dosen']:
		user.append(str("uid=" + y['uid'] + "," + "ou=people,dc=maxcrc,dc=com"))
except Exception as e:
	logeror.error(e)

try:
	for y in output['data']['tendik']:
		tendik.append(str("uid=" + y['uid'] + "," + "ou=people,dc=maxcrc,dc=com"))
except Exception as e:
	logeror.error(e)

try:
	for y in output['data']['dosen']:
		if y['homebase'] == "TE" or y['homebase'] == "TF" :
			dosenFT.append(str("uid=" + y['uid'] + "," + "ou=people,dc=maxcrc,dc=com"))
		elif y['homebase'] == "IT" :
			dosenFIK.append(str("uid=" + y['uid'] + "," + "ou=people,dc=maxcrc,dc=com"))
except Exception as e:
	logeror.error(e)

try:
	for y in output['data']['dosen']:
		if y['jabatan'] == "1" :
			kajur.append(str("uid=" + y['uid'] + "," + "ou=people,dc=maxcrc,dc=com"))
		elif y['jabatan'] == "2" :
			dekan.append(str("uid=" + y['uid'] + "," + "ou=people,dc=maxcrc,dc=com"))
except Exception as e:
	logeror.error(e)

try:
	# Open a connection
	l = ldap.initialize("ldap://localhost:389/")
except Exception as e:
	logeror.error(e)

try:
	# Bind/authenticate with a user with apropriate rights to add objects
	l.simple_bind_s("cn=manager,dc=maxcrc,dc=com","secret")
except Exception as e:
	logeror.error(e)

# The dn of our new entry/object
dn = "cn=semua_dosen,ou=group,dc=maxcrc,dc=com" 
dn2 = "cn=semua_tendik,ou=group,dc=maxcrc,dc=com"
dn3 = "cn=dosen_FIK,ou=group,dc=maxcrc,dc=com"
dn4 = "cn=dosen_FT,ou=group,dc=maxcrc,dc=com"
dn5 = "cn=semua_kajur,ou=group,dc=maxcrc,dc=com"
dn6 = "cn=semua_dekan,ou=group,dc=maxcrc,dc=com"

# A dict to help build the "body" of the object
attrs = {}
attrs['objectclass'] = ['top','groupofnames']
attrs['member'] = user
attrs['description'] = 'group untuk semua dosen'

attrs2 = {}
attrs2['objectclass'] = ['top','groupofnames']
attrs2['member'] = tendik
attrs2['description'] = 'group untuk semua tendik'

attrs3 = {}
attrs3['objectclass'] = ['top','groupofnames']
attrs3['member'] = dosenFIK
attrs3['description'] = 'group untuk semua dosen FIK'

attrs4 = {}
attrs4['objectclass'] = ['top','groupofnames']
attrs4['member'] = dosenFT
attrs4['description'] = 'group untuk semua dosen FT'

attrs5 = {}
attrs5['objectclass'] = ['top','groupofnames']
attrs5['member'] = kajur
attrs5['description'] = 'group untuk semua kajur'

attrs6 = {}
attrs6['objectclass'] = ['top','groupofnames']
attrs6['member'] = dekan
attrs6['description'] = 'group untuk semua dekan'

# Convert our dict to nice syntax for the add-function using modlist-module
ldif = modlist.addModlist(attrs)
ldif2 = modlist.addModlist(attrs2)
ldif3 = modlist.addModlist(attrs3)
ldif4 = modlist.addModlist(attrs4)
ldif5 = modlist.addModlist(attrs5)
ldif6 = modlist.addModlist(attrs6)

# Do the actual synchronous add-operation to the ldapserver
try:
	l.add_s(dn,ldif)
except Exception as e:
	logeror.error(e)

try:
	l.add_s(dn2,ldif2)
except Exception as e:
	logeror.error(e)

try:
	l.add_s(dn3,ldif3)
except Exception as e:
	logeror.error(e)

try:
	l.add_s(dn4,ldif4)
except Exception as e:
	logeror.error(e)

try:
	l.add_s(dn5,ldif5)
except Exception as e:
	logeror.error(e)

try:
	l.add_s(dn6,ldif6)
except Exception as e:
	logeror.error(e)

logger.info(attrs['description']+" "+"telah berhasil dibuat")
logger.info(attrs2['description']+" "+"telah berhasil dibuat")
logger.info(attrs3['description']+" "+"telah berhasil dibuat")
logger.info(attrs4['description']+" "+"telah berhasil dibuat")
logger.info(attrs5['description']+" "+"telah berhasil dibuat")
logger.info(attrs6['description']+" "+"telah berhasil dibuat")

# Its nice to the server to disconnect and free resources when done
l.unbind_s()