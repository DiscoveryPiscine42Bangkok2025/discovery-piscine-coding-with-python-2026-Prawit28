num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
multed = num1 * num2
print(multed)

if multed < 0:
    print("The result is negative.")
elif multed > 0:
    print("The result is positive.")
else:
    print("The result is negative and positive.")