from tkinter import Y


cp = input("Do you want Cold Pasta? (y/n): ")

if cp == "y" or cp == "Y":
    num1 = float(input("How many?: "))
    cost1 = num1 * 2.5


gc = input("Do you want Grilled Cheese? (y/n): ")

if gc == "y" or gc == "Y":
    num2 = float(input("How many?: "))
    cost2 = num2 * 5.55


p = input("Do you want Pie? (y/n): ")

if p == "y" or p == "Y":
    num3 = float(input("How many?: "))
    cost3 = num3 * 3

age = input("How old are you: ")

if age > 54:
    discount = .45
else:
    discount  = 1 

subtotal = cost1 + cost2+ cost3
disctotal = subtotal * discount
tax = subtotal * .08
total = disctotal + tax
print(total)
