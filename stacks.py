class Stack:
    def __init__(self, lm=10):
        self.sp = []
        self.lm = lm

    def push(self, elem):
        if self.len() == self.lm:
            raise OverflowError("stack is overflow")

        self.sp.append(elem)

    def pop(self):
        if self.is_empty():
            raise IndexError("stack is empty")

        return self.sp.pop()

    def is_empty(self):
        return len(self.sp) == 0

    def top(self):
        if self.is_empty():
            raise IndexError("stack is empty")

        return self.sp[-1]

    def len(self):
        return len(self.sp)

# s1 = Stack()
# s2 = Stack()
# s3 = Stack()
# s1.push(1)
# s1.push(2)
# s1.push(3)
# s1.push(4)
# s1.push(5)
# s1.push(6)
# print(s1.__dict__)

# # n = len(s1.sp)
# # if n % 2 == 1:
# #     k = n // 2
# #     for i in range(k):
# #         s2.push(s1.pop())
# #     s1.pop()
# # else:
# #     k = n // 2 - 1
# #     for i in range(k):
# #         s2.push(s1.pop())
# #     s1.pop()
# #     s1.pop()

# # while not s2.is_empty():
# #     s1.push(s2.pop())
# # print(s1.sp)

# # #3 Удалить элемент, который находится в середине сте-ка, если нечетное число элементов, а если четное, то два сред-них.
# # n = len(s1.sp)
# # if n % 2 == 1:
# #     k = n // 2
# #     for i in range(k):
# #         s2.push(s1.pop())
# #     s1.pop()
# # else:
# #     k = n // 2
# #     for i in range(k - 1):
# #         s2.push(s1.pop())
# #     s1.pop()
# #     s1.pop()
# # while not s2.is_empty():
# #     s1.push(s2.pop())

# # print(s1.sp)

# #4 Удалить каждый второй элемент стека
# # for i in range(1,s1.len()+1):
# #     if i % 2 == 0:
# #         s2.push(s1.pop())
# #     else:
# #         s1.pop()

# # while not s2.is_empty():
# #     s1.push(s2.pop())

# # print(s1.__dict__)

# # flag = True
# # code = '((dsasdas((das(d)das)d)asd)da)'
# # for i in code:
# #     if i == '(':
# #         s1.push(i)
# #     elif i == ')':
# #         if s1.is_empty():
# #             flag = False
# #             break
# #         s1.pop()

# # if not s1.is_empty():
# #     flag = False
# # if flag:
# #     print("нет ошибок")
# # else:
# #     print("ошибка")

# #7  Найти максимальный элемент и вставить после него «0»
# s = Stack()
# s1 = Stack()

# max_elem = s.top()

# while not s.is_empty():
#     x = s.pop()

#     if x > max_elem:
#         max_elem = x

#     s1.push(x)

# flag = 0

# while not s1.is_empty():
#     x = s1.pop()

#     s.push(x)

#     if x == max_elem and flag == 0:
#         s.push(0)
#         flag = 1

# #8
# s = Stack()
# s1 = Stack()

# min_elem = s.top()

# while not s.is_empty():
#     x = s.pop()

#     if x < min_elem:
#         min_elem = x

#     s1.push(x)

# flag = 0

# while not s1.is_empty():
#     x = s1.pop()

#     if x == min_elem and flag == 0:
#         flag = True
#         continue

#     s.push(x)

# удалить все пятерки 

# s = Stack()
# s1 = Stack()

# s.push(1)
# s.push(2)
# s.push(5)
# s.push(1)
# s.push(5)

# while not s.is_empty():
#     x = s.pop()

#     if x != 5:
#         s1.push(x)

# while not s1.is_empty():
#     s.push(s1.pop())

# print(s.__dict__)