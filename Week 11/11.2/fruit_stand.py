class Fruit:
    pass

APPLE = Fruit()
ORANGE = Fruit()
MANGO = Fruit()

APPLE.name = 'Apple'
ORANGE.name = 'Orange'
MANGO.name = 'Mango'

APPLE.price = 1.5
ORANGE.price = 2.0
MANGO.price = 2.5

def add_basket(basket,fruit):
    basket.append(fruit)
    print("Added: ", fruit.name)

def calculate_total_cost(basket, fruit):
    total = 0
    for fruit in basket:
        total += fruit

def count_fruit_in_basket(basket, name):
    count = 0
    for fruit in basket:
        if fruit.name == name:
            count += 1
    return count

def main():
    basket = []

    while True:

        fruit_name = input("Enter a fruit (or press Enter to  stop): ")
        if not fruit_name:
            break

        if fruit_name.lower() == "apple": 
            add_basket(basket, APPLE)
        elif fruit_name.lower() == "orange": 
            add_basket(basket, ORANGE)
        elif fruit_name.lower() == "mango": 
            add_basket(basket, MANGO)
        else:
            print("We do not have this fruit")
        
    total_cost = calculate_total_cost(basket, fruit)
    print("Your basket contains: ")
    for fruit in ["Apple", "Orange", "Mango"]:
        count = count_fruit_in_basket(basket, fruit)
        if count > 0:
            print(count, fruit, "will be purchased")

    print("Total cost: $", total_cost)
main()