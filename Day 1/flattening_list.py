def flatten_2d(lst):
    length = len(lst)
    # iterate for number of row times in list
    for i in range(length):
        for j in lst[0]:
            # append each element to last
            lst.append(j)
        # delete the sublist after appending    
        del lst[0]
    return lst 

# passing below 2d list in the function
my_list = [[1], [2, 3], [4, 5, 6, 7]]
flatten_list = flatten_2d(my_list)
print(flatten_list)