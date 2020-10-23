left, right, count = {}, {}, {}
nums = [1, 2, 2, 3, 1]
for i, x in enumerate(nums):
    if x not in left: left[x] = i
    right[x] = i
    count[x] = count.get(x, 0) + 1 # {1: 2, 2: 2, 3: 1}
    print(count[x])
