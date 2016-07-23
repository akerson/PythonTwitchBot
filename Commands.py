from Socket import openSocket, sendMessage

s = openSocket()

def checkforcommands(s,m):
	command = m[1].split(" ")[0]
	if command == "!help":
		sendMessage(s,"/w " + m[0] + " Sorry can't help you " + m[0] + "!")