# The list of candies to print to the screen
candyList = ["Snickers", "Kit Kat", "Sour Patch Kids", "Juicy Fruit", "Swedish Fish", "Skittles", "Hershey Bar", "Starbursts", "M&Ms"]
# The amount of candy the user will be allowed to choose
allowance = 5
# The list used to store all of the candies selected inside of
candy_cart = []
# Print out options
for i in range(len(candyList)):
    print("[" + str(i) + "] " + candyList[i])
# create a loop to read the users selection for the number of allowance
for i in range(allowance):
	selectedCandy = input("What Candy would you like: ")
	candyInt = int(selectedCandy)
	candy_cart.append(candyList[candyInt])
for candy in candy_cart:
	print(candy)