# There are only two main loops in Python (FOR, WHILE)

Names = ["RAGHU", 'SRINI', '', 1, 'SHREYA', 'SURYA']

for Names in Names:
    if Names == "SHREYA":
        print("Found him "+Names)
        break  # for loop stops after the condition satisfied
    print('Student Name is {0}'.format(Names))  # Printing all the objects in the list using for loop

a = 2
for index in range(2):
    a += 2
    print("iterations {0}".format(a))

