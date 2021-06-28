# s = set()
# print(type(s))

# s.add(1)
# s.add(2)
# s.add("Arindam")
# s.add(1)
# print(s)

# l=[1, 2, 3, 1, 2, 2, 3, 100, 200]
# s=set(l)
# l.append(100)
# print(l)
# print(s)    #1,2,3, 100, 200
# s1 = s.union({1, 3, 4, 7, 8})
# print(s1)    #123478

# s1=s.intersection({1, 3, 4, 7, 8})
# print(s1)
#
# print(len(s1))
# print(min(s1))
# print(max(s1))
#
# s.remove(100)
# print(s)


s1= set({1, 2, 4})
s2= set({1, 5, 6, 8, 9})

print(s2-s1)
