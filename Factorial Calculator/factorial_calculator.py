#Python program to find the factorial of a number provided by the user

version = input("Select type of fucntion to factorial the number:\n1.Loop\n2.Recursion\n")

 #To take input from the user 
num = input("Enter a number: ")

if num.isdigit():
    num = int(num)

if version == '1':
    #Factorial of a Number using Loop
    factorial = 1

    #Check if the number is negative, positive or zero
    if num < 0:
        print("Sorry, factorial does not exist for negative numbers")
    elif num == 0:
        print("The factorial of 0 is 1")
    else:
        for i in range(1, num + 1):
            factorial = factorial * i
        print("The factorial of", num, "is", factorial)
else:
    # Python program to find the factorial of a number provided by the user
    # using recursion
    def factorial(x):
        if x == 1:
            return 1
        else:
            return (x * factorial(x-1))
    result = factorial(num)
    print("The factorial of", num, "is", result)

