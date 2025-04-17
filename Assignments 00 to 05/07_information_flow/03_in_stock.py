def num_in_stock(fruit):
    inventory = {
        'pomegranates': 5,
        'cherrys' : 0,
        'strawberrys' : 2,
        'oranges' : 0,
        'kiwi' : 0,
        'apples' : 0,
    }
    return inventory.get(fruit,0)
def main():
    fruit = input("Enter the name of the fruit: ").lower()
    stock = num_in_stock(fruit)
    if stock > 0:
        print(f"{fruit.capitalize()} are in stock. We have {stock} in stock.")
    else:
        print(f"{fruit.capitalize()} are not in stock. We have {stock} in stock.")
main()



    