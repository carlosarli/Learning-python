x = 50
def func():
    global x
   
    print('x is', x)
    x = 2
    print('changed it :', x)

func()
print('Vlue of x is', x) 
