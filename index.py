# creating a function
def checkIfnotNumeric(*args): #defining the function
    for x in args: # using for loop
        # suppose x = 6.5, then isinstance() will return False
        # not(False) = True which defines the condition did not matched
        # So, it will not execute the if statment
        # will return True command
        if not(isinstance(x,(int))): 
            return False
    return True


