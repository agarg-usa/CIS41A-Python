COMPANYLIST = ["Amazon", "Apple", "Facebook", "Google", "Uber"]

def getInput():
	while True:
		companyName = input("Enter a company name: ")
		if companyName not in COMPANYLIST:
			print("Company name is in the list.")
			print(f"List of valid companies are: {COMPANYLIST}")
		else:
			break
	while True:
		hours = input("Enter how many hours you worked: ")
		if not hours.isdigit() or int(hours) < 0:
			print("Please enter a positive number.")
			continue
		hours = int(hours)

		rate = input("Enter your pay rate: ")
		if not rate.isdigit() or int(rate) < 0:
			print("Please enter a positive number.")
			continue
		rate = int(rate)
		break

	return {"company" : companyName, "hours" : hours, "rate" : rate}

