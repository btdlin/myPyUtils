# fhand = open("/tmp/test")
# for line in fhand:
#     if line.startswith("From: "): continue
#     print(line.rstrip())




# nums = [x*x for x in range(5)]
# for x in nums:
#     print(x)

# print ''.format(mem_profile.memroy_usage_resource())



# import random
# import string

# print(''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8)))



# mylist = ['spam', 'ham', 'eggs']
# print(', '.join(mylist))
#print ', '.join(mylist)


# x = [1,2,3,4,5,6,7,8,9,0]
# y = [1,3,5,7,9]

# z = list(set(x) - set(y))
# print(z)

# def F(n):
#     if n == 0: return 0
#     elif n == 1: return 1
#     else: return F(n-1)+F(n-2)

# print(F(10))


def fib():
    a, b = 0, 1
    while True:            # First iteration:
        yield a            # yield 0 to start with and then
        a, b = b, a + b    # a will now be 1, and b will also be 1, (0 + 1)

for index, fibonacci_number in enumerate(fib()):
     print('{i:3}: {f:3}'.format(i=index, f=fibonacci_number))
     if index == 10:
         break
