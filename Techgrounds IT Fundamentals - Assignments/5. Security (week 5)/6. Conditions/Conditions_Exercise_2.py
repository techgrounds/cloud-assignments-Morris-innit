# Declared an 'x' variable so that the while loop can be executed.
x = 0

# A while loop used to repeat the if else statements until the integer 100 is entered by the user.
while x != 100:
    # A variable containing the result of an input Function.
    x = int(input("Give a number please: "))

    # A variable used as comparison in the if else statements.
    y = 100

    # A series of if else statements to reply to the given input to variable 'x', 
    # where the goal is for the user to input a value of 100.
    if x == y:
        print("Right on the money.")
    elif x < y:
        print("Is " + str(x) + " all you got?")
    else:
        print("Fudging bells, don't you think " + str(x) + " is a little high?")