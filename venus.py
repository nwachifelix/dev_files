# Storing Team Venus members data using A List and Dictionary. 
venus = [
    {"name": "stella Ejem", "age": 24, "department": "public relation"},
    {"name": "veronica ogbou", "age": 20, "department": "health"},
    {"name": "ugochukwu onuoha", "age": 28, "department": "engineering"},
    {'name': 'nwachi felix', 'age': 32, 'department': 'commerce'}, 
]
print(venus)
print('')
for Venus in venus:      # Adding for loop to Team Venus list and utilising the * operator. 
    print("name:", venus["name"].title())
    print("age:", venus["age"])
    print("department:", venus["department"].title())
    print("-" * 20)
print('')
for v in venus: # Accessing the detail of one member in team Venus list using if conditional. 
    if venu ["name"] == 'veronica ogbou':
        print("name:", venus["name"].title())
        print("age:", venus["age"])
        print("department:", venus["department"].title())
        print("-" * 20)
print("The individual names used are not purely correct only used here, for the purpose of this work.\t\nThanks.")
