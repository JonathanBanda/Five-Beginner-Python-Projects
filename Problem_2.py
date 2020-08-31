"""
Create a guessing number game

Learning outcomes

- Be able to make use of the random function
- Manipulate variables
- If/Else statements
- While loops

"""

# we will use this function to generate a random number

from random import randint

strikeCount = 0

keepGoing = int(input('Hello all and welcome to the random guessing game (0-50) \n'
	  'To begin enter 1 or any other key to exit! '))

hiddenNum = randint(0,50)

while keepGoing == 1:

	guess = input('Please enter a number between 0-50: ')

	if guess == hiddenNum:

		print('you got it right!!!!')
		keepGoing = False

	else:

		strikeCount += 1

		print('Try again sorry')
		print('This is your current strike ', strikeCount)

		if strikeCount == 3:
			keepGoing = False
			print('The correct number was', hiddenNum)
	

print('Thanks Bye!!')




