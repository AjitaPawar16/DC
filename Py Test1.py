#!/usr/bin/env python
# coding: utf-8

# In[15]:


#Conditions to be checked-
#1. length of 1st word, length of 2nd word, if the length is match
#2. letters in the 1st word, letters in the 2nd word, if the set of letters is a match (eg. Silent and Listen)

#Taking input from user to check anagram

a=input("Enter first word to check anagram: ")
b=input("Enter second word: ")

#storing the entered strings into lists. Sorting the list so as to compare with the 2nd list.

list1=list(a)
list1.sort()
print(list1)


list2=list(b)
list2.sort()
print(list2)

#calculating length of both the strings

c=len(a)
d=len(b)
print(c)
print(d)

#1st condition- If the lenght of the two words do not match, the words are not anagrams. If the lengths match, we check for the next condition.

if c!=d:
    print("Entered strings are not anagrams")
    
else:
    if list1==list2:  #2nd condition- if the letters in the 1st word and 2nd word match, its an anagram else, not an anagram
        print("The entered words are anagrams")
    else:
        print("Entered words are not anagrams") #as the letters in both the words do not match, it's not an anagram.


# In[ ]:





# In[ ]:




