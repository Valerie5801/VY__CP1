#VY 2nd Multiplication Table

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
row = []

for num in nums:
    for i in range(1, 13):
        result = i * num
        row.append(result)
    print(row)
    row = []