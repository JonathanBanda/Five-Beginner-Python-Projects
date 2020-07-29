# Problme 1

"""

Nest loops to create a function that will produce the outcome shown below.
Function should take in 3 parameters -->> (number of blocks, number of rows, number of stars in each row)
The function should be print out the correct number of blocks, and stars


starLoop(2, 6, 8)

********
********
********
********
********
********

********
********
********
********
********
********

"""


def starLoop(i, j, k):
    for x in range(i):
        print("\n", end='')
        for y in range(j):
            print("\n", end='')
            for z in range(k):
                print("*", end='')


starLoop(2, 6, 8) # two blocks each with 6 rows each with 8 stars
#starLoop(2,2,3)
#starLoop(3,2,3)
#starLoop(4,2,3)

