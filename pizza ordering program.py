while True:
    print('Welcome to NITDA pizza')

    small_pizza = 15
    medium_pizza = 20
    large_pizza = 25

    pep_small_pizza = 2
    pep_medorlarge_pizza = 3

    extra_cheese = 1

    size = input(
        '''
        small pizza = $15
        medium pizza = $20
        large pizza = $25
        
        What size of pizza would you like?
        Type S for small, M for medium and L for large
        '''
        )
    toppings = input('would you like pepperoni? Please type Y for yes and N for no')

    extra_cheese = input('would you like extra cheese? Please type Y for yes and N for no')

    size = size.upper()
    toppings = toppings.upper()
    extra_cheese = extra_cheese.upper()

    if size == 'S' or size == 'M' or size == 'L':
        if size=='S':
            if toppings == 'Y':
                small_pizza
            else:
                small_pizza == 0
        if size=='M':
            if toppings == 'Y':
                medium_pizza
            else:
                medium_pizza==0
        if size == 'L':
            if toppings == 'Y':
                large_pizza
            else:
                large_pizza == 0

   
