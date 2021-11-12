"""
Aryan Garg

This code reads in an error log and counts the number of lines in the log as well as counts the number
of lines that the word "error" appears
"""
fileName = input("Enter the log file path: ")

try:
	errorLog = open(fileName)
except:
	print("Sorry that was an invalid file.")
	exit()

lineCount = 0
errorCount = 0

for line in errorLog:
	line = line.strip()
	if len(line) == 0:
		continue
	lineCount += 1
	if "error" in line.lower():
		errorCount += 1

print(f"There are {lineCount} lines in {fileName}")
print(f"There are {errorCount} lines with the word error in {fileName}")

errorLog.close()

reportError = open("reportError.txt", "w")
reportError.write(f"linesCount = {lineCount}\n")
reportError.write(f"errorLinesCount = {errorCount}\n")
reportError.close()

"""
Enter the log file path: ErrorLog.txt
There are 108 lines in ErrorLog.txt
There are 5 lines with the word error in ErrorLog.txt

reportError.txt:

linesCount = 108
errorLinesCount = 5


Enter the log file path: Errorlog.txt
Sorry that was an invalid file.
"""