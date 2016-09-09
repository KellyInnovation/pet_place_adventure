
from lobby_text import LobbyText
from display import Display
from win_lose import WinLose

class Game:

	def __init__(self):
		
		self.display_class = Display()
		self.lobby_class = LobbyText()
		self.win_lose = WinLose()

	#def run(self,
		#clear_screen=clear_screen):

		#while True:
			#clear_screen()


	def start(self):
		self.lobby_class.start_print()

		help_pets = input(">  ")

		if help_pets.lower() == "yes":
			print("Great, let's get started!")
			self.lobby()
		elif help_pets.lower() == "no":
			print("You hear whimpering.")
			self.win_lose.lose()
		else:
			print("Yes or No?")
			self.start()	

	def lobby(self):
		self.lobby_class.lobby_print()

		while True:
			menu_selection = self.display_class.get_menu_selection(
				self.lobby_class.ROOM_DOOR_MENU)

			if menu_selection == "0":
				self.display_class.leave()
			elif menu_selection == "1":
				pass#self.toy_room()
			elif menu_selection == "2":
				pass#self.grocery_room()
			elif menu_selection == "3":
				pass#self.golden_retriever_room()
			elif menu_selection == "4":
				pass#self.grooming_room()
			elif menu_selection == "5":
				pass#self.peacock_room()
			elif menu_selection == "6":
				pass#self.bunny_room()
			else: 
				self.display_class.display_selection_error(menu_selection)




game = Game()
game.start()