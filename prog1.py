#Take a string input of a number and convert it into an integer. Print its square.
nstr=input(f"enter the number in words:")
num=int(nstr)
print(f"the square of the number is {num**2}")

#Convert a float to an integer and print both the original and converted values.
n=float(input("enter the number:"))
num=int(n)
print(f"the original value is:{n}")
print(f"the converted value is :{num}")

#Ask the user to enter an integer, convert it to float, and print the result.
n=int(input("enter the number:"))
num=float(n)
print(num)

#Convert a list of strings ["1", "2", "3", "4"] into integers using a loop.
llist=["1","2","3","4"]
dlist=[]
for x in llist:
    x=int(x)
    dlist.append(x)
print(dlist)
