"""
Aryan Garg

This code organizes a friendlist based on the year you made friends with them in a dict
"""
dictOfFriends = {"2017" : ["Joseph", "Glenn", "Sally"], "2018" : ["Stalin", "Emilia", "Tanya"]}
print(f"The friends I made are: {dictOfFriends}")

friendName = input("Enter your friend's name: ")
friendYear = int(input("Enter the year you made your friend: "))
if friendYear == 2017:
	dictOfFriends["2017"].append(friendName)
elif friendYear == 2018:
	dictOfFriends["2018"].append(friendName)

print(f"The list of friends I made is now: {dictOfFriends}")

"""
The friends I made are: {'2017': ['Joseph', 'Glenn', 'Sally'], '2018': ['Stalin', 'Emilia', 'Tanya']}
Enter your friend's name: Aryan
Enter the year you made your friend: 2017
The list of friends I made is now: {'2017': ['Joseph', 'Glenn', 'Sally', 'Aryan'], '2018': ['Stalin', 'Emilia', 'Tanya']}

The friends I made are: {'2017': ['Joseph', 'Glenn', 'Sally'], '2018': ['Stalin', 'Emilia', 'Tanya']}
Enter your friend's name: Grenda
Enter the year you made your friend: 2018
The list of friends I made is now: {'2017': ['Joseph', 'Glenn', 'Sally'], '2018': ['Stalin', 'Emilia', 'Tanya', 'Grenda']}
"""