# A simple calculator program in Python
# This program performs basic arithmetic operations: addition, subtraction, multiplication, division, and average.

#function to add two numbers
def add(num1, num2):
    return num1 + num2

#function to substract two numbers
def sub(num1, num2):
    return num1 - num2

#function to multiply two numbers
def multiply(num1, num2):
    return num1 * num2

#function to divide two numbers
def divide(num1, num2):
    return num1 / num2

#function to average two numbers
def avg(num1, num2):
    return (num1 + num2) / 2

#function to get user input
print("Select operation:\n" \
      "1. Add\n" \
      "2. Subtract\n" \
      "3. Multiply\n" \
      "4. Divide\n" \
      "5. Average\n") 
select =int(input("Enter choice from 1,2,3,4,5:"))

number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

# print the result
if select == 1:
    print(number1, "+", number2, "= ", \
          add(number1, number2))
    
elif select == 2:
    print(number1, "-", number2, "= ", \
          sub(number1, number2))
    
elif select == 3:
    print(number1, "*", number2, "= ", \
          multiply(number1, number2))

elif select == 4:
    print(number1, "/", number2, "= ", \
        divide(number1, number2))
    
elif select == 5:
    print("(", number1, "+", number2, ")", "/", "2", "= ", avg(number1, number2))
    
else:
    print("Invalid input") 
    