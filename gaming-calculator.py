class Weapon (objec):
	def __init__(self, name, health, dph, energy, sgfrps): # dpn = Damage per hit, energy = Energy required, sgfrps = Single gun fire rate per second.
		self.name = name
		self.health = health
		self.dph = dph
		self.energy = energy
		self.sgfrps = sgfrps
while True:
	to_do = input("Which game do you want to calculate for?")
	to_do = to_do.lower()
	if to_do == "robocraft":
		to_do_robocraft = input("Do you want to calculate the best or worst weapon?")
