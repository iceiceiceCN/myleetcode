if 1 ^ 0:  # (if 1 ^ 0 = 1)
    print("1 ^ 0 = 1")
# ^ 相同返回true 不同返回false
if 0 ^ 0:  # (if 0 ^ 0 = 0) 0 ^ 0 =0
    print("0 ^ 0 = 0")

a = True
b = False
print(a ^ b)
print((not a) ^ b)
print((not a) ^ (not b))

m = ""
if not m: # 如果m为空
    print("m")