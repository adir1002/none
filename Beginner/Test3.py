x=12
y=0

try:  
    pass
    print(x/y)
except ZeroDivisionError as e:
    print('1')
    pass
except :
    print('2')
finally:
    pass
    print('3')