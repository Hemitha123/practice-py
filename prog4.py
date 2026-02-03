# Take marks as input and print the grade using conditions:
# ≥90: A
# 80–89: B
# 70–79: C
# 60–69: D
# <60: Fail
s1=int(input("enter the marks:"))
s2=int(input("enter the marks:"))
s3=int(input("enter the marks:"))
s4=int(input("enter the marks:"))
s5=int(input("enter the marks:"))
s6=int(input("enter the marks:"))
tot=s1+s2+s3+s4+s5+s6
print(tot)
avg=tot//6
print(avg)
if s1<60 and s2<60 and s3<60 and s4<60 and s5<60 and s6<60:
    print("Fail")
elif 90<avg<100:
    print("A")
elif 80<avg<89:
    print("B")
elif 70<avg<79:
    print("C")
elif 60<avg<69:
    print("D")
else:
    print("Fail")

# Take three numbers and find the largest.
num1=int(input("enter the number:"))
num2=int(input("enter the number:"))
num3=int(input("enter the number:"))
if num1>num2 and num1>num3:
    print(num1)
elif num2>num1 and num2>num3:
    print(num2)
else:
    print(num3)

# Check whether a given number is even, odd, or zero.
num=int(input("enter the number:"))
if num%2==0:
    print("it is even")
else:
    print("it is odd")

# Check if a character entered by user is a vowel or consonant.
mychar=input("enter the character")
vchar="aeiouAEIOU"
if mychar in vchar:
    print("it is vowel")
else:
    print("it is consonant")

# Check if a number is present in a list.
llist=[10,20,3,5,40,5,6,60]
x=100
if x in llist:
    print("number found")
else:
    print("number not found")


# Check if a character is present in a string.
mystr="Hello,My name is Hemitha"
x=input("enter the character")
if x in mystr:
    print("character found")
else:
    print("character not found")

# Write a program to check if a key exists in a dictionary
ddict={101:"amar",102:"hemitha",103:"moksha"}
x=int(input("enter the key to be found"))
if x not in ddict:
    print("key not found")
else:
    print("key found")
