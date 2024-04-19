# A list consisting of 5 integers.
intList = [4,26,7,83,91]

# A for loop
for i in range (len(intList)):
    # An if statement adding the current, and next int in the list together before printing. 
    if i < 4:
        print(intList [i] + intList [i + 1])
    # An if statement adding the last, and first int in the list together before printing. 
    else:
        print(intList [i] + intList [0])
    