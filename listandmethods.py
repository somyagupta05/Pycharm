l1=[3,5,345,2234,456,"somya"]
print(type(l1))
print(l1)

# modifies existing list
l1.remove("somya")
print(l1)

print(l1.count(2234))
l1.sort()
print(l1)

l1.pop()
l1.append(345)
print(l1)
# l1.clear()
l1.extend([78,89,90])
print(l1)

print(l1.index(78))

l1.reverse()
print(l1)

# mutable
l1[0]="somya"
print(l1)