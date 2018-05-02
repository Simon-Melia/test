from test import Test

class Exp(object):

	def __init__(self, name):
		self.person = Test(name)

	def talk(self):
		self.person.who()


def main():
	simon = Exp('simon')
	simon.talk() 


if __name__ == "__main__":
	main()
