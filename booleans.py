#over_18 = True
#print(type(over_18))
#over_21 = False
#print(type(over_21))

#over_18, over_21 = True, False
#print(over_18 and over_21)
#over_18, over_21 = True, False
#print(over_18 or over_21) 

#over_18 = True, False
#print(not over_18)
#not over_21 or (over_21 or over_18)
#print(not over_18 or (over_21 or over_18))

age = 20
#print(age<20)
#print(age >= 20 and age <= 21)
#print(age != 21)
#print(age == 19)
#print(6 == 6.0)
#print(6 == 42 / 7)
#print(6 == "6")

#print(age >= 20 and age < 30) or (age >= 30 and age < 40)
#print(20 <= age < 30) or (30 <= age <40)

#print("a" < "c")
#print("new york" > "san francisco")
#print("san francisco" > "new york")

age = 20
if age >= 18 and age < 21:
    print("At least you can vote. ")
    print("Poker will have to wait. ")
    print("I'm now an adult!")
if age >= 18:
    print("You can vote. ")
if age >= 21:
        print("You can play poker. ")
if age < 18:
    print("You aren\'t old enough to vote. ")
else:
    print("Welcome to our voting program. ")
if age >= 18:
    print("Welcome to our voting program. ")
else:
    print("You aren\'t old enough to vote. ")