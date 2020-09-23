digits = [1,0,9]
# print(list(enumerate(digits[::-1]))) # [[index,seq[len(seq)-1-index]]]
# # print(list(enumerate(digits[::1]))) # [[index,seq[index]]]
# a = [i *10**index for index,i in enumerate(digits[::-1])]
# print(a)



def plusOne(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    a = [i * 10**index for index,i in enumerate(digits[::-1])]
    nums = sum(a) + 1
    return [int(x) for x in str(nums)]


if __name__ == "__main__":
    print(plusOne(digits))