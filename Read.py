import string

def parseMessage(line):
	sep = line.split(":")
	username = sep[1].split("!")[0]
	message = sep[2][:-1]
	print(username,message)
	m = (username, message)
	print(m)
	return m