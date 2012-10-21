addressbook = {  'Lorenzo' : '3331791375',
                  'Cristina' : '3396331004',
                  'Fabrizio' : '3382110127',
                  'Casa' : '051231608'
             }
print("Lorenzo's number is", addressbook['Lorenzo'])

del addressbook['Casa']

print('there are now {0} contacts'.format(len(addressbook))

for name, telephone in addressbook.items():
    print('Contact {0} at {1}'.format(name, number))

addressbook['Canuc'] = '0516490699'

if 'Guido' in addressbook:
    print('Er numero de Guido e:' addressbook['Guido'])
