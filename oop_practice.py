def f(n):
    a = []
    for i in range(n):
        a.append(i**2)
    return a
print(f(10))
from datetime import *
# # Вариант 1
# # 1
# class Profile:
#     def __init__(self,heights):
#         self.heights = list(heights)
#     def maxh(self):
#         mx = -10
#         for i in self.heights:
#             if i > mx:
#                 mx = i
#         self.mx = mx
#         return self.mx
#     def minh(self):
#         mn = 10**6
#         for i in self.heights:
#             if i < mn:
#                 mn = i
#         self.mn = mn
#         return self.mn
#     def dispmax(self):
#         self.dispmx = self.mx - self.mn
#         return self.dispmx
#     def dispsum(self):       
#         dispsm = 0
#         for i in range(len(self.heights)-1):
#             dispsm += abs(self.heights[i] - self.heights[i+1])
#         self.dispsm = dispsm
#         return self.dispsm
# # p1 = Profile([1,2,3,4,5,6])
# # print(p1.maxh())
# # print(p1.minh())
# # print(p1.dispsum())

# # 2
# class Auto:
#     def __init__(self,name,power,places):
#         self.name = name
#         self.power = power
#         self.places = places
#     def quantity(self):
#         self.q = 0.1* self.power * self.places
#         return self.q
#     def __str__(self):
#         return f'name:{self.name},power:{self.power},places:{self.places},quantity:{self.q}'

# class Auto1(Auto):
#     def __init__(self,name,power,places,year):
#         self.year = year
#         super().__init__(name,power,places)
#     def quantity(self):
#         self.qp = self.q - 1.5 * (self.year - 2026)
#         return self.qp
# p1 = Auto('bmw',1000,4)
# print(p1.quantity())
# print(p1)

# # 3
# class Fraction:
#     def __init__(self,cel,ch,zn):
#         self.cel = cel
#         self._ch = ch
#         self._zn = zn
#     def __lt__(self,other):
#         if (self._ch / self._zn) + self.cel < (other._ch / other._zn) + other.cel:
#             return True
#         return False
#     def __gt__(self,other):
#         if (self._ch / self._zn) + self.cel > (other._ch / other._zn) + other.cel:
#             return True
#         return False
#     def __add__(self,other):
#         sm = self.cel + other.cel + (self._ch / self._zn) + (other._ch / other._zn)
#         return sm

# a = '2023-01-11'
# s = '0123456789'
# m = []
# for i in s:
#     if i in a:
#         m.append(i)
# print(m)




