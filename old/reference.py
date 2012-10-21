family = ['lorenzo', 'tazio', 'lapo', 'benito' 'fabrizio', 'cristina', 'alessandro', 'francesco giuseppe', 'donatella']
mylist = family #mylist now is a name that points to family

del family[3]

print(family)
print(mylist)#still the same, because they point to the same object

mylist = shoplist[:] #makes a !copy! by doing a full slice. now mylist is a list, not a name pointing to the list family
del mylist[0]

print(mylist) #without me
print(family) #with me. They are now different
