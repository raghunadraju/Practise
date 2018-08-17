# It allows to store key values with pairs
student = {
    "name": "MARK",
    "ID": "1432",
    "name": "RAGHU"
}
a = student["name"]
b = student.keys()  # this will give you all the keys
c = student.values()  # this will give you all the values
student["name"] = "RAJU" # this will change the value of keys
del student["ID"] # this will delete the key and value
print(b, c)
