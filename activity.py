#A function named hello() that prints a greeting to the user. This function should accept no arguments and returns nothing.
def hello():
    print('hello')

hello()

#A function named pack() that accepts three arguments, and returns a single list with the three arguments inside as list elements.
def pack(a ,b, c):
    listed = [a, b, c]
    print(listed)
    return listed

pack("yes", "no", "maybe")

#A function called eat_lunch(). This function should accept a list of any length, and print out a series of strings that say "First I eat __" (the first element of the list), and "Next I eat ___" (for the following elements in the list). If the list is empty, print "My lunchbox is empty!". The function should not return anything. 
def eat_lunch(*args):
    if not args:
        print("My lunchbox is empty!")
    else:
        for i in range(len(args)):
            if i == 0:
                print("First I eat", args[i])
            else:
                print("Next I eat", args[i])

eat_lunch()
eat_lunch("pie", "burger", "apple")

