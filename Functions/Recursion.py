#recursion
# def count_(n):
#     if n <= 10:
#         print(n)
#         n += 1
#         count_(n)
#     else:
#         return
# count_(1)

#or
# def count_(n):
#     if n > 10:
#         return
#     print(n)
#     count_(n+1)
# count_(10)

# wa recursion program to print the numbers from 1, 10
# def count_(start, end):
#     if start > end:
#         return
#     print(start)
#     count_(start+1, end)
#
#
# count_(1, 10)
#
# wa recursion program to print the numbers from 10, 1
# def count_digit(start, end):
#     if start < end:
#         return
#     print(start)
#     count_digit(start-1, end)
#
#
# count_digit(10, 1)


#wa recursion program to add the digits of a number
#normal
# s = 123
# s1 = str(s)
# sum = 0
# for i in s1:
#     sum += int(i)
# print(sum)

# or 2nd normal
# num = 123
# sum = 0
# while num > 0:
#     last = num % 10
#     sum += last
#     num = num // 10
# print(sum)


# def count_(num, sum=0):
#     if num > 0:
#         last = num % 10
#         sum += last
#         num = num // 10
#         return count_(num, sum)
#     else:
#         return sum
#
#
# print(count_(123))

#warp to find the sum of first n numbers
# def count_(num, sum=0):
#     if num > 0:
#         sum += num
#         num -= 1
#         return count_(num, sum)
#     else:
#         return sum
#
#
# print(count_(5))

#warp to find the factorial of number   #important
# def fact_(num, fact=1):
#     if num > 0:
#         fact *= num
#         return fact_(num==1, fact)
#     return fact
#
#
# print(fact_(5))


# #warp to count the number of digits in a number
# def count_(num, count=0):
#     if num > 0:
#         num = num // 10
#         count += 1
#         return count_(num, count)
#     return count
#
#
# print(count_(123))

#warp to reverse a string
# def rev_string(argu, i=0, res = ""):
#     if i < len(argu):
#         res = argu[i] + res
#         return rev_string(argu, i+1, res)
#     return res
#
# print(rev_string('sri'))

#warp to print febonocii seris upto n
# def rec_feb(n):
#     if n <= 1:
#         return n
#     else:
#         return(rec_feb(n-1) + rec_feb(n-2))
# print(rec_feb(5))





