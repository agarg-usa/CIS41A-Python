"""
Aryan Garg

Finds the amount of money made given hourly rate and hours worked
added try / except statements, validating user input
"""

hours = None
rate = None

while True:
	try:
		hours = float(input("Enter Hours: "))
		rate = float(input("Enter Rate: "))
		break
	except Exception:
		print("Error, please enter numeric input")

if hours > 40.0:
    extraHours = hours - 40
    print("Pay: " + str((40 * rate) + (extraHours * (1.5 * rate))))
else:
    print("Pay: " + str(hours * rate))

"""
Enter Hours: 45
Enter Rate: 10
Pay: 475.0

Enter Hours: asdf
Error, please enter numeric input
Enter Hours: 20
Enter Rate: nine
Error, please enter numeric input
Enter Hours: 20
Enter Rate: 40
Pay: 800.0
"""