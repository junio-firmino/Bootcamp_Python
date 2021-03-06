from Day_15_dic import resources, MENU

profit = 0

def is_resource_sufficient(order_ingredients):
    is_enough = True
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry but don't have enough resources {item}")
            is_enough = False
    return is_enough

def process_coins ():
    print('Please insert coins.')
    total = int(input('How many quarters? '))*0.25
    total += int(input('How many dimes? '))*0.1
    total += int(input('How many nickles? '))*0.05
    total += int(input('How many pennies? '))*0.01
    return total

def is_transaction_successful (money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received-drink_cost,2)
        print(f'Você pagou $ {money_received} e Seu troco é de $ {change}.')
        # global profit
        # profit += drink_cost
        # print(profit)
        return True
    else:
        print(f"Sorry that's not enough money, your payment was $ {money_received}. Money refunded.")
        return False

def make_coffe(drink_name, order_ingredients):
    '''Deduct the required ingredients from the resources.'''
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f'Here is your {drink_name.upper()}')


is_on = True
while is_on:
    choice = input('What would you like? (expresso/latte/cappuccino): ').lower()
    try:
        if choice == "off":
            is_on = False
        elif choice == 'report':
            for key, values in resources.items():
                print(key.title(),':', values,'ml')
        else:
            drink = MENU[choice]
            if is_resource_sufficient(order_ingredients=drink['ingredients']):
                payment = process_coins()
                if is_transaction_successful(money_received=payment, drink_cost=drink["cost"]):
                    make_coffe(drink_name=choice, order_ingredients=drink['ingredients'])
    except KeyError:
        print(f"We don't have this product called {choice.upper()}. ")
