import string
from Socket import sendMessage
def joinRoom(s):
	readbuffer = ""
	Loading = True
	while Loading:
		readbuffer = readbuffer + s.recv(1024).decode('utf-8')
		temp = readbuffer.split("\n")
		readbuffer = temp.pop()

		for line in temp:
			print(line)
			Loading = loadingComplete(line)
	sendMessage(s, "Successfully joined chat")
	s.setblocking(0)

def loadingComplete(line):
	if "End of /NAMES list" in line:
		return False
	return True