from bisect import bisect_right


l = [2, 3, 5]
limit = bisect_right(l, 2)
print(limit)
