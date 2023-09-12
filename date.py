#Youre going on a date. Choose a menu item from each category. Create a calculator to deduct the price from the budget that you set.

print("Let's Go on A Date")
date_name = input("Who do you want to go with \n")
date_amount = input("How much do you want to spend \n")
print(f"We are going to a food hall where you can choose from a variety of items but remember your budget of ${date_amount}. And don't forget you have to pay for your date")
entree = {"Shrimp Alfredo": 25, "Crab Legs": 40, "Lobster": 50, "Fried Shrimp": 10, "Quesadilla":8, "Enchiladas":15}
drinks = {"Wine": 15, "Rum Punch": 15, "Margarita":12}
dessert = {"Cheesecake": 10, "Tres Leches": 8}
foodHall = {"entree": entree, "drinks": drinks, "dessert": dessert}
print(f"Here's Your Menu {foodHall}")

#***BREAK***
#Enter in the entree and deduct the price from your budget
entree_order = input('What Entree Would You Like To Order? \n')
entree_list = ["Shrimp Alfredo", "Crab Legs", "Lobster", "Fried Shrimp", "Quesadilla", "Enchiladas"]
entree_price = [25, 40, 50, 10, 8, 15]


if entree_order in entree_list:
    index = entree_list.index(entree_order)
    entree_cost = entree_price[index]
    budget = int(date_amount) - entree_cost
    print(f"Your remaining budget is ${budget}")
else:
    print("Sorry, we don't have that. Please choose an item from the menu")

#***BREAK***
#Enter in the drink and deduct the price from your budget
drink_order = input('What Drink Would You Like To Order? \n')
drink_list = ["Pinot Grigio", "Rum Punch", "Margarita"]
drink_price = [15, 15, 12]

if drink_order in drink_list:
    index = drink_list.index(drink_order)
    drink_cost = drink_price[index]
    budget = int(date_amount) - entree_cost - drink_cost
    print(f"Your remaining budget is ${budget}")
else:
    print("Sorry, we don't have that. Please choose an item from the menu")

#***BREAK***
#Enter in the dessert and deduct the price from your budget. You have to add the other 2 items together first before deducting the dessert

dessert_order = input('We Hope You Enjoyed Your Meal. What Would You Like For Dessert? \n')
dessert_list = ["Cheesecake", "Tres Leches"]
dessert_price = [10, 8]

if dessert_order in dessert_list:
    index = dessert_list.index(dessert_order)
    dessert_cost = dessert_price[index]
    budget = int(date_amount) - (entree_cost + drink_cost) - dessert_cost
    print(f"Your remaining budget is ${budget}")
else:
    print("Sorry, we don't have that. Please choose an item from the menu")
    dessert_order = input('We Hope You Enjoyed Your Meal. What Would You Like For Dessert? \n')


print("I had fun. I wouldn't mind a second date.")
