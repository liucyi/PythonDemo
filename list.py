word=['a','b','c','d','e','f','g']

#如何通过索引访问元组里的元素
a=word[2]
print ("a is: "+a)
b=word[1:3]
print ("b is: ")
print (b) # index 1 and 2 elements of word.
c=word[:2]
print ("c is: ")
print (c) # index 0 and 1 elements of word.
d=word[0:]
print ("d is: ")
print (d) # All elements of word.
print ("*****************************")
#元组可以合并
e=word[:2]+word[2:]
print ("e is: ")
print (e) # All elements of word.
f=word[-1]
print ("f is: ")
print (f) # The last elements of word.
g=word[-4:-2]
print ("g is: ")
print (g) # index 3 and 4 elements of word.
h=word[-2:]
print ("h is: ")
print (h) # The last two elements.
i=word[:-2]
print ("i is: ")
print (i) # Everything except the last two characters
l=len(word)
print ("Length of word is: "+ str(l))
print ("Adds new element")
word.append('h')
print (word)
print ("*********")
#删除元素
del word[0]
print (word)
del word[1:3]
print (word)