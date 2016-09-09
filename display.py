from sys import exit
import os

class Display:

	def leave(self):
		print("The animals are sad.  Please leave Pet Place.")
		exit(0)
	
	def clear_screen(self):
		os.system('clear')
		print("*"*60)

	def get_menu_selection(self, menu_items):
		print("\n")
		for menu_item in menu_items:
			print(menu_item)

		return input("\nPlease select a number from above. \n  >  ")

	def display_selection_error(self, menu_selection):
		if menu_selection.isdigit():
			print("\n{} is an invalid option, please try again"
				.format(menu_selection))
		else:
			print("\n{} is not a number.  Please select from the options above."
				.format(menu_selection))