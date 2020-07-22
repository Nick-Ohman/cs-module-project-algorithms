'''
Input: a List of integers
Returns: a List of integers
'''

# we need to move the 0 ints to the end of list
# could i pop off the 0's and re append them?


def moving_zeroes(arr):
    # Your code here

    for i in arr:
        if i == 0:
            arr.remove(i)
            arr.append(i)
    return arr



if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")