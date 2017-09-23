#a = [5, 2, 3, 1, 4, 5]
## this will print the content of a
#print (a)

## this will count the amount of items in the list
#print (len(a))

## this will count the times the value will be in the list
#print (a.count(5))

## this will add items to the list and print the updated list
#a.append(8)
#print (a)

## this will insert new items as part of user interaction three times
## and then print the updated list
#for x in range(0,3,1):
#	y=int(input("Please enter a number..."))
#	a.append(y)
#print(a)

Nuts_family=['almond', 'Walnuts', 'cashews', 'Pistachio', 'hazelnut']
## this counts the number of items
#print (len(Nuts_family))

## forth item gets assignes to variable;
## then number of characters in that string is retrieved
#itemNut=Nuts_family[3]
#print (len(itemNut))

## this adds an item and then counts the updated list
#Nuts_family.append("pinenut")
#print(len(Nuts_family))

## inserts a new item in a specific place (will be added between 3 and former 4)
#Nuts_family.insert (4, 'Macadamia')
##checking for number of items and content of list
#print(len(Nuts_family))
#print(Nuts_family)

## adds new item at the end of the list, sorts them, starting with capital letters
#Nuts_family=Nuts_family +["Peanuts"]
#Nuts_family.sort()
#print(Nuts_family)

## transforms all capitals to lower cases, sorts them and prints the list
Nuts_family = [item.lower () for item in Nuts_family]
## this would change all letters to capitals
#Nuts_family = [item.upper () for item in Nuts_family]
Nuts_family.sort ()
print (Nuts_family)


