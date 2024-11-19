num1 = int(input("Enter the first number : \n"))
num2 = int(input("Enter the second number : \n"))
total_num = num1 * num2
print(f"{num1} x {num2} = {total_num}")

if total_num > 0:
    print("The result is positive.")
elif total_num < 0:
    print("The result is negative.")
else:
    print("The result is positive and negative.")