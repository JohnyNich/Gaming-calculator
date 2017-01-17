import os
import linecache
robocraft_text_docs = []
robocraft_weapon_class_names = []
def get_textdoc_line(text_doc_name, line): 
	print (text_doc_name)
	print (line)
	print ("robocraft/" + text_doc_name + ".txt")
	print (linecache.getline("robocraft/" + text_doc_name + ".txt", line).strip())
	return linecache.getline("robocraft/" + text_doc_name + ".txt", line).strip()
class Weapon (object):
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
		for info_doc in os.listdir("robocraft"):
			if info_doc.endswith(".txt") and info_doc != "robocraft-textdoc-structure.txt": # Just in case a file there does not end in .txt.
				robocraft_text_docs.append(info_doc)
		for name in robocraft_text_docs: # This is for appending to robocraft_weapon_class_names
			doc_name = []
			for letter in name:
				if letter == ".":
					break
				else:
					doc_name.append(letter)
			robocraft_weapon_class_names.append("".join(doc_name))
		print (robocraft_weapon_class_names)
		for name in robocraft_weapon_class_names:
			try:
				exec(name + " = Weapon(" + "\"" + get_textdoc_line(name, 1) + "\"" + ", " + get_textdoc_line(name, 2) + ", " + get_textdoc_line(name, 3) + ", " + get_textdoc_line(name, 4) + ", " + get_textdoc_line(name, 5) + ")")
				print ("Completed piece of code")
			except SyntaxError:
				print ("Failed piece of code")
				pass

