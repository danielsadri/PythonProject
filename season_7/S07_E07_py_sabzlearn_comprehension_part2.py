# =================================  1  ==========================================

# ----------------------------------------------
# c = [x for x in (1, 2, 3)]
# print(c)
# ----------------------------------------------

# =================================  2  ==========================================

# ----------------------------------------------
# set_ = {i for i in range(11) if i % 2 == 0}
# print(set_)
# ----------------------------------------------

# =================================  3  ==========================================

# ----------------------------------------------
# d = {'reza': 25, 'hossein': 19, 'danial': 18, 'mohammad': 23}
# s = {key: value for key, value in d.items()}
# print(s)
# ----------------------------------------------
# d1 = ['reza', 'hossein', 'mohammad', 'danial']
# d2 = [33, 12, 76, 17]
#
# s = {key: value for key, value in zip(d1, d2)}
# print(s)
# ----------------------------------------------

# =================================  4  ==========================================

# ----------------------------------------------
# x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# y = []
#
# for i in x:
#         y.append(i if i % 2 != 0 else 0)
#
# print(y)
# ----------------------------------------------
# x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# z = [j if j % 2 != 0 else 0 for j in x]
# print(z)
# ----------------------------------------------
# def func(x):
#     if x % 2 != 0:
#         return x
#     else:
#         return 0
#
#
# x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# z = [func(j) for j in x]
# print(z)
# ----------------------------------------------

# =================================  5  ==========================================

# ----------------------------------------------
# from random import randrange
#
#
# def func():
#     return randrange(50, 150)
#
#
# x = [n for _ in range(10) if (n := func()) > 100]
# print(x)
# ----------------------------------------------

# =================================  6  ==========================================

# ----------------------------------------------
# names = ['reza', 'hossein', 'hasan', 'akbar']
# z = {name: [0 for _ in range(5)] for name in names}
# print(z)
# ----------------------------------------------
