"""
Aryan Garg

This program will calculate the weekly pay for a given employee, given the hours they worked and their hourly rate.
This program will also keep in count their overtime hours and print out a paystub
"""

from GetInput import getInput
from ComputePay import computePay
from PrintPay import printPayStub

def payProcess():
	myDict = getInput()
	myDict = computePay(myDict)
	printPayStub(myDict)

if __name__ == "__main__":
	payProcess()

"""
Enter a company name: Google
Enter how many hours you worked: 41
Enter your pay rate: 10
**********
Company Name: Google
Rate: 10
Hours worked: 41
Overtime: 1
Pay: 415.0

Enter a company name: asdf
Company name is in the list.
List of valid companies are: ['Amazon', 'Apple', 'Facebook', 'Google', 'Uber']
Enter a company name: Amazon
Enter how many hours you worked: -12
Please enter a positive number.
Enter how many hours you worked: 12
Enter your pay rate: -21
Please enter a positive number.
Enter how many hours you worked: 12
Enter your pay rate: 21
**********
Company Name: Amazon
Rate: 21
Hours worked: 12
Pay: 252
"""