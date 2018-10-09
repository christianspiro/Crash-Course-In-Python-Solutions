inputList = int(input('How hard do you want to make this? Input a max value now! ==> '))
testValue = int(input('Enter a guess from 0 to the number you just selected! ==> '))
contFlag = 'y'

# binary search for guessing a number
listToGuess = range(inputList)
while contFlag != 'n':

    low = 0
    high = len(listToGuess)-1
    while low <= high:
        mid = int((low + high) / 2)
        computerGuess = listToGuess[mid]
        if computerGuess == testValue:
            print('Final Guess! ==>', computerGuess)
            contFlag = str(input('Do you want to see it again? Enter y/n for a repeat! ==>'))
        if computerGuess > testValue:
            high = mid - 1
            print("Just working it out! ==> ", computerGuess)
        else:
            low = mid + 1
            print("Just working it out! ==> ", computerGuess)
# YAH YEET

