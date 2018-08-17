student = {
    "name": "MARK",
    "ID": "1432",
}
student["lastname"] = "RAJU"
try:
    lastname = student["lastname"]
    a = 1 + lastname
except KeyError:
    print("error finding lastname")
except TypeError as error:  # this is to print the error message description
    print("Not able to add Integer and String together")
    print(error)
except Exception:  # Generice exception
    print("Unknown Error")
