"""
# __slots__ دو مزیت
1-صرفه جویی در حافظه
2- دسترسی سریع تر به اتریبیوت
"""
"""
 __slots__ چیست؟؟؟
 یه اتریبیوت ویژه در پایتونه که اگه این رو مقدار بدید  و یه سری کلید هایی رو براش مشخص کنید فقط فقط اجازه میده
  اون کلید ها که اتریبیوت هامون هستند ایجاد بشه و جز اون ها هیچ اتریبیوت دیگه ای رو اجازه نمیده که توی کلاس ساخته بشه 
 و همچنان دیکشنری رو غیر فعال میکنه و شما نمیتونید ببینید 
"""


# ======================================================================================================================
# class MyClass:
#     __slots__ = ("a", "b", "c")
#
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b


# ------------------------------
# obj = MyClass(a=1, b=2)
# print(obj.__dict__)  # تمام اتریبیوت هایی که برای یک شی ایجاد میکنم توی یک دیکشنری ذخیره میشه و با داندر دیکت در دسترسه
# obj.c = 3
# print(obj.__dict__)
# obj.__dict__["d"] = 4
# print(obj.__dict__)
# ------------------------------
# obj = MyClass(a=1, b=2)
# obj.c = 3
# print(obj.a, obj.b, obj.c)
# ------------------------------
# ======================================================================================================================
# مشکلات __slots__ در ارث بری

# class ParentClass:
#     __slots__ = ('a', 'b')
#
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#
# class MyClass(ParentClass):
#     __slots__ = ('a', 'b', 'c')
#
#     def __init__(self, a, b):
#         super().__init__(a, b)


# -------------------------
# obj = MyClass(1, 2)
# print(obj.__dict__)
# obj.c = 3
# print(obj.__dict__)
# -------------------------
# obj = MyClass(1, 2)
# obj.c = 3
# print(obj.c)
# -------------------------

# ======================================================================================================================
