# mates = ["vee", "felix", "arinze", "lanre", "zarah", "chima", "vienivre"]
# for mate in mates:
#     print(mate) 
#     print(f"{mate.title()}, I really enjoyed our online session last night! ")
#     print(f"Would it not be better we schedule another session this weekend, {mate.title()}?\n")
# print("It's nice having you guys as cohorts, Thank you!")

# pizzas = ["pepperoni", "yumyum", "chickenp"]
# for pizza in pizzas:
#     #print(pizza)
#     print(f"I use {pizza} pizza as lunch everyday at work. ")
#     print(f"I really like {pizza} pizza!\n ")
# print("We actually love pizzas in our family.\n ")
for value in range(6):
    print(value)
numbers = list(range(1, 6))
print(numbers)

even_nums = list(range(2, 11, 2))
print(even_nums)

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))
print(list(range(1, 101)))
print(list(range(3, 13, 3)))

squares = []
for value in range(1, 11):
    square = value**2
    squares.append(square)
print(squares)

squares = [value**2 for value in range(1, 11)]
print(squares)
for value in range(1, 21):
    print(value)

print(list(range(1, 1000001)))
for value in (range(1, 1000001)):
    print(value)