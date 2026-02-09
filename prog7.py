# . Vowel & Consonant Counter
# Ask user to enter a sentence.
# Count how many vowels and consonants it has.
# Print the counts and display all vowels found (no duplicates)

sentence=input("enter the sentence ")
vowel="aeiouAEIOU"
list1=[]
llist2=[]
ch=0
for ch in sentence:
    if ch.isalpha():
        if ch in vowel:
            list1.append(ch)
        else:
            llist2.append(ch)
print(list(set(list1)))
print(list(set(llist2)))
print(len(list1))
print(len(llist2))