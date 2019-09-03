import time

start_time = time.time()

# for a in range(1001):
#     for b in range(1001):
#         for c in range(1001):
#             if 1000 == a + b + c and a**2 + b**2 == c**2:
#                 print("a, b, c: %d, %d, %d" % (a, b, c))

# 280.911694

# 1000 * 1000 * 1000 * 10 = 10 * 1000^3 = T

# T(n) = 10 * n^3   =   O(n^3)



for a in range(1001):   #  2000
    for b in range(1001):
        c = 1000 - a -b     # 3
        if a**2 + b**2 == c**2:  # 5
            print("a, b, c: %d, %d, %d" % (a, b, c)) # 2


# 1000 *  1000 *  (3+5+2)   = 10 * 1000^2 = T

# 时间复杂度  T(n) = 10 * n^2     O(n^2)


# 基本运算总数 * 基本运算的单位时间

# cost: 1.838194

end_time = time.time()
cost = end_time - start_time
print("cost: %f" % cost)


# li = [1,3,2,7,3,2,4,6]  -> [1, 2, 3, 3, 4,5 6]
#
# T(n)
#
# [1,2,3,4,5,6,7]


























