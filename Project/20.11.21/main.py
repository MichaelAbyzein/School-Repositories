from configs import Configures
import json
from acc import Account
from getpass import getpass
from orderlist import Orders
from random import randint
import os

class MainApp:
	
	def __init__(self):
		self.configs = Configures()

	def save(self):
		with open(self.configs.order_data, 'w') as file:
			json.dump(self.configs.orders, file)

	def load(self):
		try:
			with open(self.configs.order_data, 'r') as file:
				self.configs.orders = json.load(file)
		except:
			self.configs.orders = {}

		try:
			with open(self.configs.acc_data, 'r') as file:
				self.configs.accounts = json.load(file)
		except:
			self.configs.accounts = {}

	def clear(self):
		if os.name == "nt":
			os.system("cls")
		else:
			os.system("clear")

	def logger(self):
		self.clear()
		self.attempts = 0
		while self.attempts < 3:
			print("\nPlease Login")
			username  = input("Username\t: ")
			password = getpass("Password\t: ")

			if username in self.configs.accounts:
				if self.configs.accounts[username]['password'] == password:
					self.account = Account(username,
						first=self.configs.accounts[username]['first'],
						last=self.configs.accounts[username]['last'],
						password='')
					return True
			else:
				print("Login Failed!")
			self.attempts += 1

		return False

	def searchid(self, ordid):
		orderlist = self.configs.orders

		if ordid in orderlist:
			print()
			print(f"Order {ordid} Found!")
			print("================================================")
			print(f"Customer     : {orderlist[ordid]['customer']}")
			print(f"Ordered Items: {orderlist[ordid]['order']}")
			print(f"Description  : {orderlist[ordid]['desc']}")
			print("================================================")
			print()
			return True

		else:
			print()
			print(f"Order {ordid} not found!")
			print()

	def user_opt(self, char):
		if char == 'q':
			self.configs.is_active = False
			self.clear()
			print(f"Goodbye, {self.account.username.title()}.")

		elif char == '1':
			self.clear()
			orderlist = self.configs.orders
			print(f"OrderID\t\tCustomer\tOrder\t\tNotes")
			print("============================================================")

			for ordid, orderin in orderlist.items():
				print(f"{ordid}\t\t{orderin['customer']}\t\t{orderin['order']}\t\t{orderin['desc']}")

			print("============================================================")
			print()
			input("Press Enter to Return.")

		elif char == '2':
			self.clear()
			ordid = input("Enter the OrderID : ")

			self.searchid(ordid)

			input("Pres Enter to Return.")

		elif char == '3':
			self.clear()
			ordid = input("OrderID : ")
			customer = input("Customer Name : ")
			order = input("Ordered Items : ")
			desc = input("Extra Description : ")

			if len(ordid) <= 3:
				ordid = randint(1000, 10000)

			if len(ordid) > 4:
				ordid = randint(1000, 10000)

			orderlist = Orders(customer, order, ordid, desc)
			self.configs.orders[orderlist.ordid] = {
				"customer" : orderlist.customer,
				"order" : orderlist.order,
				"desc" : orderlist.desc
			}

			self.save()
			print()
			print("Order Listed!")
			input("Press Enter to Return.")


		elif char == '4':
			self.clear()
			orderlist = self.configs.orders
			print(f"OrderID\t\tCustomer\tOrder\t\tNotes")
			print("============================================================")

			for ordid, orderin in orderlist.items():
				print(f"{ordid}\t\t{orderin['customer']}\t\t{orderin['order']}\t\t{orderin['desc']}")
			print("============================================================")
			print()

			ordid = input("OrderID: ")
			print("\nEdit Option:\n1. Customer Name\n2. Ordered Items\n3. Description")
			print()
			choice = input("What do you want to change? : ")
			print()

			if choice == "1":
				new_custname = input("New Name : ")
				self.configs.orders[ordid]['customer'] = new_custname
				self.save()
				print()
				print("New name has been saved!")
			elif choice == "2":
				new_food = input("Updated Order : ")
				self.configs.orders[ordid]['order'] = new_food
				self.save()
				print()
				print("Order has been updated!")
			elif choice == "3":
				new_desc = input("Change Description : ")
				self.configs.orders[ordid]['desc'] = new_desc
				self.save()
				print()
				print("Description has been updated!")
			else:
				print("Option not available, please try again.")
				print()
			input("Press Enter to Return.")

		elif char == '5':
			self.clear()
			orderlist = self.configs.orders
			print(f"OrderID\t\tCustomer\tOrder\t\tNotes")
			print("============================================================")

			for ordid, orderin in orderlist.items():
				print(f"{ordid}\t\t{orderin['customer']}\t\t{orderin['order']}\t\t{orderin['desc']}")
			print("============================================================")
			ordid = input("OrderID : ")

			if self.searchid(ordid):
				confirm = input(f"Are you sure you want to remove Order {ordid} from the orderlist ? (y/n) ")
				if confirm.lower() == 'y':
					del self.configs.orders[ordid]
					self.save()
					print("Order Successfully Deleted.")
			input("Press Enter To Return.")


	def menu(self):
		self.clear()
		print(self.configs.ui)

	def run(self):
		self.load()
		self.configs.is_active = self.logger()

		while self.configs.is_active:
			self.menu()
			self.user_opt(input("Choice: ").lower())
			
if __name__ == "__main__":
	ordapp = MainApp()
	ordapp.run()