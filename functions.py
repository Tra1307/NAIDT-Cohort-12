'''
Functions
'''

#SYNTAX
def function_name(parameters):      
    function body         #what action you want the function to carry out

function_name(arguments)     #calling the function with the arguments that the parameters represent


def greet():
    print('welcome')

greet()

def add_num(num1, num2, num3):
    sum = num1 + num2 + num3
    print('The sum is:', sum)

add_num(3, 2, 6)

def food(fruit):
    fruit.append('orange')

fruit = ['mango', 'apple', 'pawpaw']
food(fruit)

def my_func(x):
    return 5*x

print(my_func(3))

def add_num(num1, num2):
    sum = num1 + num2
    return sum

print(add_num(3, 2))


def my_func(fname):
    print(fname + 'john')

my_func('george')

def add_num(*args):
    sum = 0
    for num in args:
        sum +=  num
    return sum
print(add_num(1,2,3))

def my_func(*kids):
    print('the youngest child is' + kids[2])

my_func('george', 'prince', 'king')

def my_func(**kids):
    print('the youngest child is ' + kids['lname'])

my_func(fname = 'chinedu', lname = 'george')

def intro(**data):
    print('\nData type:', type(data))
    for key, value in data.items():
        print(f'{key} is {value}')
intro(firstname = 'James' , lastname = 'Jude', email = 'gfvdsj@jjk.com', country = 'nigeria', age = 33, phone = 65479548)

lambda arguments: expression
bb = lambda a, b: a + b
print(bb(5, 6))

def square(n):
    '''Takes in a number n, returns the square of n'''
    return n**2

