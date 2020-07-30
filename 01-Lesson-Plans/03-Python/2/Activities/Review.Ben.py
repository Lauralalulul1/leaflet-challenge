print("Welcome to class!")
# ask a question a store the response in a variable
playGame = input("Would you like to play a game of thermonuclear war? (y/n) " )
playerName = ""
turnNumber = 0
#print the users choice
print(f"You chose {playGame}")
#if they said y then tell the user the game has started
if (playGame == "y"):
	print("The Game Has Started")
	playerName = input("what is your name? ")
	#find out who the player is
	if(playerName == "dave"):
		print(f"I'm sorry {playerName}, I cannot do that")
	elif(playerName == "hal"):
		print("You can't play against yourself")
	else:
		print(f"Your turn {playerName}, it is turn {turnNumber}")
		print("turn: " + str(turnNumber))
else:
	print("I didn't want to play anyway")