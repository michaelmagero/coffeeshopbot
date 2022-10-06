print("Welcome to Mikes Coffee shop!!!!!!!\n")

name = input("What is your name:\n")

print("Hello " + name + " happy to serve you today here is our menu\n")

menu = ["Espresso", "Black coffee", "Cappucino", "Latte"]
print(menu)

order = input("\nwhat will you have today:\n")

if order == 'espresso':
  coffee_price = 350

if order == 'black coffee':
  coffee_price = 150

if order == 'capucino':
  coffee_price = 300

if order == 'latte':
  coffee_price = 200


accompaniment = input("\nwill you have an accompaniment?\n")

if accompaniment == 'yes':
  accompaniment_choice = input("\nwhat accompaniment will you have?\n")
  
  if accompaniment_choice == 'cookie':
    accompaniment_price = 300

  if accompaniment_choice == 'croissant':
    accompaniment_price = 400

  if accompaniment_choice == 'sandwich':
    accompaniment_price = 350

  total_order_price = coffee_price + accompaniment_price
  
  print("\nYour order is " + order + " accompanied with a " +     accompaniment_choice + " and it will cost you KES " + str(total_order_price))
  
else:

  total_order_price = coffee_price

  print("\nYour order is " + order + " with no accompaniment and it will cost you KES " + str(total_order_price))

