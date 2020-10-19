nums = [1,0,1,1,0,1]
list(map(str,nums)) # ['1', '0', '1', '1', '0', '1']
print(''.join(map(str,nums)))  # 101101
print(''.join(map(str,nums)).split('0'))  # ['1', '11', '1']
print(max(''.join(map(str,nums)).split('0'))) # 11 得到最大的值，11大于1 越长的1序列越大
print(len(max(''.join(map(str,nums)).split('0')))) # 2