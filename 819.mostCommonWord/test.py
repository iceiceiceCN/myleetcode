from collections import Counter
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
par = paragraph.lower().split()
list(par)
res = Counter(par)
print(res)


# for c in "!?',;.":
#     paragraph = paragraph.replace(c," ")