from test import Test
class exp(object):
	def __init__(self, name):
		self.person = Test(name)
	def talk(self):
		self.person.who()
