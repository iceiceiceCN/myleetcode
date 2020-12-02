def func():
    x = 'hello func'
    print('func1', x, id(x))

    def ifunc():
        nonlocal x
        x = 'hello ifunc'
        print('ifunc', x, id(x))
    
    ifunc()
    print('func2', x, id(x))
    
x = 'hello main'

print('main1', x, id(x))
func()
print('mian2', x, id(x))