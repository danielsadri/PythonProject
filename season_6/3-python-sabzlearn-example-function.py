# ============================================ 1 ===================================================
# تابع ای بنویسیم که دو تا عدد میگیره و برای ما مشخص میکنه این عدد تک رقمی که گرفته چند بار توی اون عدد اولی تکرار شده

# -------------------------------------------------------------
# def repeat(number, digit):
#     count = 0
#     while number > 0:
#         if number % 10 == digit:
#             count += 1
#         number //= 10
#     return count
#
#
# number = int(input('number: '))
# digit = int(input('digit: '))
#
# print(f"{digit} repeat {repeat(number, digit)} times")
# -------------------------------------------------------------
# def repeat(number, digit):
#     return str(number).count(str(digit))
#
#
# number = int(input('number: '))
# digit = int(input('digit: '))
#
# print(f"{digit} repeat {repeat(number, digit)} times")
# -------------------------------------------------------------

# ============================================ 2 ===================================================
# میخام حاصل عبارت این رو به دست بیارم
# 1! + 2! + 3! + 4! + ... + n!
# 1 + 2 ==> 3
# 1 + 2 + 6 ==> 9
# 1 + 2 + 6 + 24 ==> 33

# -------------------------------------------------------------
# def fact(n):
#     f = 1
#     for i in range(1, n + 1):
#         f *= i
#     return f
#
#
# def sum_fact(n):
#     sum_ = 0
#     for i in range(1, n+1):
#         sum_ += fact(i)
#     return sum_
#
#
# number = int(input('inter a number: '))
# print(f"sum: {sum_fact(number)}")
# -------------------------------------------------------------

# ============================================ 3 ===================================================
# تابعی بنویسیم که سه تا عدد بگیره و بزرگ ترینش و کوچک ترینش رو چاپ کنه

# -------------------------------------------------------------
# def max_3(a, b, c):
#     return max(a, b, c)
#
#
# x = int(input('x: '))
# y = int(input('y: '))
# z = int(input('z: '))
#
# print(f"max: {max_3(x, y, z)}")
# -------------------------------------------------------------
# def max_3():
#     x = int(input('x: '))
#     y = int(input('y: '))
#     z = int(input('z: '))
#     return max(x, y, z)
#
#
# print(f"max: {max_3()}")
# -------------------------------------------------------------
# def max_3():
#     x = int(input('x: '))
#     y = int(input('y: '))
#     z = int(input('z: '))
#     print(max(x, y, z))
#
#
# max_3()
# -------------------------------------------------------------
