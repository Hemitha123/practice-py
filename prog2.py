#Given a string "PythonProgramming", print: First 6 characters,Last 6 characters,Every alternate character,The string in reverse order

mystr="PythonProgramming"
print(mystr[:6])
print(mystr[-6:])
print(mystr[::2])
print(mystr[::-1])

#Take a string from user and check if it’s palindrome (same forward and backward).
mystr=input("enter the name")
mystr=mystr.lower()
if mystr==mystr[::-1]:
    print("the name is palindrom")
else:
    print("the name is not palindrom")

#Extract only vowels from a given string.
mystr=input("enter the string:")
veowel="aeiouAEIOU"
for ch in mystr:
    if ch in veowel:
        print(ch)
        
#find its first letter vowel or not 
def fn_vowel(name):
    vstr="aeiouAEIOU"
    if name[0] in vstr:
        print("its a vowel")
    else:
        print("its not a vowel")
    return name
name=input("enter the name")
n=fn_vowel(name)
print(n)

#Create a list of 5 numbers. Print the sum and average.
nlist=[]
for x in range(5):
    m=int(input("enter the element:"))
    nlist.append(m)
    tot=sum(nlist)
    avg=tot/len(nlist)
print(tot)
print(avg)

#Find the largest and smallest number in a list without using max() or min().
nlist=[]
n=int(input("enter the number"))
for x in range (n):
    m=int(input("enter the element"))
    nlist.append(m)
    print(nlist)
    for x in nlist:
        big=nlist[0]
        small=nlist[0]
        if x>big:
            big=x
        if x<small:
            small=x
print(f"the biggest number is:{big}")
print(f"the smallest number is:{small}")

#Take 5 names from the user and store them in a list, then print them in reverse order.
slist=[]
n=int(input("enter the number"))
for x in range(n):
    m=input("enter the name")
    slist.append(m)
    print(slist)
    print(slist[::-1])

#Remove duplicates from a list manually (without using set()).
mylist=[]
dlist=[]
n=int(input("enter the number"))
for x in range(n):
    m=int(input("enter the element:"))
    mylist.append(m)
    print(mylist)
    for x in mylist:
        if x not in dlist:
            dlist.append(x)
print(dlist)

#Merge two lists into one using a loop and using the + operator.
list1=[4,4,6,2,7,9,8]
list2=[6,3,5,8,4,6,2]
list3=[]
for x in list1:
    list3.append(x)
for y in list2:
    list3.append(y)
print(list3)



