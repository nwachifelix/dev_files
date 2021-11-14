# trucks = {}
# trucks["mack"] = "ch"
# trucks["scania"] = 124
# trucks["daf"] = "xf"
# trucks["volvo"] = "rd"
# trucks["man"] = "diesel"
# print(trucks)

# trucks["volvo"] = "rb"
# print(f"The volvo has changed to {trucks['volvo']}. ")
# print(trucks)
# del trucks["volvo"]
# print(trucks)
# my_truck = trucks["mack"].title()
# print(f"Felix's truck is {my_truck}. ")
# no_key = trucks.get("points", "No point valus assigned. ")
# print(no_key)

# john_single = {
#     "first_name": "akaraonu",
#     "last_name": "chukwu",
#     "age": 32,
#     "city": "quangzhou"
#     }
# print(john_single)
# print(john_single.keys())
# print(john_single.values())

# friends_favourite_numbers = {"felix": 5, "zarah": 11, "vee": 3, "chima": 8, "arinze": 4}
# for name, value in friends_favourite_numbers.items():
#     print(f"\nname: {name} ")
#     print(f"Value: {value} ")

cars = {
    "engine": "the heart of a car", 
    "transmission": " helps to control speed",
    "battery": "provides power for electrical components of a car",
    "radiator": "ragulates engine temperature",
    "alternator": "charges car battery",
    "shocks_struts": "stabilizes car movement",
    "brakes": "device that inhibits motion",
    "catalytic_converter": "reduces toxic gas",
    "muffler": "reduces the noise emitted by a car",
    "tailpipe": "directs the exhaust gases out from the car",
    }
print(cars)
print(cars[f"engine"])
cars["tailpipe"] = (cars["tailpipe"] + " " "exhaust.")
print(cars["tailpipe"])