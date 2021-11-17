# printing first five and last five names in the attendancelists including the square [] brackets.
attendancelists = ["vee", "arinze", "ugochi", "felix", "tosin", "lanre", "vienivre", "josiah", "chima", "zarah. "]
print(attendancelists[0:5])
print(attendancelists[5:10])

# Here, using for loop to iterate each name in the attendancelists, excluding the [] brackets.
for everystudent in attendancelists:
    print(everystudent.title())
# Using few individual items in the attendanlists.
statament = f"{attendancelists[0].title()} and {attendancelists[3].title()}, have received funding for their next program with CHAfrica.TECH as announced by mentor Chizom. "
print(statament)
name = f"This is a personal message to {attendancelists[1].title()}, wishing you good luck in your forth coming exams! "
print(name)

# Changing an item in the list.
attendancelists[0] = "josiah"
print(attendancelists)

# Adding an item in the list.
attendancelists.insert(0, "vee")
print(attendancelists)
# Removing an item from the list.
del attendancelists[-3]
print(attendancelists)

neigbours = ["md", "ugo", "biggy", "inno", "olu", "felix"]
print(neigbours)
popped_neigbours = neigbours.pop()
print(neigbours)
print(popped_neigbours)

print(f"The youngest neigbour in the compound is {popped_neigbours.title()}, who happens to be a clearing and forwarding agent. ")
print(neigbours.pop(-2))

neigbours.remove("ugo")
print(neigbours)

earlybird = "ugo"
neigbours.remove(earlybird)
print(neigbours)
print(f"{earlybird.title()} is the first person to always leave for work in the compound. ")

list_of_cars = ["lexus", "honda", "toyota", "benz", "chrisler" ]
print(list_of_cars[0].title() + " " +list_of_cars[1].title() + " " + list_of_cars[4].title())
from operator import itemgetter
list_of_cars = ["lexus", "honda", "toyota", "benz", "chrisler" ]
print("Here is the original list: ")
print(list_of_cars)

print("Here is the sorted list: ")
print(sorted(list_of_cars))

print(list_of_cars)
list_of_cars.reverse()
print(list_of_cars)
list_of_cars.reverse()
print(list_of_cars)
len (list_of_cars)
print(list_of_cars)

location = ["canada", "usa", "dubai", "australia", "germany"]
print(location)
print(sorted(location))
print(location)
location.reverse()
print(location)
location.reverse()
print(location)
location.sort(reverse=True)
print(location)
location.sort(reverse=False)
print(location)