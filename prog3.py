#Create a tuple with 5 elements. Try to change one and observe what happens.
# tup=()
# n=int(input("enter the number:"))
# for x in range(n):
#     m=int(input("enter the element:"))
#     tup.append(m)
# print(tup)
#it cannot be appended or change the existing element because tuple is immutable

#Convert a list into a tuple and a tuple into a list.
llist=[1,4,2,"hemitha",40.23,"amar"]
tup=tuple(llist)
print(tup)

tup1=[1,4,2,"hemitha",40.23,"amar"]
list1=list(tup1)
print(list1)

# Find the index of a given element in a tuple.
ttup=(10,20,55,"hemitha","ananya",30)
res=ttup.index("hemitha")
print(res)

# Create a dictionary with names as keys and ages as values. Print names of people older than 18.
ddict={"amar":22,"hemitha":20,"himani":15,"moksha":12}
for name,age in ddict.items():
    if age>18:
        print(name)


#Add, update, and delete keys in a dictionary.
ddict={"amar":101,"vaishnavi":102,"moksha":103,"hemitha":104}
print(ddict)
ddict["syed"]=105
print(ddict)
ddict["moksha"]=107
print(ddict)
ddict["moksha m g"]=103
print(ddict)
ddict.pop("amar")
print(ddict)

#Count the frequency of each character in a given string using a dictionary.
ddict={}
s=input("enter the string")
for ch in s:
    if ch in ddict:
        ddict[ch]+=1
    else:
        ddict[ch]=1
print(ddict)

#Merge two dictionaries into one
ddict={"amar":101,"monisha":102}
ddict2={"hemitha":103,"moksha":104}
ddict3={}
ddict3.update(ddict)
ddict3.update(ddict2)
print(ddict3)

#Given a dictionary of students and marks, find who scored the highest
ddict={'amar': 99, 'monisha': 100, 'hemitha': 67, 'moksha': 90}
high=0
hname=""
for name,marks in ddict.items():
    if marks>high:
        high=marks
        hname=name
print(f"the highest scored is {hname} with {high}")        

#Create two sets of numbers and perform union, intersection, and difference.
sset1=set()
n=int(input("enter the number"))
for x in range(n):
    m=int(input("enter the element"))
    sset1.add(m)
print(sset1)
sset2=set()
y=int(input("enter the number"))
for x in range(y):
    i=int(input("enter the element"))
    sset2.add(i)
print(sset2)
union_set=sset1 | sset2
interaction_set=sset1 & sset2
difference_set=sset1-sset2
print(union_set)
print(interaction_set)
print(difference_set)

#Remove duplicates from a list using a set.
llist=[10,2,20,50,48,30,10,3,2,10]
llist1=list(set(llist))
print(llist1)

#Check if one set is a subset of another.
set1={2,4,2,2,2}
set2={2,4,2,2,2}
print(set1.issubset(set2))
