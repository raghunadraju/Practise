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

c=set([1,2,1,3,2]) # which will remove duplicates from the list
print(c)
# Get three test score
round1 = int(input("Enter score for round 1: "))

round2 = int(input("Enter score for round 2: "))

round3 = int(input("Enter score for round 3: "))

# Calculate the average
average = (round1 + round2 + round3) / 3

# Print out the test score
print("the average score is: ", average)

import string
from random import *
characters = string.ascii_letters + string.punctuation  + string.digits
password =  "".join(choice(characters) for x in range(randint(8, 16)))
print(password)