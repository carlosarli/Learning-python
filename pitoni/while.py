number = 23
running = True

while running:
    guess = int(input('guess it, cmon'))
    if guess==number:
        print('we got ourselves a winer, folks!')
        running = False
    elif guess < number:
        print('is that the only minor thing you got ?')
    else:
        print('this guy likes to shot them high !')
else:
    print('the while loop is over')
