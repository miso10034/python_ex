# def add(a,b):
#     return a+b

# def add1():
#     a = input('a=')
#     b = input('b=')
#     print(a+b)
#     return

    
# def add2():
#     a = input('a=')
#     b = input('b=')
#     print(a+b)
#     return a+b

# def add(a,b):
#     a[0] =b
#     print('in',a)
#     return a

# a=7
# b=3
# print('out',add(a,b))
# print('out',a,b)

# a = [1,2,3]
# b = [4,5,6]
# print('out',add(a,b))
# # print('out',a,b)

# def test(t):
#     print(x)
#     t=20
#     print('in:',t)

# x = 10
# test(x)
# print('out:',x)
# print('out:',t)


# def f():
#     global s
#     s ="i love london!"
#     print(s)

# s="i love paris!"
# f()
# print(s)

# def factorial(n):
#     if n==1:
#         return 1
#     else:
#         return n*factorial(n-1)

# print(factorial(int(input("Input Number for Factorial Calculation:"))))

# def add(a=2,b):
#     return a+b

# print(add(2))

def add(**a):
    print(a)

print(add(a=1,b=3,f=6))