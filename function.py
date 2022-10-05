
#A function is a block of code which only runs when it is called.

# Creating a function
def f1():
    print("This is a funtion")

f1() # calling a function

# arguments 
def my_function(fname, lname): #2 arguments
  print(fname + " " + lname)

my_function("John", "Doe") #calling the function with 2 variables


#round() function
print(round(4.5))
print(round(4.3))
print(round(4.6))


#divmod() - output in touples (quotient, remainder)
print("divmod() function")
print(divmod(27,5))

#pow() function
print(pow(2,3)) # pow(x,y) - x^y
print(pow(2,3,3)) #pow(x,y,z) - (x^y)%z


#isinstance() function
print(isinstance(1, int))
print(isinstance(1.0, int))
print(isinstance(1.0,(int,float)))

