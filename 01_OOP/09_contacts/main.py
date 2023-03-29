from settings import Settings
import json
from user import User
from getpass import getpass
from contact import Contact

import os

class ContactApp:

	def __init__(self):
		self.settings = Settings()
		#self.active = True

	def save_data(self):
		with open(self.settings.contacts_loc, 'w') as file:
			json.dump(self.settings.contacts, file)


	def load_data(self):
		try:
			with open(self.settings.contacts_loc, 'r') as file:
				self.settings.contacts = json.load(file)
		except:
			self.settings.contacts = {}
			
		try:
			with open(self.settings.users_loc, 'r') as file:
				self.settings.users = json.load(file)
		except:
			self.settings.users = {}
		# print(self.settings.contacts, self.settings.users)

	def clear_scr(self):
		if os.name == "nt":
			os.system("cls")
		else:
			os.system("cls")

	def logger(self):
		self.clear_scr()
		self.login_attemps = 0
		while self.login_attemps < 3:
			print("\nPlease Login")
			username = input("Username\t: ")
			password = getpass("Password\t: ")

			if username in self.settings.users:
				if self.settings.users[username]["password"] == password:
					self.user = User(username, 
						first=self.settings.users[username]['first'],
						last=self.settings.users[username]['last'],
						password="")
					return True
			else:
				print("Login Failed!")
			self.login_attemps += 1

		return False

	def show_menus(self):
		self.clear_scr()
		print(self.settings.menu)

	def find_contact(self, phone):
		contacts = self.settings.contacts
		if phone in contacts:
			print("contact found!")
			print(f"name: {contacts[phone]['first'].title()} {contacts[phone]['last'].title()}")
			print(f"phone: {phone}")
			print(f"address: {contacts[phone]['address']}")
			return True

		else:
			print("contact doesn't exist")

	def check_opt_user(self, char):
		if char == 'q':
			self.settings.active = False
		elif char == '1':
			self.clear_scr()
			# print(self.settings.contacts)
			contacts = self.settings.contacts
			print(f"Number\t\tFull Names\t\tAddress")

			for phone, contact in contacts.items():
				print(f"{phone}\t\t{contact['first'].title()} {contact['last'].title()}\t\t{contact['address']}")

			input("Press Enter to Return.")

		elif char == '2':
		    
			self.clear_scr()
			phone = input ("Enter the phone number : ")

			self.find_contact(phone)

			input("Press Enter to Return.")

		elif char == '3':
		    
		    self.clear_scr()
		    first = input("First : ")
		    last = input("Last : ")
		    phone = input("Phone : ")
		    address = input("Address : ")

		    contact = Contact(first, last, phone, address)
		    self.settings.contacts[contact.phone] = {
		    	"first" : contact.first,
		    	"last" : contact.last,
		    	"address" : contact.address
		    }

		    self.save_data()

		    print("Contact Saved")
		    input("Press Enter to Return.")

		elif char == '4':
			self.clear_scr()
			phone = input("Phone : ")

			if self.find_contact(phone):
				print("\nEdit Options:\n1. Phone\n2. First\n3. Last\n4. Address")
				option = input("What do you want to edit / change ? (1/2/3/4) :")

				if option == "1":
					old_contact = self.settings.contacts[phone]
					new_phone = input("New phone : ")

					self.settings.contacts[new_phone] = {
						"first" : old_contact["first"],
						"last" : old_contact["last"],
						"address" : old_contact["address"]

					}

					del self.settings.contacts[phone]
					self.save_data()
					print("New phone number saved.")


				elif option == "2":
					
					new_first = input("New First: ")
					self.settings.contacts[phone]['first'] = new_first
					self.save_data()
					print("New first name saved.")


				elif option == "3":
					
					new_last = input("New Last: ")
					self.settings.contacts[phone]['last'] = new_last
					self.save_data()
					print("New last name saved.")

				elif option == "4":
					
					new_address = input("New Address: ")
					self.settings.contacts[phone]['address'] = new_address
					self.save_data()
					print("New address saved.")

			input("Press Enter to Return.")

		elif char == '5':
		    
		    self.clear_scr()
		    phone = input("Phone : ")

		    if self.find_contact(phone):
		    	confirm = input("Are you sure do you want to delete this contact ? (y/n) ")
		    	if confirm.lower() == "y":
		    		del self.settings.contacts[phone]

		    		self.save_data()

		    		print("Contact Deleted.")

		    input("Press Enter to Return.")


	def run(self):
		self.load_data()
		self.settings.active = self.logger()

		while self.settings.active:
			self.show_menus()
			self.check_opt_user(input("Options:").lower())
			

if __name__ == '__main__':				
	app = ContactApp()
	app.run()