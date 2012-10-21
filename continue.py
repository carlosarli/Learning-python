running = True
while running:
    question = (input('login'))
    if question == 'quit':
        break
    elif (len(question)) < 3:
        print('security hazard !')
        continue
    else:
        print('thank you very much, have fun')
        running = False
print('aaaaaaaaaaaaaaaahhhhhhhh')
