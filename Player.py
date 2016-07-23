class Player(object):
	def __init__(self,name):
		self.name = name
		self.lvl = 1
		self.xp = 0
		self.weapon = None
		self.armor = None
		self.helmet = None
		self.gloves = None
		self.boots = None
		self.offhand = None
		self.accessory = None

	def __str__(self):
		return self.name
	def __repr__(self):
		return self.name