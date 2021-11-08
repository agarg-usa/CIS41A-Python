def computePay(dictOfStub):
	#If "hours" is greater than 40, multiply 1.5 to the rate for the overtime
	if dictOfStub["hours"] > 40:
		dictOfStub["workedOvertime"] = True
		dictOfStub["overtime"] = dictOfStub["hours"] - 40
		dictOfStub["pay"] = dictOfStub["rate"] * 40 +  dictOfStub["rate"] * dictOfStub["overtime"] * 1.5
	else:
		dictOfStub["pay"] = dictOfStub["rate"] * dictOfStub["hours"]
		dictOfStub["workedOvertime"] = False
	return dictOfStub