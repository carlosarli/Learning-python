drinks = ['tee','wine', 'water', 'beer']
dog = 'bauwolf'


#Indexing or 'Subscription' operation
print('drink 1 is', drinks[0])
print('drink -3 is', drinks[-3])#for negative number the position is calculated from the end of the sequence (last item is -1)
print('character 1 is', dog[0])

#Slicing
print('items 1 to 3 are', drinks[0:2])
print('items 2 to end are', drinks [1:])
print('items start to end are', drinks[:])
print('items 2 to -1 are', drinks[1:-1] #for negative number the position is calculated from the end of the sequence (last item is -1)
print('characters 1 to 3 are', dog[0:2])
