

#LOOPING THROUGH A KEY VALUE PAIR
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
for key, value in laptops.items():
    name = value["name"]
    model = value["model"]
    print(f"{key}: Name: {name}, Model: {model}")