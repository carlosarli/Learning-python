number = 23
guess = (int(input('Enter an integer: ')))

if guess == number:
    print('yeah, buddy!')
elif guess < number:
    print('Nope, lil\' bit too low')
else:
    print('Nope, too low')
print ('Done') 
