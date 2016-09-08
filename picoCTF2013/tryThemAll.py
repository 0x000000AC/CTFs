'''
pico-ctf-2013 - try-them-all

Hint:
You have found a passwd file containing salted passwords. An unprotected configuration 
file has revealed a salt of 5948. The hashed password for the 'admin' user appears to be 
02ed2bf40532f187ec9334ef37f75591, try to brute force this password.

Answer:
The linux standard dictionary passwords text file is used to check

'''
import sys, os, md5

# Open the newline delimited password file, split the contents into a list which
# will be md5 hashed with the salt and compared to the hashed password
while True:
	filename = raw_input("Please enter filename in current directory to open : ")
	try:
		contents = open(filename,'r').read().splitlines()
		break
	except OSError as err:
		print "OS error: {0}".format(err)
	except:
		print "File name invalid or file doesn't exist"


for item in contents:
	if(md5.new(item + "5948").hexdigest() == "02ed2bf40532f187ec9334ef37f75591"):
		print item

