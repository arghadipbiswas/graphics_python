# mydict={
#     "fast":"in a quick manner",
#     "harry":"a codder",
#     "marks":[1,2,3],
#     "anotherict":{"harry":"player"},
#     1:12
# }
# print(mydict['fast'])
# print(mydict['harry'])
# print(mydict['marks'])
# mydict['marks']=[11,5,89,6]
# print(mydict['marks'])


#dictionary methods
# print(mydict.keys())
# print(type(mydict.keys()))
# print(mydict.values())
# print(type(mydict.values()))
# print(mydict.items())
# print(mydict)

# updatedict={
#     "love":"friend",
#     56:9
# }
# (mydict.update(updatedict))
# print(mydict)

# print(mydict.get("harry2"))   #if yes,it will show,,,if not,it will show none




# set
# a={1,2,3,4,5}
# print(a)
# print(type(a))

# a={}  # class dict
# print(type(a))

#creat empty set
# b=set()
# print(type(b))
# adding values to an empty set
# b.add(4)
# b.add(5)
# b.add(4)  # (will be ignore)
# b.add(4)  # (will be ignore)
# b.add(4)  # (will be ignore)
# print(b)


#list and dict will not add  -->unhashable
# b.add([4,5,6,7])
# print(b)
# b.add({4:5})
# print(b)


# s={1,8,2,3}
# print(len(s))
# s.remove(8)
# print(s)
# s.pop()  #pop any random value
# print(s)



# s={20,20.0,"20"}
# print(len(s))
# def factorial(n):
# 	if n == 0 or n == 1 : #Base condition which doesn’t call the function any further
# 		return n
# 	else:
# 		return n*factorial(n-1) #Function calling itself
# print(factorial(5))

# def max(n1,n2,n3):
#     if(n1>n2 and n1>n3):
#         return n1
#     elif(n2>n1 and n2>n3):
#         return n2
#     else:
#         return n3

# m =max(12892,345,498)
# print(str(m))

