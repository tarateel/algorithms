'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''

def sliding_window_max(nums, k):
    # Your code here
    first = 0
    last = len(nums)
    max_nums = []
    for i in range(last - k + 1):
        first = nums[i]
        for j in range(1, k):
            if nums[i + j] > first:
                first = nums[i + j]
        max_nums.append(first)
    return max_nums
# passing: test_sliding_window_max.py
# not passing: test_sliding_window_max_large_input.py

if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")