def makePizza(*toppings):

    """Print the list of toppings that have been requested
        Heh ehe
    """
    print("\n Making a pizza with the following toppings:")
    for topping in toppings:
        print(f'- {topping}')

def makePizzaWithSize(size, *toppings):
    print(f"\n Make a {size}-inch pizza with following toppings:")

    for topping in toppings:
        print(f'- {topping}')

makePizza('mushrooms', 'green peppers', 'extra cheesse')
makePizza('pepperoni')
makePizzaWithSize(5, 'pepperoni', 'green peppers')