#for loop executes a block of code as long as their is an item in a sequence.
listofnumbers = [1, 2, 3, 4, 5, 6, 7]
listofcolours = ['red', 'green', 'blue', 'yellow', 'orange', 'purple' ]
list = [ 20,40, 60,80,'kenya','uganda','tanzania']
'''
for num in listofnumbers:
    #here we print out the initializer ; will give you all the indexes in the list
    print(num)
    num = num + 1
    print("after",num)
    '''
#NB use multiline comment starting three quotes and ending three quotes

#for loop implementation in a list of cclours.

for colour in listofcolours:
    if colour == "green":
        print('colour found')
    else:
        print('colour not found')

    




