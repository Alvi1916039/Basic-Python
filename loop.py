"""
#for
L = [] #array
for i in range(0,10,2): #range(initialization, end, increment)
    print(i) 
    L.append(i) #putting the values of i into the array
print(L)



#while
n = int(input("Enter any integer: "))
i = 1 #initialization
while i<n: #condition
    print(i)
    i = i+1 #increment



#break
i = 1 #initialization
while True:
    if i % 9 == 0:
        print("INSIDE IF BLOCK")
        break
    else:
        print("INSIDE ELSE")
    i = i + 1
"""
"""
#continue
i = 1 #initialization
while True:
    if i % 9 == 0:
        print("INSIDE IF BLOCK")
        continue
    else:
        print("INSIDE ELSE")
    i = i + 3
"""

