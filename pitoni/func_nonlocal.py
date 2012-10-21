def func_outer():
    x = 2
    print('x is', x)
    def func_inner():
        nonlocal x
        x = 10
        print('look, I have chaned x !:', x)
    func_inner()
    print('He really did ! look !', x)
func_outer()

