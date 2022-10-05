#list, tuples, sets, dictionaries
L = [12, "Python", 24, 29] # this is a list
S = {12, "Python", 24, 29} # this is a set
T = (12, "Python", 24, 29) # this is a touple
D = {23 : "TwoThree", 'B':"Banana", 'C':23} # this is dictionary
#printing the items
print(L) # changeable
print(S) #unchangeable
print(T) #addable/removable
print(D) #changeable

#print type()
print("Type of L is ", type(L)) 
print("Type of S is ", type(S))
print("Type of T is ", type(T))
print("Type of D is ", type(D))

#deleting an item from list
del L[2]
print(L)

#appending an item into the list
L.append(6.8)
print(L)
