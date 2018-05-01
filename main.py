

class Person:
	"""docstring for ClassName"""
	def __init__(self, name):
		self.name = name

	def printName(self):
		print(self.name)

	def changeName(self, arg = ''):
		if( arg == ''):
			self.name = input("enter name\n")
		else:
			self.name = arg


#if __name__ == '__main__':
person1 = Person("Fredrik")


person1.printName()

person1.changeName()