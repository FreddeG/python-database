


class Person:
	"""docstring for ClassName"""
	def __init__(self, name):
		self.name = name
		self.num = 15

	def printName(self):
		print(self.name)

	def changeName(self, arg = ''):
		if( arg == ''):
			self.name = input("enter name\n")
		else:
			self.name = arg
		return self.name

class People:
	def __init__(self):
		self.dataset = dict()

	def addName(self, name):
		self.dataset[name] = Person(name)
	def printPeople(self):
		#self.dataset["Bob"].name = "Test"
		new = self.dataset.pop('Bob')
		temp = new.changeName("Robert")
		
		self.dataset[temp] = new

		#self.dataset['Bob'].key() = "Test" 
		print(self.dataset)
		#print(self.dataset.pop("Bob"))
		print([self.dataset[i].num for i in self.dataset.keys()]) #



Database = People()
Database.addName("Bob")
Database.addName("Fredrik")
Database.addName("Magnus")

Database.printPeople()
#if __name__ == '__main__':
#person1 = Person("Fredrik")


#person1.printName()

#person1.changeName()
#people = people.