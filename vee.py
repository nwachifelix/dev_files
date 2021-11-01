colleagues = ["vee", "arinze", "augustinchima", "zarah", "tosin"]
print(colleagues[0:3])
print(colleagues[1:4])
print(colleagues[:4])
print(colleagues[2:])
print(colleagues[-3:])
print("\nBelow are my favourite colleagues at Code Hub Africa tech.\n")
for colleague in colleagues[:3]:
    print(colleague.title())

# my_team = ["mosh", "chima", "vienivre"]
# there_team = my_team[:]
# print("my best team are:")
# print(there_team)

# print("\nThere best team is:")
# print(there_team)

team_a = ["vee", "felix", "vienivre"]
team_b = team_a[:]
print(team_b)
print(team_a)
team_a.append("ij")
team_b.append("ugo")
print(team_a)
print(team_b)
print("\nThe first three items in the list are: ")
print(colleagues[0:3])
print(("\nThe three items from the middle are: "))
print(colleagues[1:4])
print("\nThe last three items from the list are: ")
print(colleagues[-3:])

food_1 = ["eba", "semo", "rice", "beans"]
food_1.append("yam")
food_2 = food_1[:]
food_1.append("plantain")
food_2.append("amala")
print(food_1)
print(food_2)
print(f"My favourite foods are: ")
print(food_1[-4:])
for food in food_1[:4]:
     print(food.title())
print("He\'s favourite foods are: ")
print(food_2[-4:])
for food in food_2[:4]:
    print(food.title())

for item in food_1:
    print(item)
for value in food_2:
    print(value)