class Dog:
	def speak(self):
		print "Dog speak"
	def sit(self):
		print "Dog Sit"
	def reproduce(self):
		pass


class Robot:
	def speak(self):
		print "Robot Speak"
	def sit(self):
	    print "Robot Sit"
	def oilChange(self):
		pass

def perform(anything):
	anything.speak()
	anything.sit()

a = Dog();
b = Robot();
perform(a);
perform(b);