import time
import random
from Socket import sendMessage

king = "akerson_"
kingTime = time.time()
goldenAge = 0 # DONT TOUCH
inGoldenAge = False # DONT TOUCH
kingOn = False # DONT TOUCH
coupAttempts = 0 # DONT TOUCH
contention = {} # DONT TOUCH

kingrule = 100 # 100% health!
contentionTime = 120 #how long between coup attempts
goldenAgeLength = 15 #how long the king stays king before being taken
coupAttemptWeaken = 10 #how much it weakens the king (in %)



def writeHeader():
	s1 = "King: " + king + "\n"
	if inGoldenAge:
		s2 = "GOLDEN AGE"
	else:
		s2 = "Coup Attempts: " + str(coupAttempts)
	MYFILE = r"C:\Users\John\Desktop\ShopBot\KingText.txt"
	lines = [s1,s2]
	open(MYFILE, 'w').writelines(lines)

def kingcontest(s,contender):
	global king, kingcontest, kingTime, kingrule, contention, goldenAge, inGoldenAge, coupAttempts
	decrease = int(time.time() - kingTime)/60*2
	r = random.randint(0, 100)
	total = kingrule - decrease
	if r > total:
		sendMessage(s,"%s hits the ground as %s towers over the old king. There's a new king in town -- all hail %s! Let the golden age begin!" % (king,contender,contender))
		king = contender
		kingTime = time.time()
		kingrule = 100
		goldenAge = time.time()+goldenAgeLength
		inGoldenAge = True
	else:
		coupAttempts += 1
		total -= coupAttemptWeaken
		kingrule -= coupAttemptWeaken
		if total > 90:
			sendMessage(s,"Despite %s's best attempt, %s remains the king! Still strong as ever. All hail %s!" % (contender,king,king))
		elif total > 75:
			sendMessage(s,"Despite %s's best attempt, %s remains the king! He's breathing a little heavier. All hail %s!" % (contender,king,king))
		elif total > 50:
			sendMessage(s,"Despite %s's best attempt, %s remains the king! He's staggering, but still triumphant. All hail %s!" % (contender,king,king))
		elif total > 25:
			sendMessage(s,"Despite %s's best attempt, %s remains the king! Down, but not defeated! All hail %s!" % (contender,king,king))
		elif total > 10:
			sendMessage(s,"Despite %s's best attempt, %s remains the king! He's still holding on, but barely!! All hail %s??" % (contender,king,king))
		else:
			sendMessage(s,"Despite %s's best attempt, %s remains the king! HOW IS HE STILL ALIVE?!" % (contender,king))
	writeHeader()
	contention[contender] = time.time()

def coop(s,contender):
	if kingOn:
		if king == contender:
			sendMessage(s,"Sorry %s, you're already the king you crazy dude" % contender)
		elif inGoldenAge:
			sendMessage(s,"Sorry %s, we're still really loving %s as king, don't be a jerk." % (contender, king))
		elif contender not in contention or time.time()-contention[contender] >= contentionTime:
			kingcontest(s,contender)
		else:
			t = (contentionTime-int(time.time()-contention[contender]))/60
			sendMessage(s,"Sorry %s, you can't just fight whenever you want. Try again in %d minutes" % (contender,t)) 		

def whosKing(s):
	if kingOn:
		dk = int(time.time() - kingTime)/60
		sendMessage(s,"The current king is %s and he's ruled this chat for %d minutes" % (king,dk)) 

def setRule(s,contender,rule):
	global king
	if kingOn and contender == king:
		sendMessage(s, "King %s declares a new rule! From here on out: %s" % (king,rule))
		MYFILE = r"C:\Users\John\Desktop\ShopBot\DrinkingRule.txt"
		lines = open(MYFILE, 'r').readlines()
		lines = lines[:-1]
		lines.append("6. " + rule)
		open(MYFILE, 'w').writelines(lines)
		MYFILE2 = r"C:\Users\John\Dropbox\RULES.txt"
		open(MYFILE2, 'w').writelines(rule)

def inGoldenAge(s):
	global inGoldenAge, coupAttempts
	if kingOn and inGoldenAge and time.time() > goldenAge:
		sendMessage(s,"Hey remember that king %s? Yeah, the kingdom doesn't like him anymore. Someone should stage a coup!" % king)
		inGoldenAge = False
		coupAttempts = 0
		writeHeader()

def kingMe(s,contender):
	global king, kingcontest, kingTime, kingrule, contention, goldenAge, inGoldenAge,kingOn
	if contender == "akerson_":
		sendMessage(s,"Hey guys! King akerson has arrived to set a new rule! All hail king Akerson_! Let the golden age begin!")
		king = "akerson_"
		kingTime = time.time()
		kingrule = 100
		goldenAge = time.time()+goldenAgeLength
		inGoldenAge = True
		kingOn = True
		writeHeader()