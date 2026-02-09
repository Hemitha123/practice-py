# Print numbers from 1 to 10 using both for and while loops.

for x in range(11):
    print(x)

x=1
while x<=10:
    print(x)
    x+=1

# Print the multiplication table of any number given by the user.

x=int(input("enter the number"))
for i in range(1,11):
    print(i*x)

# Calculate factorial of a number using a while loop.

x=int(input("enter the number"))
fact=1
i=1
while i<=x:
    fact*=i
    i+=1
print(fact)


# Print the Fibonacci series up to n terms.

n=int(input("enter the number"))
a=0
b=1
for x in range(n):
    print(a)
    c=a+b
    a=b
    b=c

# Count the number of vowels in a given string.

mystr="Hello my name is hemitha"
myv="aeiouAEIOU"
vcount=0
for ch in mystr:
    if ch in myv:
        # print(ch)
      vcount+=1
print(vcount)

# print pattern 
# *
# **
# ***
# ****

for x in range(1,5):
    for y in range(1,x+1):
        print("*",end="")
    print()

# Print multiplication tables from 2 to 5.

for x in range(2,6):
    for y in range(1,11):
        print(x*y)
    print()
# Generate all possible pairs (i, j) where i = 1–3 and j = 1–3.

for x in range(1,4):
    for y in range(1,4):
        print(x,y)
    print()
