from sys import *
from time import *
class Hangman():

	def __init__(self):
		print "This is a game of Hangman. Guess correctly or you shall face the wrath of 'THE ROPE'!!!"
		print "1--> I accept the to face the wrath of the rope."
		print "2--> I accept my defeat. Nooooooo!!!!"

		choice = raw_input("-->")

		if choice == '1':
			print "Loading beers...."
			sleep(2)
			print "Loading heroes,thieves,killers,pirates...."
			sleep(2)
			self.startTheGame()

		elif choice == '2':
			print "You have been executed..."
			exit(0)

		else:
			print "I beg your pardon but it seems I am hearing you wrong. Could you please what you have said..."
			self.init()


	def startTheGame(self):
		print "The day of my birth, my death began its walk. It is walking toward me, without hurrying."
		print "Death twitches my ear. 'Live' he says 'I am coming'"
		self.coreGame()

	def coreGame(self):
		chances = 0
		letters_used = ""
		wordDecidingFate = "death"
		progress = ["?","?","?","?","?"]

		while chances < 6:
			chance = raw_input("Guess a letter -->")

			if chance in wordDecidingFate and chance not in letters_used:
				print "It seems you have evaded...."
				letters_used += "" + chance
				self.hangmanGraphics(chances)
				print "Progress: " + self.progressUpdate(chance, wordDecidingFate,progress)
				print "Letter used: " + letters_used

			elif chance not in wordDecidingFate and chance not in letters_used:
				chances += 1				
				print "Things aren't looking so good. The guess was wrong..."
				print "It seems that the rope is wants to feel your neck and so does your doom awaits..."
				letters_used += "," + chance
				self.hangmanGraphics(chances)
				print "Progress: " + "".join(progress)
				print "Letter used: " + letters_used

			else:
				print "This is the wrong letter, you wanna be out all day? "
				print "Try again..."

	def hangmanGraphics(self,chances):
		if chances == 0:
			print "________      "
			print "|      |      "
			print "|             "
			print "|             "
			print "|             "
			print "|             "

		elif chances == 1:
			print "________      "
			print "|      |      "
			print "|      0      "
			print "|             "
			print "|             "
			print "|             "

		elif chances == 2:
			print "________      "
			print "|      |      "
			print "|      0      "
			print "|     /       "
			print "|             "
			print "|             "

		elif chances == 3:
			print "________      "
			print "|      |      "
			print "|      0      "
			print "|     /|      "
			print "|             "
			print "|             "

		elif chances == 4:
			print "________      "
			print "|      |      "
			print "|      0      "
			print "|     /|\     "
			print "|             "
			print "|             "

		elif chances == 5:
			print "________      "
			print "|      |      "
			print "|      0      "
			print "|     /|\     "
			print "|     /       "
			print "|             "

		else:
			print "________      "
			print "|      |      "
			print "|      0      "
			print "|     /|\     "
			print "|     / \     "
			print "|             "
			print "The noose tightens around your neck, and you feel the"
			print "sudden urge to urinate."
			print "GAME OVER!"
			self.__init__()

	def progressUpdate(self, chance, wordDecidingFate, progress):
		i = 0
		while i < len(wordDecidingFate):
			if chance == wordDecidingFate[i]:
				progress[i] = chance
				i += 1
			else:
				i += 1

		return "".join(progress)

game = Hangman()					


