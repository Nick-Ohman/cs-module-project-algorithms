'''
Input: a List of integers
Returns: a List of integers
'''
from functools import reduce
## are are going to mult all numbers expect the index at that index
def product_of_all_other_numbers(arr):
    # Your code here
    # total = reduce((lambda x, y: x * y), arr)
    # # print(total)
    # new_list = []
    # new_list.append(total)
    # new_list.append(total)
    # new_list.append(total)
    # new_list.append(total)
  
    
    # # print(arr)
    # # print(new_list)
    
    # res = [i / j for i, j in zip(arr, new_list)]
    # print(res)
    # return total

    

    # solution = []
    # # loop thru array indices
    # for i in range(len(arr)):
    #     # init product
    #     product = 1

    #     # problem clearly hints at division,
    #     # multiply all values in array and divide by arr[i]
    #     for x in arr:
    #         product = product * x

    #     product = product/arr[i]
    #     solution.append(product)

    # return solution  
    new = []

    num = 1
    for x in arr:
        num = num * x
    
    for y in arr:
       new.append(num/y)

    return new

    
    


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 2, 3, 4, 5]
    # arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
