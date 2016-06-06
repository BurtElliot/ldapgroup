import json,urllib
import ldap
import logging

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

## konek ldap server
## first you must open a connection to the server
try:
	l = ldap.open("127.0.0.1")
	l.protocol_version = ldap.VERSION3	
except Exception as e:
	logeror.error(e)

#update anggota semua dosen

den = "top"
cari = "objectClass="+den

baseDN = "cn=semua_dosen,ou=group,dc=maxcrc,dc=com"
searchScope = ldap.SCOPE_SUBTREE
retrieveAttributes = None 
searchFilter = cari

sama = 0
ubah = 0

try:
	ldap_result_id = l.search(baseDN, searchScope, searchFilter, retrieveAttributes)
except Exception as e:
	logeror.error(e)

try:
	while 1:
		result_type, result_data = l.result(ldap_result_id, 0)
		if (result_data == []):
			print "tidak ada"
			break;
		else:
			## here you don't have to append to a list
			## you could do whatever you want with the individual entry
			## The appending to list is just for illustration. 
			if result_type == ldap.RES_SEARCH_ENTRY:
				
				#print result_data
				#print " "
				#print result_data[0][1]['member'][0]
				for y in result_data[0][1]['member']:
					#listLDAP.append(y)
					#print listLDAP
					#print y
					for z in output['data']['dosen']:
						a="uid=" + z['uid'] + "," + "ou=people,dc=maxcrc,dc=com"
						if a == y:
							sama=1
							break
						else:
							sama=0
					if sama == 0:
						# Open a connection
						l = ldap.initialize("ldap://localhost:389/")

						# Bind/authenticate with a user with apropriate rights to add objects
						l.simple_bind_s("cn=manager,dc=maxcrc,dc=com","secret")
						delet = [(ldap.MOD_DELETE, 'member', y)]
						l.modify_s('cn=semua_dosen,ou=group,dc=maxcrc,dc=com', delet)
						#print y+" "+"berhasil dipindahkan dari semua dosen"
						logger.info(y+" "+"berhasil di hapus dari semua dosen")
						ubah=+1
			break
	#if sama == 1:
	#	print "tidak ada perubahan data di semua dosen"
		#logger.info("tidak ada yang pindahkan dari semua dosen")
	l.unbind_s()
except Exception as e:
	logeror.error(e)

#update anggota semua tendik
try:
	l = ldap.open("127.0.0.1")
	l.protocol_version = ldap.VERSION3	
except ldap.LDAPError, e:
	print e

den = "top"
cari = "objectClass="+den

baseDN = "cn=semua_tendik,ou=group,dc=maxcrc,dc=com"
searchScope = ldap.SCOPE_SUBTREE
retrieveAttributes = None 
searchFilter = cari

sama = 0

ldap_result_id = l.search(baseDN, searchScope, searchFilter, retrieveAttributes)

try:
	while 1:
		result_type, result_data = l.result(ldap_result_id, 0)
		if (result_data == []):
			print "tidak ada"
			break;
		else:
			## here you don't have to append to a list
			## you could do whatever you want with the individual entry
			## The appending to list is just for illustration. 
			if result_type == ldap.RES_SEARCH_ENTRY:
				
				#print result_data
				#print " "
				#print result_data[0][1]['member'][0]
				for y in result_data[0][1]['member']:
					#listLDAP.append(y)
					#print listLDAP
					#print y
					for z in output['data']['tendik']:
						a="uid=" + z['uid'] + "," + "ou=people,dc=maxcrc,dc=com"
						if a == y:
							sama=1
							break
						else:
								sama=0
					if sama == 0:
						# Open a connection
						l = ldap.initialize("ldap://localhost:389/")

						# Bind/authenticate with a user with apropriate rights to add objects
						l.simple_bind_s("cn=manager,dc=maxcrc,dc=com","secret")
						delet = [(ldap.MOD_DELETE, 'member', y)]
						l.modify_s('cn=semua_tendik,ou=group,dc=maxcrc,dc=com', delet)
						#print y+" "+"berhasil dipindahkan dari semua tendik" 
						logger.info(y+" "+"berhasil di hapus dari semua tendik")
						ubah=+1
			break
	#if sama == 1:
	#	print "tidak ada perubahan data di semua tendik"
		#logger.info("tidak ada yang dipindahkan dari semua tendik")
	l.unbind_s()
except Exception as e:
	logeror.error(e)

#update anggota kajur

try:
	l = ldap.open("127.0.0.1")
	l.protocol_version = ldap.VERSION3	
except ldap.LDAPError, e:
	print e

den = "top"
cari = "objectClass="+den

baseDN = "cn=semua_kajur,ou=group,dc=maxcrc,dc=com"
searchScope = ldap.SCOPE_SUBTREE
retrieveAttributes = None 
searchFilter = cari

sama = 0

try:
	ldap_result_id = l.search(baseDN, searchScope, searchFilter, retrieveAttributes)
except Exception as e:
	logeror.error(e)

try:
	while 1:
		result_type, result_data = l.result(ldap_result_id, 0)
		if (result_data == []):
			print "tidak ada"
			break;
		else:
			## here you don't have to append to a list
			## you could do whatever you want with the individual entry
			## The appending to list is just for illustration. 
			if result_type == ldap.RES_SEARCH_ENTRY:
				
				#print result_data
				#print " "
				#print result_data[0][1]['member'][0]
				for y in result_data[0][1]['member']:
					#listLDAP.append(y)
					#print listLDAP
					#print y
					for z in output['data']['dosen']:
						if z['jabatan'] == "1":
							a="uid=" + z['uid'] + "," + "ou=people,dc=maxcrc,dc=com"
							if a == y:
								sama=1
								break
							else:
									sama=0
					if sama == 0:
						# Open a connection
						l = ldap.initialize("ldap://localhost:389/")

						# Bind/authenticate with a user with apropriate rights to add objects
						l.simple_bind_s("cn=manager,dc=maxcrc,dc=com","secret")
						delet = [(ldap.MOD_DELETE, 'member', y)]
						l.modify_s('cn=semua_kajur,ou=group,dc=maxcrc,dc=com', delet)
						#print y+" "+"berhasil dipindahkan dari dosen_FT"
						logger.info(y+" "+"berhasil di hapus dari semua_kajur")
						ubah=+1
			break
	#if sama == 1:
		#print "tidak ada perubahan data di dosen FT"
		#logger.info("tidak ada yang dipindahkan dari dosen FT")
	l.unbind_s()
except Exception as e:
	logeror.error(e)

#update anggota dekan

try:
	l = ldap.open("127.0.0.1")
	l.protocol_version = ldap.VERSION3	
except ldap.LDAPError, e:
	print e

den = "top"
cari = "objectClass="+den

baseDN = "cn=semua_dekan,ou=group,dc=maxcrc,dc=com"
searchScope = ldap.SCOPE_SUBTREE
retrieveAttributes = None 
searchFilter = cari

sama = 0

try:
	ldap_result_id = l.search(baseDN, searchScope, searchFilter, retrieveAttributes)
except Exception as e:
	logeror.error(e)

try:
	while 1:
		result_type, result_data = l.result(ldap_result_id, 0)
		if (result_data == []):
			print "tidak ada"
			break;
		else:
			## here you don't have to append to a list
			## you could do whatever you want with the individual entry
			## The appending to list is just for illustration. 
			if result_type == ldap.RES_SEARCH_ENTRY:
				
				#print result_data
				#print " "
				#print result_data[0][1]['member'][0]
				for y in result_data[0][1]['member']:
					#listLDAP.append(y)
					#print listLDAP
					#print y
					for z in output['data']['dosen']:
						if z['jabatan'] == "2":
							a="uid=" + z['uid'] + "," + "ou=people,dc=maxcrc,dc=com"
							if a == y:
								sama=1
								break
							else:
									sama=0
					if sama == 0:
						# Open a connection
						l = ldap.initialize("ldap://localhost:389/")

						# Bind/authenticate with a user with apropriate rights to add objects
						l.simple_bind_s("cn=manager,dc=maxcrc,dc=com","secret")
						delet = [(ldap.MOD_DELETE, 'member', y)]
						l.modify_s('cn=semua_dekan,ou=group,dc=maxcrc,dc=com', delet)
						#print y+" "+"berhasil dipindahkan dari dosen_FT"
						logger.info(y+" "+"berhasil di hapus dari semua_dekan")
						ubah=+1
			break
	#if sama == 1:
		#print "tidak ada perubahan data di dosen FT"
		#logger.info("tidak ada yang dipindahkan dari dosen FT")
	l.unbind_s()
except Exception as e:
	logeror.error(e)


#update anggota dosen teknik

try:
	l = ldap.open("127.0.0.1")
	l.protocol_version = ldap.VERSION3	
except ldap.LDAPError, e:
	print e

den = "top"
cari = "objectClass="+den

baseDN = "cn=dosen_FT,ou=group,dc=maxcrc,dc=com"
searchScope = ldap.SCOPE_SUBTREE
retrieveAttributes = None 
searchFilter = cari

sama = 0

try:
	ldap_result_id = l.search(baseDN, searchScope, searchFilter, retrieveAttributes)
except Exception as e:
	logeror.error(e)

try:
	while 1:
		result_type, result_data = l.result(ldap_result_id, 0)
		if (result_data == []):
			print "tidak ada"
			break;
		else:
			## here you don't have to append to a list
			## you could do whatever you want with the individual entry
			## The appending to list is just for illustration. 
			if result_type == ldap.RES_SEARCH_ENTRY:
				
				#print result_data
				#print " "
				#print result_data[0][1]['member'][0]
				for y in result_data[0][1]['member']:
					#listLDAP.append(y)
					#print listLDAP
					#print y
					for z in output['data']['dosen']:
						if z['homebase'] == "TE" or z['homebase'] == "TF":
							a="uid=" + z['uid'] + "," + "ou=people,dc=maxcrc,dc=com"
							if a == y:
								sama=1
								break
							else:
									sama=0
					if sama == 0:
						# Open a connection
						l = ldap.initialize("ldap://localhost:389/")

						# Bind/authenticate with a user with apropriate rights to add objects
						l.simple_bind_s("cn=manager,dc=maxcrc,dc=com","secret")
						delet = [(ldap.MOD_DELETE, 'member', y)]
						l.modify_s('cn=dosen_FT,ou=group,dc=maxcrc,dc=com', delet)
						#print y+" "+"berhasil dipindahkan dari dosen_FT"
						logger.info(y+" "+"berhasil di hapus dari dosen FT")
						ubah=+1
			break
	#if sama == 1:
		#print "tidak ada perubahan data di dosen FT"
		#logger.info("tidak ada yang dipindahkan dari dosen FT")
	l.unbind_s()
except Exception as e:
	logeror.error(e)
#update dosen FIK

try:
	l = ldap.open("127.0.0.1")
	l.protocol_version = ldap.VERSION3	
except ldap.LDAPError, e:
	print e

den = "top"
cari = "objectClass="+den

baseDN = "cn=dosen_FIK,ou=group,dc=maxcrc,dc=com"
searchScope = ldap.SCOPE_SUBTREE
retrieveAttributes = None 
searchFilter = cari

sama = 0

ldap_result_id = l.search(baseDN, searchScope, searchFilter, retrieveAttributes)

try:
	while 1:
		result_type, result_data = l.result(ldap_result_id, 0)
		if (result_data == []):
			print "tidak ada"
			break;
		else:
			## here you don't have to append to a list
			## you could do whatever you want with the individual entry
			## The appending to list is just for illustration. 
			if result_type == ldap.RES_SEARCH_ENTRY:
				
				#print result_data
				#print " "
				#print result_data[0][1]['member'][0]
				for y in result_data[0][1]['member']:
					#listLDAP.append(y)
					#print listLDAP
					#print y
					for z in output['data']['dosen']:
						if z['homebase'] == "IT":
							a="uid=" + z['uid'] + "," + "ou=people,dc=maxcrc,dc=com"
							if a == y:
								sama=1
								break
							else:
								sama=0
					if sama == 0:
						# Open a connection
						l = ldap.initialize("ldap://localhost:389/")

						# Bind/authenticate with a user with apropriate rights to add objects
						l.simple_bind_s("cn=manager,dc=maxcrc,dc=com","secret")
						delet = [(ldap.MOD_DELETE, 'member', y)]
						l.modify_s('cn=dosen_FIK,ou=group,dc=maxcrc,dc=com', delet)
						#print y+" "+"berhasil dipindahkan dari dosen FIK"
						logger.info(y+" "+"berhasil di hapus dari dosen FIK")
						ubah+=1
			break
	#if sama == 1:
	#	print "tidak ada perubahan data di dosen FIK"
	#	logger.info("tidak ada perubahan data di dosen FIK")
		#logger.info("tidak ada yang dipindahkan dari dosen FIK")
	l.unbind_s()
except Exception as e:
	logeror.error(e)

if ubah == 0:
	#print "tidak ada anggota yang dihapus"
	logger.info("tidak ada anggota yang dihapus")

#MENAMBAH ANGGOTA BARU

# The dn of our new entry/object
dn = "cn=semua_dosen,ou=group,dc=maxcrc,dc=com" 
dn2 = "cn=semua_tendik,ou=group,dc=maxcrc,dc=com"
dn3 = "cn=dosen_FIK,ou=group,dc=maxcrc,dc=com"
dn4 = "cn=dosen_FT,ou=group,dc=maxcrc,dc=com"
dn5 = "cn=semua_kajur,ou=group,dc=maxcrc,dc=com"
dn6 = "cn=semua_dekan,ou=group,dc=maxcrc,dc=com"

iki = []
ika = []

ada = 0


#menambah anggota ke grup semua tendik
try:
	for y in output['data']['tendik']:	
		l = ldap.open("127.0.0.1")
		l.protocol_version = ldap.VERSION3
		den = "uid=" + y['uid'] + "," + "ou=people,dc=maxcrc,dc=com"
		cari = "member="+den
		baseDN = "cn=semua_tendik,ou=group,dc=maxcrc,dc=com"
		searchScope = ldap.SCOPE_SUBTREE
		retrieveAttributes = None 
		searchFilter = cari			
		ldap_result_id = l.search(baseDN, searchScope, searchFilter, retrieveAttributes)
		
		while 1:
			result_type, result_data = l.result(ldap_result_id, 0)
			if (result_data == []):
				
				tendik = (str("uid=" + y['uid'] + "," + "ou=people,dc=maxcrc,dc=com"))
				
				# Open a connection
				l = ldap.initialize("ldap://localhost:389/")

				# Bind/authenticate with a user with apropriate rights to add objects
				l.simple_bind_s("cn=manager,dc=maxcrc,dc=com","secret")
				ika = [(ldap.MOD_ADD, 'member', tendik)]

				l.modify_s(dn2,ika)
				#print y['uid']+" berhasil ditambahkan ke grup semua tendik"
				logger.info(y['uid']+" "+"berhasil ditambahkan ke grup semua tendik")
				ada+=1
				break
			else:
				#print y['uid']+" sudah ada di group semua tendik"
				break
except Exception as e:
	logeror.error(e)

#menambah anggota baru ke semua dosen
try:
	for y in output['data']['dosen']:	
		l = ldap.open("127.0.0.1")
		l.protocol_version = ldap.VERSION3	
		den = "uid=" + y['uid'] + "," + "ou=people,dc=maxcrc,dc=com"
		cari = "member="+den
		baseDN = "cn=semua_dosen,ou=group,dc=maxcrc,dc=com"
		searchScope = ldap.SCOPE_SUBTREE
		retrieveAttributes = None 
		searchFilter = cari			
		ldap_result_id = l.search(baseDN, searchScope, searchFilter, retrieveAttributes)
		
		while 1:
			result_type, result_data = l.result(ldap_result_id, 0)
			if (result_data == []):
				
				dosen = (str("uid=" + y['uid'] + "," + "ou=people,dc=maxcrc,dc=com"))
				
				# Open a connection
				l = ldap.initialize("ldap://localhost:389/")

				# Bind/authenticate with a user with apropriate rights to add objects
				l.simple_bind_s("cn=manager,dc=maxcrc,dc=com","secret")
				ika = [(ldap.MOD_ADD, 'member', dosen)]

				l.modify_s(dn,ika)
				#print y['uid']+" berhasil ditambahkan ke grup semua dosen"
				logger.info(y['uid']+" "+"berhasil ditambahkan ke grup semua dosen")
				ada+=1
				break
			else:
				#print y['uid']+" sudah ada di group semua dosen"
				break
except Exception as e:
	logeror.error(e)

#menambah anggo baru di group dosen fak teknik
try:
	for y in output['data']['dosen']:
		if y['homebase'] == "TE" or y['homebase'] == "TF" :
			l = ldap.open("127.0.0.1")
			l.protocol_version = ldap.VERSION3	
			den = "uid=" + y['uid'] + "," + "ou=people,dc=maxcrc,dc=com"
			cari = "member="+den
			baseDN = "cn=dosen_FT,ou=group,dc=maxcrc,dc=com"
			searchScope = ldap.SCOPE_SUBTREE
			retrieveAttributes = None 
			searchFilter = cari			
			ldap_result_id = l.search(baseDN, searchScope, searchFilter, retrieveAttributes)
			
			while 1:
				result_type, result_data = l.result(ldap_result_id, 0)
				if (result_data == []):
					
					dosenFT = (str("uid=" + y['uid'] + "," + "ou=people,dc=maxcrc,dc=com"))
					
					# Open a connection
					l = ldap.initialize("ldap://localhost:389/")

					# Bind/authenticate with a user with apropriate rights to add objects
					l.simple_bind_s("cn=manager,dc=maxcrc,dc=com","secret")
					ika = [(ldap.MOD_ADD, 'member', dosenFT)]

					l.modify_s(dn4,ika)
					#print y['uid']+" berhasil ditambahkan ke dosen_FT"
					logger.info(y['uid']+" "+"berhasil ditambahkan ke grup semua dosen_FT")
					ada+=1
					break
				else:
					#print y['uid']+" sudah ada di grup dosen FT"
					break

#menaambahkan anggota baru di dosen fak Informasi Komunikasi
		elif y['homebase'] == "IT" :
			l = ldap.open("127.0.0.1")
			l.protocol_version = ldap.VERSION3	
			den = "uid=" + y['uid'] + "," + "ou=people,dc=maxcrc,dc=com"
			cari = "member="+den
			baseDN = "cn=dosen_FIK,ou=group,dc=maxcrc,dc=com"
			searchScope = ldap.SCOPE_SUBTREE
			retrieveAttributes = None 
			searchFilter = cari		
			ldap_result_id = l.search(baseDN, searchScope, searchFilter, retrieveAttributes)

			
			while 1:
				result_type, result_data = l.result(ldap_result_id, 0)
				if (result_data == []):
					
					dosenFIK = (str("uid=" + y['uid'] + "," + "ou=people,dc=maxcrc,dc=com"))
					
					# Open a connection
					l = ldap.initialize("ldap://localhost:389/")

					# Bind/authenticate with a user with apropriate rights to add objects
					l.simple_bind_s("cn=manager,dc=maxcrc,dc=com","secret")
					iki = [(ldap.MOD_ADD, 'member', dosenFIK)]
					l.modify_s(dn3,iki)
					#print y['uid']+" berhasil ditambahkan ke dosen_FIK"
					logger.info(y['uid']+" "+"berhasil ditambahkan ke grup semua dosen_FIK")				
					ada+=1
					break
				else:
					#print y['uid']+" sudah ada di grup semua FIK"
					break
	
	l.unbind_s()
except Exception as e:
	logger.error(e)

#menambah anggota baru di group semua kajur
try:
	for y in output['data']['dosen']:
		if y['jabatan'] == "1" :
			l = ldap.open("127.0.0.1")
			l.protocol_version = ldap.VERSION3	
			den = "uid=" + y['uid'] + "," + "ou=people,dc=maxcrc,dc=com"
			cari = "member="+den
			baseDN = "cn=semua_kajur,ou=group,dc=maxcrc,dc=com"
			searchScope = ldap.SCOPE_SUBTREE
			retrieveAttributes = None 
			searchFilter = cari			
			ldap_result_id = l.search(baseDN, searchScope, searchFilter, retrieveAttributes)
			
			while 1:
				result_type, result_data = l.result(ldap_result_id, 0)
				if (result_data == []):
					
					kajur = (str("uid=" + y['uid'] + "," + "ou=people,dc=maxcrc,dc=com"))
					
					# Open a connection
					l = ldap.initialize("ldap://localhost:389/")

					# Bind/authenticate with a user with apropriate rights to add objects
					l.simple_bind_s("cn=manager,dc=maxcrc,dc=com","secret")
					ika = [(ldap.MOD_ADD, 'member', kajur)]

					l.modify_s(dn5,ika)
					#print y['uid']+" berhasil ditambahkan ke dosen_FT"
					logger.info(y['uid']+" "+"berhasil ditambahkan ke grup semua kajur")
					ada+=1
					break
				else:
					#print y['uid']+" sudah ada di grup dosen FT"
					break

#menambah anggota baru di group semua dekan
		elif y['jabatan'] == "2" :
			l = ldap.open("127.0.0.1")
			l.protocol_version = ldap.VERSION3	
			den = "uid=" + y['uid'] + "," + "ou=people,dc=maxcrc,dc=com"
			cari = "member="+den
			baseDN = "cn=semua_dekan,ou=group,dc=maxcrc,dc=com"
			searchScope = ldap.SCOPE_SUBTREE
			retrieveAttributes = None 
			searchFilter = cari			
			ldap_result_id = l.search(baseDN, searchScope, searchFilter, retrieveAttributes)
			
			while 1:
				result_type, result_data = l.result(ldap_result_id, 0)
				if (result_data == []):
					
					dekan = (str("uid=" + y['uid'] + "," + "ou=people,dc=maxcrc,dc=com"))
					
					# Open a connection
					l = ldap.initialize("ldap://localhost:389/")

					# Bind/authenticate with a user with apropriate rights to add objects
					l.simple_bind_s("cn=manager,dc=maxcrc,dc=com","secret")
					ika = [(ldap.MOD_ADD, 'member', dekan)]

					l.modify_s(dn6,ika)
					#print y['uid']+" berhasil ditambahkan ke dosen_FT"
					logger.info(y['uid']+" "+"berhasil ditambahkan ke grup semua dekan")
					ada+=1
					break
				else:
					#print y['uid']+" sudah ada di grup dosen FT"
					break
	l.unbind_s()
except Exception as e:
	logger.error(e)


if ada == 0:
	logger.info("tidak ada data baru")

