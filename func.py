# # # def factorial_iter(n):
# # #     res = 1
# # #     for i in range(1, n + 1):
# # #         res *= i
# # #     return res

# # # def factorial_rec(n):
# # #     if n == 0:
# # #         return 1
# # #     return n * factorial_rec(n - 1)

# # depth = 0  # глобальная переменная

# # def factorial_debug(n):
# #     global depth
# #     print(" " * depth + f"factorial({n})")
# #     depth += 4
    
# #     if n == 0:
# #         depth -= 4
# #         return 1
    
# #     result = n * factorial_debug(n - 1)
# #     depth -= 4
# #     return result

# # indent = 0

# # def printIn(s):
# #     global indent
# #     print(" " * indent + s)
# #     indent += 4

# # def printOut(s):
# #     global indent
# #     indent -= 4
# #     print(" " * indent + s)

# # def factorial_full(n):
# #     printIn(f"factorial({n})")
    
# #     if n == 0:
# #         printOut("1")
# #         return 1
    
# #     result = n * factorial_full(n - 1)
    
# #     printOut(str(result))
# #     return result

# # def fib(n):
# #     if n == 0:
# #         return 0
# #     elif n == 1:
# #         return 1
# #     elif n > 1:
# #         return fib(n-1) + fib(n-2)
# #     elif n == -1:
# #         return -1
# #     elif n < -1:
# #         return fib(n+1) + fib(n+2)
    
# # print(fib(-6))

# # def printIn(s):
# #     global p
# #     print(p*'    '+s)
# #     p +=1

# def plus(a,b):
#     ''' plus '''
#     return a + b

# def minus(a,b):
#     ''' minus '''
#     return a - b

# def hello(a,b):
#     ''' hello '''
#     return f'Hello {a} and {b}'

# def func(*a):
#     d = {}
#     for i in a:
#         d[i.__doc__.split()[0]] = i
#     return d

# # print(func(plus,minus,hello))
# d = func(plus,minus,hello)
# def inputt():
#     flag = 1
#     while flag:
#         i = input()
#         if i == 'plus':
#             print(d['plus'](5,2))
#         elif i == 'minus':
#             print(d['minus'](5,2))
#         elif i == 'hello':
#             print(d['hello'](5,2))
#         else:
#             flag = 0
#     return 'finish'

bash = 31
c_and_c_plus_plus = 29
c_sharp = 11
html_css = 36
java = 19
javascript = 37
sql = 34
a = [bash,c_and_c_plus_plus,c_sharp,html_css,java,javascript,sql]
def analyze_skills(a):
    print(f'Доля питонистов, у которых есть наименее популярный навык (в %): ',min(a))
    print(f'Доля питонистов, у которых есть наиболее популярный навык (в %): ',max(a))
print(analyze_skills())