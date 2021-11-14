#i = 1
#while i <= 10:
    #print(i)
    #i += 1

#x = 5
#while x <= 20:
    #print(x)
    #x += 5

# Find the first number greater than 100 and divisible by 17.
#x = 100
#while x <= 1000:
    #x += 1
    #if x % 17 == 0:
        #print(f'{x} is the first number greater than 100 that is divisible by 17. ')
        #break


# Find the least Common Multiple of Two Divisors.
#first_divisor, second_divisor = 24, 36
#counting = True
#i = 1
#while counting:
    #if i % first_divisor == 0 and i % second_divisor == 0:
        #break
    #i +=1
#print(f"The Least Common Multiple of {first_divisor}, and {second_divisor}, is {i}. ")

print("Enter a number to see if it\'s a perfect square. ")
number = input()
number = abs(int())
i = -1
square = False
while 1 <= number**(0.5):
    i += 1
    if i*1 == number:
        square = True
        break
    if square:
        print(f"The square root of {number}, is {i}. ")
    else:
        print(f"number, is not a perfect square. ")

