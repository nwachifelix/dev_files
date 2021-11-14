# Conditionals
age = 19
if age >= 18 and age < 20:
     print('you are old enough to vote come 2023 national election. ')
     print('There\'s no more complaining to do. ')

if age >= 18:                    # Using nested conditionals. 
     print('You can vote. ')
     if age >= 21:
          print('You can vote and also participate in sensitizing people about voter apathy. ')

if age < 18:                   # Adding the otherwise clause "else". 
     print('You will not be voting come 2023 election. ')
else:
    print('You will have less complain to do. ')

#The else-if "elif" staement. 

age = 59

age_input = input('Please tell us your age: ')
age_input = int(age_input)

if age >= 59:
     print('You\'re now a statesman!')
     print('Continue exercising.')
if age <= 39:
      print('You can vote and be voted to become the president come next general election. ')
elif age >= 29:
     print('You\'re the hope of the nation. ')
elif age >= 18:
      print('You\'re now an adult and can participate in the 2023 election. ')
elif age >= 10:
     print('You\'re still a kid, keep learning and be good. ')
elif age_0 < 10:
     print('You\'re  good my boy. ')
else:
     print('Today is a blessing!')