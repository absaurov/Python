a = [3,4,23,4]
b = [2,4,'a',3,2,"Hi",5]
# print(type(a))
# print(b)
# for i in a:
#   print(i, end = " ")
a.append(199)
print(a)
a.insert(2,200)
print(a)
a.pop() # remove the last data
print(a)
a.remove(200)
print(a)
print(len(b))
a.sort(reverse=True)
print(a)
print(max(a))
