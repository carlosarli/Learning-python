shoppinglist = ['mango', 'carrot', 'rice']

print('I have', len(shoppinglist), 'items to purchase')

print('These items are:', end='')

for item in shoppinglist:
    print(item, end='')
print('\nI also have to buy pasta !')
shoppinglist.append('pasta')

print('Right, now I am ready, with my new shoppinglist:', shoppinglist)

shoppinglist.sort()

print("Great, I have bought the", shoppinglist[0], " Let's strike it off")
olditem = shoppinglist[0]
del shoppinglist[0]
print('done. now my shoppinglist is only', len(shoppinglist), 'long, since i bought the', olditem)
