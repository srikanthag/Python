
#left justified triangle
# for row in range(5):
#     for column in range(row+1):     #inner for loop execute first
#         print("*", end=" ")
#     print()

# for row in range(1,5):
#     print("* " * row)
# *
# * *
# * * *
# * * * *

#right justified triangle
# for row in range(1,5):
#     print(f'{"* " * row:>8}')    #> justified right side
#       *
#     * *
#   * * *
# * * * *


#centrally alligned
# for row in range(1,5):
#     print(f'{"* " * row:^8}')   #^ centralize allinment


#invert left justified triangle
# for row in range(4, 0, -1):
#     print("* " * row)

#invert right justified triangle
# for row in range(4, 0, -1):
#     print(f'{"* " * row:>8}')

#inverted centrally alligned
# for row in range(4, 0, -1):
#     print(f'{"* " * row:^8}')

# left justified number pattern triangle
# for row in range(1, 5):
#     for col in range(1, row+1):
#         print(col, end=" ")
#     print()

#OR

# x = ""
# for row in range(1, 5):
#     x += str(row) + " "
#     for col in range(1, row+1):
#         print(x)

#invert left justified triangle
# for row in range(4, 0, -1):
#     for col in range(1, row+1):
#         print(col, end=" ")
#     print()

# Number Pattern in triangle (Left Justified)
# pat = ''
# for i in range(1, 6):
#     pat += str(i)
#     print(f'{pat:<5}')

# Number Pattern in triangle (Right Justified)
# pat = ''
# for i in range(1, 6):
#     pat += str(i)
#     print(f'{pat:>5}')

# Number Pattern in triangle (Centre)
# pat = ''
# for i in range(1, 6):
#     pat = pat + ' '+ str(i)
#     print(f'{pat:^10}')

# left justified number pattern triangle using abcd
# for row in range(ord("a"), ord("d")+1):
#     for col in range(ord("a"), row+1):
#         print(chr(col), end=" ")
#     print()
#
# x = ""
# for row in range(ord("a"), ord("d")+1):
#     x += chr(row) + " "
#     print(x)


# pat = ''
# for i in range(1,6):
#     pat=pat+" "+str(i)
#     print(f"{pat:^10}")


