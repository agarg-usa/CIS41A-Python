"""
Aryan Garg

Finds the amount of money made given hourly rate and hours worked
Now, all the functionality is in its separate function and all of them gets called in the main() method
"""

def get_input():
	while True:
		try:
			hours = float(input("Enter Hours: ").strip())
			rate = float(input("Enter Rate: ").strip())
			return (hours, rate)
		except Exception:
			print("Error, please enter numeric input")

def compute_pay(hours, rate):
	if hours > 40.0:
		extraHours = hours - 40
		return round((40 * rate) + (extraHours * (1.5 * rate)), 2)
	else:
		return str(round(hours * rate,2))

def print_output(pay):
	print("Pay: " + str(pay))

def main():
	hours, rate = get_input()
	pay = compute_pay(hours, rate)
	print_output(pay)

main()

"""
Enter Hours: 45
Enter Rate: 10
Pay: 475.0

Enter Hours: 34
Enter Rate: asdf
Error, please enter numeric input
Enter Hours: 65
Enter Rate: 98
Pay: 7595.0
"""