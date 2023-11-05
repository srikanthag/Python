# names = ["john", "eve", "bob", "emma", "ana"]
# d = {}
# for name in names:
#     d[name] = len(name)
#
# d = {}
#
# for name in names:
#     if name[0] not in d:
#         d[name[0]] = [name]
#     else:
#         d[name[0]] += [name]
# print(d)
#
#
# """ try except """
# d = {}
# for name in names:
#     try:
#         d[name[0]] += [name]
#
#     except:
#         print("in except block")


# a = 10
# b = 0
#
# # default exception block
# try:
#     # print(a / b)
#     print(l.append(10))
#
# except:
#     print("In except block")
#
# print("hello")

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


# multiple except block
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


# # Storing error message
# a = 10
# b = 0

# try:
#     print(a / b)
#     print(l.append(10))
#
# except (ZeroDivisionError, NameError) as error_msg:
#     print("In except block")
#     print(error_msg)


# generic exception block
# a = 10
# b = 0
# try:
#     print(a / b)
#     print(l.append(10))
#
# except BaseException as error_msg:
#     print("In except block")
#     print(error_msg)

# BaseException --> Exception --> all the other exceptions


# else block

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


# finally block
# username = "John"
# try:
#     if username == "John":
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


# custom exceptions

# Class UserNotAuthorizedException(Exception):
#     pass


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


# username = "j"
# if username == "John":
#    print("username is matched")
# else:
#     raise UserNotAuthorizedException("username is not present")
