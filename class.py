Classes

class person:
	pass

p = Person()
print(p)

Methods

class Person:
	def say_hi(self):
		print('Hello,how are you?')

p = Person()
p.say_hi()



class Person:
	def say_hi(self):
		print('Hello,how are you?')
	def say-age(self):
		print('How old are you?')

p = Person()
p.say_hi()
p.say_age()

__init__method

class Person:
	def __init__(self,name,age):
			self.name = name
			self.age = age
 	def say_name(self):
 			print('hello,my name is',self.name)

 	def say_age(self):
 			print('I am',self.age,'years old.')

P = Person('Mg Mya','28')
p.say_name()
p.say_age()

p = Person('Ma Ni','20')
p.say_name()
p.say_age()

p2 = Person('U Phyu','56')
p2.say_age()

p2.say_name()

##home work 
dog = dog('Name')
dog.color('Black')
dog.owner('U Kaung')

dog.function()	- brak
				- eat
				- sleep
				- bite

