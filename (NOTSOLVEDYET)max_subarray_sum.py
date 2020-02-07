def maxSequence(arr):
    max_so_far = max_ending_here = arr[0]
    for i in arr[1:]:
        max_ending_here = max(i, max_ending_here + i)
        max_so_far = max(max_so_far, max_ending_here)
    print(max_so_far)

maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
