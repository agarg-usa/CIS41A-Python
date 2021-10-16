"""
Aryan Garg

Given a number, finds the sum of all the digits in the number
"""
inputStr = None
inputInt = None

while True:
	try:
		inputStr = input("Please enter a number: ")
		int(inputStr)
		break
	except Exception:
		print("Error: Integer not inputted")
ans = 0
for char in inputStr:
	ans += int(char)

print("Sum of the digits are: " + str(ans))

"""
Please enter a number: 1729
Sum of the digits are: 19

Please enter a number: asdf
Error: Integer not inputted
Please enter a number: 654
Sum of the digits are: 15
"""
