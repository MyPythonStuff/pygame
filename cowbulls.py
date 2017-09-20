import random

num = list(str(random.randint(1000, 9999)))
count = 0
guess = ""

while guess != num:
    cond = True
    guess = list(input('Guess the 4-digit number : '))
    cows = 0
    bulls = 0
    for i in range(4):
        if len(guess) != 4:
            print('incorrect input')
            cond = False
            break
        else:
            if num[i] == guess[i]:
                cows += 1
            elif guess[i] in num and num[i] != guess[i]:
                bulls += 1
    if cond:
        print ("Cow(s): %d" % cows)
        print ("Bull(s): %d" % bulls)
        count += 1


print('You took %d guesses' %count)
