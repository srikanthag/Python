'''Exception handling'''

'''1. Exception handling 01'''
# names = ["john", "eve", "bob", "emma", "ana"]
#
# """ try except """
# d = {}
# for name in names:
#     try:
#         d[name[0]] += [name]
#
#     except:
#         print("in except block")


''' 2. Exception handling 02 '''
# a = 10
# b = 0
#
# try:
#     print(a / b)
#     print(l.append(10))
#
# except:
#     print("In except block")
#
# print("hello")


''' 3. Exception handling 03 '''
# specific exception block
# a = 10
# b = 0
# try:
#     print(a / b)
#     print(l.append(10))
#
# except ZeroDivisionError:
#     print("In except block")
#
# print("hello")


''' 4. Exception handling 04 (Multiple except error) '''
# a = 10
# b = 0
# try:
#     print(a / b)
#     print(l.append(10))
#
# except ZeroDivisionError:
#     print("Zero division handled")
#
# except NameError:
#     print("name error handled")
#
# print("hello")


''' 5. Exception handling 05 (Store error message) '''
# a = 10
# b = 0

# try:
#     print(a / b)
#     print(l.append(10))
#
# except (ZeroDivisionError, NameError) as error_msg:
#     print("In except block")
#     print(error_msg)


''' 6. Exception handling 06 (Base exception) '''
# BaseException --> Exception --> all the other exceptions

# a = 10
# b = 0
# try:
#     print(a / b)
#     print(l.append(10))
#
# except BaseException as error_msg:
#     print("In except block")
#     print(error_msg)


''' 7. Exception handling 07 (Else block) '''

# username = "johnny"
#
# try:
#     if username == "srikanth":
#        print("username is matched")
#     else:
#         raise NameError("username is not present")
#
#
# except BaseException as error_msg:
#     print("In except block")
#     print(error_msg)
#
# else:
#     print("in home page")


''' 8. Exception handling 08 (Finally block) '''

# username = "John"
# try:
#     if username == "Sri":
#        print("username is matched")
#     else:
#         raise NameError("username is not present")
#
# except BaseException as error_msg:
#     print("In except block")
#     print(error_msg)
#
# else:
#     print("in home page")
#
# finally:
#     print("closing the browser")


''' 9. Exception handling 09 (Custom exception)'''

# class UserNotAuthorizedException(Exception):
#     pass
#
# username = "Johnny"
# try:
#     if username == "John":
#        print("username is matched")
#     else:
#         raise UserNotAuthorizedException("username is not present")
#
# except BaseException as error_msg:
#     print("In except block")
#     print(error_msg)
#
# else:
#     print("in home page")
#
# finally:
#     print("closing the browser")



