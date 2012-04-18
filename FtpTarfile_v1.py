import os, sys, string,  socket
import tarfile
import time, datetime
from ftplib import FTP

class Ihaveuftp:
	def __init__(self, hostaddr, username, password, port=21):
		self.hostaddr = hostaddr
		self.username = username
		self.password = password
		self.port = port
		self.ftp = FTP()
#		self.ftp.set_debuglevel(2)
	def __del__(self):
		self.ftp.close()
#		self.ftp.set_debuglevel(0)


	def login(self):
		ftp = self.ftp
		try:
			timeout = 60
			socket.setdefaulttimeout(timeout)
			ftp.set_pasv(True)
			print 'start connect %s' %(self.hostaddr)
			ftp.connect(self.hostaddr, self.port)
			print 'success connect %s' %(self.hostaddr)
			print 'start login %s' %(self.hostaddr)
			ftp.login(self.username,self.password)
			print 'success login %s' %(self.hostaddr)
			print ftp.getwelcome()
#			debug_print(ftp.getwelcome())
		except Exception:
			print 'Falied'
#			deal_error("Failed")
	def upload(self, localdir, localfile):
		try:
			self.ftp.cwd(localdir)
		except:
			print "localdir no exist"
#		if not os.path.isdir(localdir):
#			os.makedirs(localdir)
#		self.ftp.cwd(localdir)
		file_handler = open(localfile, 'rb')
		self.ftp.storbinary('STOR %s' %localfile, file_handler)
		file_handler.close()
#		ftp.quit()

	def debug_print(s):
		print (s)


'''
	def deal_error(e):
		datenow = time.strftime('%Y%m%d')
 #		print datenow
 # 		timenow  = time.localtime()  
 #  	datenow  = time.strftime('%Y-%m-%d', timenow)  
    	logstr = '%s ERROR: %s' %(datenow, e)  
    	debug_print(logstr)  
    	file.write(logstr)  
    	sys.exit()
'''
if __name__ == '__main__':
	file = open("log.txt", "a")
#ftp
#	timenow = time.localtime()
#	datenow = time.strftime('%Y%m%d')
#	datenow = time.strftime('%Y-%m-%d', timenow)
#	logstr = datenow

	hostaddr = ''
	username = ''
	password = ''
	port = 21
	ftpbackup_file = ''


	f = Ihaveuftp(hostaddr, username, password, port)
	f.login()	
	f.upload(ftpbackup_file, tar_name1)

#	timenow = time.localtime()
#	datanow = time.strftime('%Y-%m-%d', timenow)
#	logstr += "= %s backup success\n" %datanow
#tar
	tar_name = "blog" + time.strftime('%Y%m%d') + '.tar.gz'
	tar = tarfile.open(tar_name,"w:gz")
	for name in ["/opt/c","/etc/passwd","/opt/zenir"]:
			tar.add(name)
	tar.close()
#	f.deal_error('TAR blogbackup file success!)
	file.write('TAR blogbackup file success!')
#rm
#	rm3days_cmd = 'find /opt/backup -name "blog2012*" -mtime +3 -exec rm {} \;'
	rm3days_cmd = 'find /opt/backup -name "blog2012*"  -exec rm {} \;'
	if os.system(rm3days_cmd) ==  0:
#		f.deal_error('rm backup files success!')
		file.write('rm backup files success!')
	else:
#		f.deal_error('rm backup files Failed')
		file.write('rm backup files Failed') 
#	file.write(logstr)
	file.close()
