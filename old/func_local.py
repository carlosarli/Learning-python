x = 50
def func(x):
    print('Did I say x =', x)
    x = 2
    print('I meant that x =', x)
func(x)
print('I see no changes !, x is still', x)
