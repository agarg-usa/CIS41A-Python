import random
"""
Aryan Garg

Finds the amount of money made given hourly rate and hours worked
added try / except statements, validating user input using while loop
"""

company = input("Enter your company name: ").strip()
hours = None
rate = None

while True:
	try:
		hours = float(input("Enter Hours: ").strip())
		rate = float(input("Enter Rate: ").strip())
		break
	except Exception:
		print("Error, please enter numeric input")

print("*"*20)
print("Your document number is: " + str(random.randint(1000, 2000)))
if hours > 40.0:
    extraHours = hours - 40
    print("Your " + company + " gross pay is: " + str(round((40 * rate) + (extraHours * (1.5 * rate)), 2)))
else:
    print("Your " + company + " gross pay is: " + str(round(hours * rate,2)))

"""
Enter your company name: Google
Enter Hours: 45
Enter Rate: 10
********************
Your document number is: 1366
Your Google gross pay is: 475.0

Enter your company name: apple
Enter Hours: nine
Error, please enter numeric input
Enter Hours: 3
Enter Rate: asdf
Error, please enter numeric input
Enter Hours: nine
Error, please enter numeric input
Enter Hours: 45
Enter Rate: 32
********************
Your document number is: 1534
Your apple gross pay is: 1520.0

Enter your company name: 34
Enter Hours: 34
Enter Rate: 34
********************
Your document number is: 1346
Your 34 gross pay is: 1156.0
"""