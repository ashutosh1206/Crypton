#! /usr/bin/python

from subprocess import Popen, PIPE
import shlex

blksz = 32
blocksize=blksz
cmd = shlex.split("python baby_crypt.py")


import socket
HOST,PORT = "localhost",1337
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect((HOST,PORT))
def r(input):
	
	#a = Popen(cmd, stdin=PIPE, stdout=PIPE)
	#b = a.communicate(input+"\n")
	#b=b[0][53:];	
	b = sock.recv(1024)
	sock.sendall(input)
	b = sock.recv(1024).split(":")[1].lstrip().strip();
	return repr(b.strip().lstrip())


def align(prefix):
	build = "" 
	while len(build) % blocksize != blocksize-len(prefix)-1:
		build = "a" + build;
	return build;

def chk(ali,bas,new):
	length = len(ali)+1+blksz
	#print str(length)
	return bas[:length]==new[:length]

def slv1(prefix):
	s = align(prefix)
	#print "tr="+s
	#print "ln="+str(len(s))
	base = (r(s))
	#print "base="+base
	for i in range(33,127): # Assume ASCIIi
		tr = s+prefix+ chr(i);
		#print "I="+str(i)
		#print "tr="+tr
		#print "ln="+str(len(tr))
		new = r(tr)
		#time.sleep(.01)
		#print " new="+new
		if chk(s,base,new):
			return chr(i);
	print("EXCEOPTIONNSONSONSONSON")	
	return None


#one = align("")
#print r(one)[:32]
#print r(one+'f')[:32]

#import sys
#sys.exit(1)
import time
retur = ""
while r != None:
	retur += slv1(retur)
	print repr(retur)
	#time.sleep(.1)
#print r(align(""))
#print r(align("")+'f')
#print r(align("")+'c')
#print r('a'*128)
#blksz = 32
#blocksize=32
#print r(align(""))
#print r(align("")+'f')
#print r(align("")+'c')

#print slv1("")
#print slv1("f")
#print(r("2"*blksz*22+"boop"))
