import random
"""
Aryan Garg

Taking my code from exer2, I added company name as well as adding more to the output and validating user input 
"""

def get_input():
	company = input("Enter your company name: ").strip()
	while True:
		try:
			hours = float(input("Enter Hours: ").strip())
			if hours < 0:
				raise ValueError("Negative Number")
			rate = float(input("Enter Rate: ").strip())
			if rate < 0:
				raise ValueError("Negative Number")
			return (company, hours, rate)
		except Exception:
			print("Error, please enter numeric input greater than 0")

def compute_pay(hours, rate):
	if hours > 40.0:
		extraHours = hours - 40
		return round((40 * rate) + (extraHours * (1.5 * rate)), 2)
	else:
		return str(round(hours * rate,2))

def print_output(company, pay):
	print("*"*20)
	print("Your document number is: " + str(random.randint(1000, 2000)))
	print("Your " + company + " gross pay is " + str(pay) + " dollars.")

def main():
	company, hours, rate = get_input()
	pay = compute_pay(hours, rate)
	print_output(company, pay)

main()

"""
Enter your company name: google
Enter Hours: 45
Enter Rate: 10
********************
Your document number is: 1367
Your google gross pay is 475.0 dollars.

Enter your company name: Yahoo
Enter Hours: -34
Error, please enter numeric input greater than 0
Enter Hours: 34
Enter Rate: -23
Error, please enter numeric input greater than 0
Enter Hours: 34
Enter Rate: thirty
Error, please enter numeric input greater than 0
Enter Hours: 32
Enter Rate: 73
********************
Your document number is: 1334
Your Yahoo gross pay is 2336.0 dollars.
"""