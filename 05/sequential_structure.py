def f(i):
    return i % 10

# index copy

l1 = [1,2,3,4,5,6,7,8]
l2 = l1[:]
l3 = l1
print(l1 == l2)
print(l2 == l3)
print(l1 == l3)
print()
print(l1 is l2)
print(l2 is l3)
print(l1 is l3)

# slicing
l1[:]
l1[::-1]
# repeatation
l1 * 2
# connection
l1  + [9,0,8]
# length
len(l1)
# in, not in
4 in l1
# delete(mutable)
del l1[2]

# delete with slice
l1[2:3] = []

l10 = []
l10.append(10)
print(l10)


# sort

l11 = [10,2,33,9,8,4,11]
l11.sort(key=str)
print(l11)

#cf: sorted global function

l12 = [1,23,4,5,8,7]
l12 = sorted(l12)
print(l12)

l13 = [1,23,4,5,8,7,123,5]


l14 =sorted(l13, key=f, reverse=False)

print(l14)

