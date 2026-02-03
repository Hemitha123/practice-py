# # 1. Student Marks Analyzer
# # Write a program that:
# # Takes names and marks of 5 students as input (use dictionary).
# # Prints the average marks.
# # Displays the student who scored the highest.
# # If the average is ≥ 50, print “Class Passed”, else “Class Failed”

# ddict={}
# n=int(input("enter the nuumber"))
# for x in range(n):
#     name=input("enter the name")
#     marks=int(input("enter the marks"))
#     ddict[name]=marks
#     print(ddict)
# tot=sum(ddict.values())
# #print(tot)
# avg=tot//5
# print(avg)
# high=0
# hname=0
# for name,marks in ddict.items():
#     if marks>high:
#         high=marks
#         hname=name
# print(f"the highest scored is {hname} with {high}")
# if avg>=50:
#     print("class passed")
# else:
#     print("class failed")

#  2. Grocery Billing System
# Create a program that:
# Has a predefined dictionary of grocery items and prices.
# Asks the user to enter items to buy until they type "done".
# Calculate total bill.
# If bill > 1000, give 10 % discount.
# Display final amount

# # Predefined dictionary of items and prices
# grocery = {
#     "rice": 50,
#     "sugar": 40,
#     "milk": 30,
#     "bread": 25,
#     "oil": 120,
#     "apple": 100
# }

# total = 0

# print("Available items:", grocery)

# while True:
#     item = input("Enter item to buy (type 'done' to finish): ").lower()

#     if item == "done":
#         break

#     if item in grocery:
#         total += grocery[item]
#         print(f"{item} added. Price = {grocery[item]}")
#     else:
#         print("Item not available!")

# print("\nTotal bill =", total)

# # Apply discount
# if total > 1000:
#     discount = total * 0.10
#     final_amount = total - discount
#     print("10% discount applied!")
#     print("Discount amount =", discount)
# else:
#     final_amount = total

# print("Final amount to pay =", final_amount)

