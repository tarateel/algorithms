'''
Input: a List of integers
Returns: a List of integers
'''

def product_of_all_other_numbers(arr):
    # Your code here
    result = 1
    new_arr = []
    y = 0.50

    for x in arr:
        result *= x

    for x in arr:
        new_arr.append(result / x)

    return new_arr


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")

'''
initialize empty array
iterate over length of array
how to multiply a decimal by x?? This would get rid of the division, if it were possible to import math and do something like this:
new_arr.append(result * (0.50*x))
or
new_arr.append(result * int(math.floor(x * y)))
'''
