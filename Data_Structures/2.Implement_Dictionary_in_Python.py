# You are familiar with most of the properties of dictionaries in Python. Add some more info about the dictionary through dictionary formatting and deleting key-value pairs.

# Let's get this into head by solving a question. Given some queries for dictionary.

# The task is to do some operations as described below:

# a. i key value: Driver code calls the function insert_dict() which inserts key and value in the dictionary, and prints 'Inserted'.
# b. d key: Driver code calls the function del_dict() which deletes the entry for a given key and prints 'Deleted' if the key to be deleted is present, else prints '-1'.
# c. key: print marks of given key in statement as "Marks of {student_name} is : {marks}". If key is not present print '-1'.


# insert into dictionary and print "Inserted"
def insert_dict(key, value, Dict):
    Dict[key] = int(value)
    print("Inserted")


# deleting from dictionary and print "Deleted" if key present else "-1"
def del_dict(key, Dict):
    if key in Dict:
        del Dict[key]
        print("Deleted")
    else:
        print('-1')


# print marks of student whos name is key if student name is present in Dict else "-1"
def print_dict(key, Dict):
    if key in Dict:
        print("Marks of " + key + " is " + str(Dict[key]))
    else:
        print("-1")