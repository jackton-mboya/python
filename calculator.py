# 1. addition
# 2. subtraction
# 3. multiplication
# 4. division
def calculator():
    print("This is my calculator")

print("select an operation to perform:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

operation = input()

if operation == "1":
    num1 = input("Enter First Number :")
    num2 = input("Enter Second Number :")
    print("The sum is: " + str(int(num1) + int(num2)))
elif operation == "2":
    num1 = input("Enter First Number :")
    num2 = input("Enter Second Number :")
    print("The difference is: " + str(int(num1) - int(num2)))
elif operation == "3":
    num1 = input("Enter First Number :")
    num2 = input("Enter Second Number :")
    print("The product is: " + str(int(num1) * int(num2)))
elif operation == "4":
    num1 = input("Enter First Number :")
    num2 = input("Enter Second Number :")
    print("The division is : " + str(int(num1) / int(num2)))
else:
    print("Invalid Entry")

calculator()
