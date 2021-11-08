def printPayStub(dictOfStub):
	print("*"*10)
	print("Company Name:", dictOfStub["company"])
	print("Rate:", dictOfStub["rate"])
	print("Hours worked:", dictOfStub["hours"])
	if dictOfStub["workedOvertime"]:
		print("Overtime:", dictOfStub["overtime"])

	print("Pay:", dictOfStub["pay"])