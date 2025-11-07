myList = []
numberOfItemsToBeAdded = int(input("Enter the number of items to be added to the list: "))

for i in range(numberOfItemsToBeAdded):
    item = input("Enter item {}: ".format(i + 1))
    myList.append(item)

search = input("Enter the item to search for: ")

for index in range(len(myList)):
    if myList[index] == search:
        print(f"{myList[index]} is in {index} position.")
        break