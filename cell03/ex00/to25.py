print("Enter a number less than 25: ")
num1 = int(input())
if num1 >= 25:
    print("Error")
else:
    while num1 <= 25:
        print("Inside the loop, my variable is", num1)
        num1 += 1
