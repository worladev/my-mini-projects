print("\n")

import datetime

shopping_list = ["Meat", "Cheese"]

# welcome message
greeting = "Welcome to the Grocery List App!"
print(greeting)

# getting date and time
date_time = datetime.datetime.now()
month = date_time.month
day = date_time.day
hour = date_time.hour
minute = date_time.minute

# displaying the date and time.
print(f"""Date: {str(month)} / {str(day)}
Time: {str(hour)} : {str(minute)}""")

# Initial items in the shopping list
print("You have {0} and {1} in your list.".format(shopping_list[0],shopping_list[1]))

# while loop to add new items to the shoping list.
while len(shopping_list) < 5:
    new_food = input("Add new food to the grocery list: ")
    shopping_list.append(new_food.title())

# shopping list after adding new items
print("\nHere is your grocery shopping list: \n {0}".format(shopping_list))

# sorting the items in the list in alphabetical order.
shopping_list.sort()

# number of items in the grocery list and sorted list.
print("You have " + str(len(shopping_list)) + " items in your list.")
print("\nHere is your grocery list sorted: \n {0}".format(shopping_list))

# removing unwanted items from the shoping list 
item_unwanted = input("What item do you want to remove: ")
shopping_list.remove(item_unwanted.title())

print("\nThe rest of the items in your shopping list. \n {0}".format(shopping_list))
print("You have " + str(len(shopping_list)) + " items in your list.")

add_item = input("\nWhat do you want to add: ")
shopping_list.append(add_item)

print("This is your updated shopping list \n {0}".format(shopping_list))

print("\nSimulating Grocery shopping list...")
