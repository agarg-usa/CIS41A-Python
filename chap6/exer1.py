"""
Aryan Garg

This program collects a users friends and stores them in a friends list.
"""
friendsIn2017 = ["Joseph", "Glenn", "Sally"]
friendsIn2018 = ["Stalin", "Emilia", "Tanya"]

print(f'In 2017 and 2018 I made friends with {friendsIn2017 + friendsIn2018}')

friendName = input("Enter your friend's name: ")

if friendName in friendsIn2017:
	print(f'{friendName} is in 2017')
elif friendName in friendsIn2018:
	print(f'{friendName} is in 2018')
else:
	print(f'{friendName} is not in 2017 or 2018')
	friendYear = int(input("Enter the year you made your friend: "))
	if friendYear == 2017:
		friendsIn2017.append(friendName)
		print(f'In 2017 I made friends with {friendsIn2017}')
	elif friendYear == 2018:
		friendsIn2018.append(friendName)
		print(f'In 2018 I made friends with {friendsIn2018}')

print(f'In 2017 I made friends with {friendsIn2017}, and in 2018 I made friends with {friendsIn2018}')

"""
In 2017 and 2018 I made friends with ['Joseph', 'Glenn', 'Sally', 'Stalin', 'Emilia', 'Tanya']
Enter your friend's name: Aryan
Aryan is not in 2017 or 2018
Enter the year you made your friend: 2018
In 2018 I made friends with ['Stalin', 'Emilia', 'Tanya', 'Aryan']
In 2017 I made friends with ['Joseph', 'Glenn', 'Sally'], and in 2018 I made friends with ['Stalin', 'Emilia', 'Tanya', 'Aryan']

In 2017 and 2018 I made friends with ['Joseph', 'Glenn', 'Sally', 'Stalin', 'Emilia', 'Tanya']
Enter your friend's name: Stalin
Stalin is in 2018
In 2017 I made friends with ['Joseph', 'Glenn', 'Sally'], and in 2018 I made friends with ['Stalin', 'Emilia', 'Tanya']
"""