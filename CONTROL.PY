#If statement
#IF elif
#if else


#if statement checks if the condition is true but we don't know what will happen if the condition is false.
'''
listofnumbers = [1,2,3,6]
for num in listofnumbers:
    if num == 4:
        print("number found") 
    else:
        print("number not found: ")
#if else statement shows if one statement is true and the other one is false
'''


#if elif checks if the condition is true, execute and move to the next sequencially

try:
    option = int(input("Enter option : "))
    if option == 0:
        print('Buy tunukiwa')
    elif option == 1:
        print('Buy minutes')    
    elif option == 2:
        print('Buy hours')
    elif option == 3:
        print('Buy days')
    elif option == 4:
        print('Buy weeks')
    elif option == 5:
        print('Buy months')
    else:
        print("invalid option")
except ValueError:
    print('invalid option')        


