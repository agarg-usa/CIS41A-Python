"""
Aryan Garg

Finds the amount of money made given hourly rate and hours worked
"""

hours = float(input("Enter Hours: "))
rate = float(input("Enter Rate: "))
if hours > 40.0:
    extraHours = hours - 40
    print("Pay: " + str((40 * rate) + (extraHours * (1.5 * rate))))
else:
    print("Pay: " + str(hours * rate))

"""
Enter Hours: 45
Enter Rate: 10
Pay: 475.0

Enter Hours: 65
Enter Rate: 80.2
Pay: 6215.5
"""