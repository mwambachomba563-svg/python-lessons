#Global variable
global_variable = 200
print("Globlal Variable 1: ", global_variable)

#Local variable 
def sayName():
    #Prining global variable 
    print("Globlal Variable 2: ", global_variable)
    
    #Make local variable and print
    local_variable = 10
    print("Locally scoped: ", local_variable)
    
#Executing a function
sayName()

#Printing local variable outside scope
#print("Locally scoped: ", local_variable)

#Print global variable
print("Globlal Variable 3: ", global_variable)