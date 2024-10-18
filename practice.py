# 1. Write a program that takes 2 numbers and tell whether the numbers are equal or not.

num1 = int (input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if num1 == num2:
    print("The numbers are equal.")
else:
    print("The numbers are not equal.")

# 2. Write a program that takes a number and tell whether the number is odd, even, or zero.
num = int (input("Enter a number: "))

if num == 0:
    print("The numbers are equal 0.")

elif num % 2==0:  
    print("The numbers are even.")
    
else:
    print("The numbers are odd.")

# 3. Write a program that takes 3 numbers and prints the highest number.
num1 = int (input("Enter the first number: "))
num2 = int (input("Enter the second number: "))
num3 = int (input("Enter the third number: "))

highest = max (num1, num2, num3)
print  ("the highest number is", highest)

#4. Write a program that takes a a coordinate and tell which quadrant the coordinate falls.
x_quadrant = int(input("Enter the x-coordinate: "))
y_quadrant = int(input("Enter the y-coordinate: "))

def find_quadrant(x, y):
    if x > 0 and y > 0:
        return 'quadrant 1'
    elif x < 0 and y > 0:
        return 'quadrant 2'
    elif x < 0 and y < 0:
        return 'quadrant 3'
    elif x > 0 and y < 0:
        return 'quadrant 4'
    else:
        return 'on one of the axes'

quadrant_result = find_quadrant(x_quadrant, y_quadrant)

print(f"The coordinates ({x_quadrant}, {y_quadrant}) are in {quadrant_result}.")

# 5. Write a program that takes a character and tells whether it is consonant or vowel.
char = input("Enter a single character: ")

if char in "aeiouAEIOU":
        result = "Vowel"
else:
        result = "Consonant"

print(f"The character '{char}' is a {result}.")

# 6. Write a program that takes a 2 digit number and returns the sum of the 2 digits. Ex. 24 -> 6
num = int (input("Enter 2 digit numbers: "))

ones = num % 10
tens = num // 10

digits = ones + tens 
print ("The sum of 2 digits is:", digits)