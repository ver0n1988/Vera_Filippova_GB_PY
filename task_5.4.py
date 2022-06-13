src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
res=[number for i, number in enumerate(src) if i > 0 and src[i] > src[i - 1]]

print(res)



