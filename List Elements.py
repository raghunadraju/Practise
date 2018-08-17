Names = ["RAGHU", 'SRINI', '', 1, 'SHREYA', 'SURYA']

a = Names[0]  # 0 means first object in the list
b = Names[1]

del Names[-1]  # Delete string from list

c = Names[-1]  # -1 means last object in the list
d = Names[-2]
print(a, b, c, d)

Names.append("SATISH")  # Adding string to list

e = len(Names)  # Finding number of elements in the list
print(e)

f = "HARI" in Names  # Check the specified name exists in the list or not
g = int(f)
print(f, g)

h= Names[1:]  # list slicing mean temporary ignoring the elements
i = Names[4:-1]
print(h)
print(i)
