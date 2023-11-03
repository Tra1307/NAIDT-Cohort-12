#An Automated pizza order program
while True:
    print("Welcome to Phace Pizzas, How may we serve you today?")

    small_pizza_price = 15
    medium_pizza_price = 20
    large_pizza_price = 25

    small_pepperoni_price = 1
    big_pepperoni_price = 2
    extra_cheese_price = 1

    size = input(
'''
Please input one option of your choice to select the size you want:
For small pizza($15): "S" 
For medium pizza($20): "M" 
For Large pizza($25): "L"
''')
    size = size.upper()
    add_pepperoni = input(
"""
Would you like to have some pepperoni($1)?
Yes or No
""")
    add_pepperoni = add_pepperoni.upper()
    extra_cheese = input(
"""
Would you like to have some extra cheese($1)?
Y or N
""")
    extra_cheese = extra_cheese.upper()
    if size == "S" or size == "M" or size == "L":
        if size == "S":
            if add_pepperoni == "YES":
                small_pepperoni_price
            else:
                small_pepperoni_price = 0

            if extra_cheese == "Y":
                extra_cheese_price
            else:
                extra_cheese_price = 0
            final_bill = small_pizza_price + small_pepperoni_price + extra_cheese_price
            print(f"Your final bill is: ${final_bill}")

        elif size == "M":
            if add_pepperoni == "YES":
                big_pepperoni_price
            else:
                big_pepperoni_price = 0

            if extra_cheese == "Y":
                extra_cheese_price
            else:
                extra_cheese_price = 0
            final_bill = medium_pizza_price + big_pepperoni_price + extra_cheese_price
            print(f"Your final bill is: ${final_bill}")

        elif size == "L":
            if add_pepperoni == "YES":
                big_pepperoni_price
            else:
                big_pepperoni_price = 0

            if extra_cheese == "Y":
                extra_cheese_price
            else:
                extra_cheese_price = 0
            final_bill = large_pizza_price + big_pepperoni_price + extra_cheese_price
            print(f"Your final bill is: ${final_bill}")
    else: 
        print("Please input the correct size which is S or M or L")