#!/usr/bin/env python3
num = int(input("Give me the first number: "))
num2 = int(input("Give me the second number: "))
print("Thank you!")
plus = num + num2
delete = num - num2
divide = num // num2 if num2 != 0 else "ไม่สามารถหารด้วยศูนย์ได้"
multiply = num * num2
print(f"{num} + {num2} = {plus}")
print(f"{num} - {num2} = {delete}")
print(f"{num} / {num2} = {divide}")
print(f"{num} * {num2} = {multiply}")