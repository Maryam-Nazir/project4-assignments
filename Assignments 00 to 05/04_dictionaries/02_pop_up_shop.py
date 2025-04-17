# Write a program that loops through a dictionary of fruits, prompting the user to see how many of each fruit they want to buy.
# And then prints out the total combined cost of all of the fruits.
def pop_up_shop():
    fruits = {
    "Apple":100,
    "Lychee":200,
    "Strawberry":100,
    "Mango":150,
    } 
    total_cost = 0
    for fruits_name in fruits:
      price = fruits[fruits_name]
      amount = int(input(f"How Many ({fruits_name}) do you want to buy?: "))
      total_cost += (price * amount)
    print(f"Your Total is ${total_cost}")
pop_up_shop()