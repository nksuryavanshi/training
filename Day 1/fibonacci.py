def fibonacci(n):
    # initializing a->0 and b->1
    a, b = 0, 1
    for i in range(n):
        print(a)

        '''
        passing value of b to a and updating
        b with the addition of a and b
        '''
        temp = a+b
        a = b 
        b = temp 

# first 10 numbers in fibonacci series
fibonacci(10)