import string
import time

from Socket import openSocket, sendMessage
from Initialize import joinRoom
from Read import parseMessage
from Commands import checkforcommands
from Player import Player
from KingContest import kingcontest,coop,whosKing,setRule,inGoldenAge,kingMe

s = openSocket()
joinRoom(s)
readbuffer = ""
m = []
start_time = time.time()

while True:
	try:
		readbuffer = readbuffer + s.recv(1024).decode('utf-8')
	except BlockingIOError:
		#do this if someone didn't talk
		inGoldenAge(s)
		continue
	else:
		#do this if osmeone talked
		temp = readbuffer.split("\n")
		readbuffer = temp.pop()
		for line in temp:
			print(line)
			if "PING :tmi.twitch.tv" in line:
				s.send(("PONG :tmi.twitch.tv" + "\r\n").encode('utf-8'))
			if "JOIN" in line:
				print("SOMEONE JOINED?!")
			if "PRIVMSG" in line:
				m = parseMessage(line)
				a = "!coop"
				a1 = "!coup"
				b = "!king"
				c = "!rule "
				d = "!kingme"
				e = "!freeabqu"
				f = "!jailaker"
				if m[1][0:len(a)] == a or m[1][0:len(a1)] == a1:
					coop(s,m[0])
				if m[1][0:len(b)] == b:
					whosKing(s)
				if m[1][0:len(c)] == c:
					if len(m[1]) > len(c):
						setRule(s,m[0],m[1][6:])
				if m[1][0:len(d)] == d:
					kingMe(s,m[0])
				if m[1][0:len(d)] == e:
					free