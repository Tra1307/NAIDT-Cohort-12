# DATA STRUCTURES
# STRING METHODS

text = "hEllO WoRlD"
# print(text.upper())
# print(text.lower())
# print(text.title())
# # text = text.upper()
# print(text[0:5].upper())
# print(text.capitalize())
# print("Hello! \nHow are you doing today?")
# print(
# """Hello! 
# How are you doing today?""")
greetings = """Hello! 
how are you doing this morning?"""
# print(greetings)
text = "hello world"
# print(text.islower())
# print(text.isupper())
# print(text.count("o"))
# print(text.count("l"))
# print(text.count("hello"))
# print(text.count("o", 0, 8))
# print(text.replace("hello", "hi"))
# print(text.replace("e", "a"))

text = "welcome to this class"
# print(text.split())
text = "welcome to this class, have a nice day"
# print(text.split(","))

text = "     hello    "
# print(text)
# print(text.strip())

a, b = 4, 3
# print(a+b)

# # Number Manipulation
# print(round(12.2, 2))


# ACCESSING TUPLES
cars = ("Volvo", "Toyota", "Lexus", "Ferrari", "Mercedes")
# print(cars[0])
# print(cars[2])
# print(cars[-1])
# print(cars[-4])
"""
when accessing tuples or lists from the beginning,
the index is usually 0,1,2.....
when accessing tuples or lists from the end,
the index is usually -1,-2,-3.....
"""
# You can use a length function to check how many items are in your list or tuple
# print(len(cars))
# print(cars)

# changing tuple to list
new_cars = list(cars)
# print(new_cars)
new_cars[1] = "Camry\n then"
# print(new_cars)

# changing tuple back to list
cars = tuple(new_cars)
# print(cars)

# SET
set1 = {1,2,3,4,5}
set2 = {6,7,8,9,1}
union_of_sets = set1.union(set2)
# print(union_of_sets)
inter_of_sets = set1.intersection(set2)
# print(inter_of_sets)

#ACESSING LISTS
cars = ["Volvo", "Toyota", "Lexus", "Ferrari", "Mercedes"]
# print(len(cars))
cars[3] = "Bugatti"
# print(cars)
numbers = [10,20,30,40,50,60,70,80]
# print(numbers[0:5]) # the second position after the colon is usually n-1
# print(numbers[:5])  # from beginning to a specific point
# print(numbers[2:]) # from a specific point to the end
# print(numbers[:])
# replacing multiple items in the list
# print(cars[1:3])
# print(cars)
cars[1:3] = ["Honda", "BMW"]
# print(cars)

#append adds an item to the end of the list
cars.append("Toyota")
# print(cars)
#insert adds an item to a specific position in your list
cars.insert(0, "Lexus")
# print(cars)
#extend
food = ["rice", "beans", "yam"]
fruit = ["Pineapple", "Mango", "Apple"]
food.extend(fruit)
# print(food)

#Three methods to remove an item from a list
#remove
food.remove("rice")
# print(food)
#pop
food.pop()
# print(food)
food.pop(0)
# print(food)
#del
del food[-1]
# print(food)

#DICTIONARY - Key Value Pairs

cars = {
    "brand": "Toyota",
    "model": "Corolla",
    "year": 2019,
    "color": "black"
    }

computers = {
    "brand": "HP",
    "model": "Elitebook 840 G3",
    "storage": "256 GB",
    "RAM": "8 GB"
    }
# print(cars)
# print(computers)
# print(type(cars))
# print(cars["model"])
# print(cars["brand"])

#update
# cars.update({"year": 2020})
# cars.update({"engineno": 2222020})
cars.update({"year": 2020, "engineno": 2222020})
# print(cars)
# print(type(cars))

cars = {
    "brand": "Toyota",
    "model": "Corolla",
    "year": 2019,
    "color": ["black", "white", "blue", "silver"]
    }
# print(cars["color"])
# cars["model"] = "Yaris"
# print(cars)
# x = cars.keys()
# print(x)
# y = cars.values()
# print(y)
new_cars = cars.copy()
# print(new_cars)
new_cars.pop("model")
# print(new_cars)

car = dict(brand = "Toyota", model = "Camry", year = "2020")
# print(car)

# NESTED DICTIONARY
laptops = {
    "laptop1": {
        "name": "HP",
        "model": "Pavilion G6"
        },
    "laptop2": {
        "name": "Dell",
        "model": "Vostro"
    },
    "laptop3": {
        "name": "Lenovo",
        "model": "Thinkpad"
    }
    }
print(laptops["laptop1"])
print(laptops["laptop1"]["name"])

#NESTED DICTIONARY USING dict()
laptops = dict({
    "laptop1": {
        "name": "HP",
        "model": "Pavilion G6"
        },
    "laptop2": {
        "name": "Dell",
        "model": "Vostro"
    },
    "laptop3": {
        "name": "Lenovo",
        "model": "Thinkpad"
    }
    })
print(laptops)