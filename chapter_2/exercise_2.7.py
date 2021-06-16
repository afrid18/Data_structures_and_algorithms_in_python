# R-2.4		Write a python class, Flower, that has three instance variables of type str, int, and float, that respectively represent
#the name of the flower, its number of petals, and its price. Your class must include a constructor method that initializes ecah vairable to an appropriate value, and your class should include methods for setting the calue of each type, and retrieving the value of each type.



# SOLUTION-----------


class Flower:
	
	def __init__(self, name, petals, price):
		
		self.name = name
		self.petals = petals
		self.price = price


	def get_price(self):
		return self.price

	def get_name(self):
		return self.name

	def get_petals(self):
		return self.petals


flower1 = Flower('Rose', 12, 5.5)
flower2 = Flower('Lilly', 5, 12)


print(flower1.get_name())
print(flower2.get_name())
