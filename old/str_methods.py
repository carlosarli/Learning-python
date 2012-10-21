name = 'lorenzo' #this is a string object

if name.startswith('lo'):
    print('yes')
if name.find('lo') != -1: #.find finds the position of a string in a string, and returns -1 if it's not succesfull in finding the string in the string
    print('yes')
delimiter = '.'
namelist = ['l', 'o', 'r', 'e', 'n', 'z', 'o']
print('imma the new florida: ', delimiter.join(namelist))#.join substitutes commas and spaces  between strings in a list with a given string
