def squres(l):
    for item in l:
        yield item**2

r = squres([5,6,7])
print(r)        # Returns generator object (<generator object squres at 0x000001EBD2882260>)

for t in r:
    print(t)


































