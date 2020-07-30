print("Lists")
# VBA ---   Dim myArray(10) As Integer
myList = ['Ben', 1, 2.5, True, 'Scuba "the stevest" Steve', [0,1,2,3]]
#add and item
myList.append("stuff")
#cast list to the string
print("List = " + str(myList))
#print the 4th item from the list ( counting from 0! )
print(myList[4])
#find where an item is in a list
print(myList.index(2.5))
#assign to specific spot in a list
myList[4] = 3.14
#removes last item of the list and assigns to x
x= myList.pop()
print(x)
#find and remove an item from a list and assign to x
x= myList.pop(myList.index(2.5))
print(x)
#remove 3.14 from the list
myList.remove(3.14)
print(myList)
# print the length of the list
print(len(myList))