def reverse_num(n):
    reverse = remainder = 0 
    quotient = n 

    # iterate until the quotient becomes 0
    while quotient > 0:
        remainder = quotient % 10 
        quotient = int(quotient/10)
        reverse = reverse*10 + remainder
    # display the reverse of n
    print(reverse)

# calling function to reverse 9687
reverse_num(9687)