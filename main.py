with open('inventory.txt','r') as file:
    contents = file.read()

store_inventory = eval(contents)


def open_store():
    print("Welcome to Stink's Hardware Shop!")
    print("------------------------------------")
    print('Here are the available items in stock')
    print('Item            | Price     ')

def display_inventory():
    for item in store_inventory:
        print(item, ':', store_inventory[item])

def user_shop():
    shopping = True
    while shopping:
        product = str(input("What would you like to purchase(Enter 'exit' to checkout):"))
        if product in store_inventory:
            amount = int(input("How many would you like to purchase: "))
            if store_inventory[product] >= amount:
                print(f"{amount} of {product} has been added to your cart.")
        elif product == 'exit':
            shopping = False

open_store()
display_inventory()
user_shop()