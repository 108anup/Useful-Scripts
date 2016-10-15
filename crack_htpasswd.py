#Usage: $python crack_htpasswd.py <encrypted-string> <salt>
#Note: the First 2 characters of the String Encrypted using htpasswd or crypt(3) (LINUX MAN) represent the salt.

from sys import argv
from crypt import crypt

def generate_strings(length, s):

	if(not found):
		if(length == 0):
			#print s;
			if(crypt(s,salt)[len(salt):]==chckstring):
				global found 
				found = True
				global cracked
				cracked = s
		
		else:
			for i in range(0,26):
				app_s = s+alphabets[i]
				generate_strings(length-1,app_s);
				

alphabets = ['a',  'b',  'c',  'd',  'e',  'f',  'g',  'h',  'i',  'j',  'k',  'l',  'm',  'n',  'o',  'p',  'q',  'r',  's',  't',  'u',  'v',  'w',  'x',  'y',  'z']
chckstring = argv[1]
found = False
cracked = ""
salt = argv[2]	
i = 1	
while(not found):
	print "Attempting with length = ",i
	generate_strings(i,"")
	i+=1
else:
	print chckstring,cracked
