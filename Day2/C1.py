l=[1,5,66,1,0]
print(l.count(1))
l.sort()
print(l)
print(l.index(66))
a = ['A', 'a', -11, 45, 33, 67]
a.sort(key=lambda x: ord(str(x)) if isinstance(x, str) else x)
print(a)

