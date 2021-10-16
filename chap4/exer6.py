"""
Aryan Garg

This program asks the user for an email address. It then validates the email address then
prints out the domain name of the email address
"""
email = ""

while True:
	email = input("Please enter an email address: ")
	if not "@" in email and not "." in email:
		print("That was not a valid email address. Please enter a valid email address")
	else:
		break

print("The domain name of the email address is: " + email.split("@")[1])

"""
Please enter an email address: asdf
That was not a valid email address. Please enter a valid email address
Please enter an email address: asdf@gmail.com
The domain name of the email address is: gmail.com

Please enter an email address: joe@yahoo.com
The domain name of the email address is: yahoo.com
"""