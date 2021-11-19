"""
Aryan Garg

This program is very similar to the earlier rate-hours program that we have been creating, but this time
we used objects to store everything, using object oriented programming 
"""
import random
class PayClass:
	OVERTIME = 1.5
	name = ""
	company = ""
	hours = 0
	rate = 0
	def __init__(self, theName):
			self.name = theName
			print("The object", theName, "has been created!")

	def getInputs(self):
		self.company = input("Enter your company name: ").strip()
		while True:
			try:
				self.hours = float(input("Enter Hours: ").strip())
				if self.hours < 0:
					raise ValueError("Negative Number")
				self.rate = float(input("Enter Rate: ").strip())
				if self.rate < 0:
					raise ValueError("Negative Number")
				return
			except Exception:
				print("Error, please enter numeric input greater than 0")

	def computePay(self):
		if self.hours > 40.0:
			extraHours = self.hours - 40
			return round((40 * self.rate) + (extraHours * (self.OVERTIME * self.rate)), 2)
		else:
			return str(round(self.hours * self.rate,2))

	def printOutput(self):
		print("\nPAY STUB FOR: " + self.name)
		print("*"*20)
		print("Your document number is: " + str(random.randint(1000, 2000)))
		print("Your " + self.company + " gross pay is " + str(self.computePay()) + " dollars.\n")


pay1 = PayClass("Jimmy")
pay1.getInputs()
pay1.printOutput()
pay2 = PayClass("Jeniffer")
pay2.getInputs()
pay2.printOutput()

"""
The object Jimmy has been created!
Enter your company name: Google
Enter Hours: 12
Enter Rate: 53

PAY STUB FOR: Jimmy
********************
Your document number is: 1775
Your Google gross pay is 636.0 dollars.

The object Jeniffer has been created!
Enter your company name: Apple
Enter Hours: 144
Enter Rate: 43

PAY STUB FOR: Jeniffer
********************
Your document number is: 1036
Your Apple gross pay is 8428.0 dollars.
"""
