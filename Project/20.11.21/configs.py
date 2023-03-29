

class Configures:

	def __init__(self):
		self.is_active = True
		self.order_data = "data/orders.json"
		self.acc_data = "data/acc.json"
		self.accounts = None
		self.orders = None

		self.ui = """
========================
Test UI
========================
1. View Orderlist
2. Search
3. Create A New Orders
4. Update An Order
5. Remove an Order
Q. Quit
========================
"""