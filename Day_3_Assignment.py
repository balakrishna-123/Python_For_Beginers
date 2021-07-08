# Asignment 3 - 

# 1. Learn about in built functions of Python objects 

                                                                           # a. List 
#List -> [] ,ordered , indexed , changable , allow duplicates
#ordered
fruits=["apple","orange","mango"]
print(fruits)

#indexed
print(fruits[1])
print(fruits[-1])

#slicing
print(fruits[1:3])
print(fruits[-3:-1])

#changable
fruits[2]="papaya"
print(fruits)

#allow duplicates
fruits=["apple","orange","mango","apple"]
print(fruits)

#loop
for data in fruits:
    print(data)

#membership
print("orange" in fruits)

#List method
#length
print(len(fruits))

#append->data will be added at the end of the list
fruits.append("grapes")
print(fruits)

#insert
fruits.insert(2,"guava")
print(fruits)

#remove
fruits.remove("orange")
print(fruits)

#pop->last data will be popped out
fruits.pop()
print(fruits)

                                                       
  
  
  
                                                               # b. Dict
    #ordered
fruits=["apple","orange","mango"]
print(fruits)

#indexed
print(fruits[1])
print(fruits[-1])

#slicing
print(fruits[1:3])
print(fruits[-3:-1])

#changable
fruits[2]="papaya"
print(fruits)

#allow duplicates
fruits=["apple","orange","mango","apple"]
print(fruits)

#loop
for data in fruits:
    print(data)

#membership
print("orange" in fruits)

#List method
#length
print(len(fruits))

#append->data will be added at the end of the list
fruits.append("grapes")
print(fruits)

#insert
fruits.insert(2,"guava")
print(fruits)

#remove
fruits.remove("orange")
print(fruits)

#pop->last data will be popped out
fruits.pop()
print(fruits)

 
                                                                   # c. Tuple
    
#() ,ordered ,indexed , unchangable , allow duplicates
names=("hari","nikhil","bala","shreya","shushmitha")

#ordered
print(names)

#indexed
print(names[2])
print(names[-5])
#slicing
print(names[-5:])
print(names[:4])

#unchangable
'''
names[2]="balakrishna"
print(names)#TypeError: 'tuple' object does not support item assignment
'''
#change tuple value using list
data=list(names)
print(type(data))
data[2]="balakrishna"
print(data)
names=tuple(data)
print(names)

#loop
for i in names:
    print(i)

#membership
print("bala" in names)
print("hari" not in names)

#del
del names
#print(names)#NameError: name 'names' is not defined
names=("hari","nikhil","bala","shreya","shushmitha")
t1=(20,21,22,23,24)
print(names+t1)

#length
print(len(names))

#add->we cant able to add or modify data in list
#names[5]="kishore"
#print(names)



                                                    # d. Set
  
#{} ,unordered ,unindexed , unchangable , doesn't allow duplicates
names={"hari","nikhil","bala","shreya","shushmitha"}

#unordered
print(names)

#unindexed
#print(names[2])
#TypeError: 'set' object is not subscriptable

#slicing-> there is no concept slicing in set

#unchangable
#names[2]="balakrishna"
#print(names)#TypeError: 'set' object does not support item assignment

#looping
for data in names:
    print(data)

#membership
print("nikhil" in names)

#add
names.add("python")
print(names)

#pop
print(names.pop())
print(names)

#update-> we can use list or tuple
#names.update("akash","kishore")
names.update(["akash","kishore"])
print(names)

#length
print(len(names))

#remove
names.remove("python")
print(names)
#names.remove("python")#KeyError: 'python'
#discard-> it will not raise any error if the data is already removed
names.discard("akash")
print(names)
names.discard("akash")

#clear
names.clear()
print(names)
#del
s1={1,2,3}
del s1
#print(s1)#NameError: name 's1' is not defined

names={"hari","nikhil","bala","shreya","shushmitha"}

#union
s1={1,2,3}
set1=s1.union(names)
print(set1)

#update
s2={"a","b","c","d"}
s3={1,2,3}
s2.update(s3)
print(s2)



                                                                     # e. String 
  

a="python"
a='python'

print(a)

#indexed
#postive indexing
print(a[0])#p
print(a[3])#h

#Negative indexing
print("a[-2]:",a[-2])#o
print(a[-4])#t

#slicing
#positive slicing
print(a[0:2])#py
print(a[2:])#thon
print(a[:4])#pyth

#negative slicing
print(a[-4:-1])#tho
print(a[-3:])#hon
print(a[:-2])#pyth

print(a[:])#python

#String methods
data="python language"
#length
print(len(data))
#strip
name="  good  "
print(name)
print(len(name))
name=name.strip()
print(name)
print(len(name))

#upper
print(name.upper())

#lower
name1="AWESOME"
print(name1.lower())

#titile
txt="monty python"
print(txt.title())

#replace
print(txt.replace("monty", "language"))
print(txt.replace("ho","o"))

#count
print(txt.count("t"))

#split
# by . , char space
txt="python is intresting language to learn"
print(txt.split(" "))
txt="python is intresting language, to learn"
print(txt.split(","))

#membership
print("python" in txt)

#string concatenation
print(name+(name1.lower()))

#string format
orange=int(input("enter number of orange u want:"))
price=int(input("enter your price:"))
text="i want {} number of orange for Rs {}"
print(text.format(orange,price))
