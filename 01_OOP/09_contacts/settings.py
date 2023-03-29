
class Settings:

	def __init__(self):
		self.active = True
		self.contacts_loc = "data/contacts.json"
		self.users_loc = "data/users.json"

		self.contacts = None
		self.users = None

		self.menu = """
*APLIKASI CONTACTAPP*
1. VIEW ALL CONTACTS
2. FIND CONTACT BY PHONE
3. ADD NEW CONTACT
4. UPDATE CONTACT
5. REMOVE CONTACT
Q. EXIT
"""