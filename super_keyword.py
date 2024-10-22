class Person:
	def __init__(self, name, age, job, religion):
		self.name = name
		self.age = age
		self.job = job
		self.religion = religion
	def show_info(self):
		print(f"{self.name} is {self.age} years old and he is {self.job} also he is {self.religion}.")

class Me(Person):
	def __init__(self, name, age, job, religion, dressing, hairstyle, speciality):

		super().__init__(name, age, job, religion)
		self.dressing = dressing
		self.hairstyle = hairstyle
		self.speciality = speciality

	def show_info2(self):
		print(f"His dressing is {self.dressing}, his hairstyle is {self.hairstyle}, and his special ability is {self.speciality}")
person = Person("Akram", 50, 'Farmer', 'Muslim')
person.show_info()
me = Me('Zohaib', 20, 'Programmer', 'Muslim', 'Werstern', 'short', 'intelligence')
me.show_info()
me.show_info2()