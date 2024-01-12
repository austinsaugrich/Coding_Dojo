
x = [[5, 2, 3], [10, 8, 9]]
students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]
sports_directory = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer': ['Messi', 'Ronaldo', 'Rooney']
}
z = [{'x': 10, 'y': 20}]

# change 10 to 15
x[1].pop(0)
print(x)
x[1].insert(0, 15)
print(x)

# change the last name of the first student to Bryant
students[0]['last_name'] = 'Bryant'
print(students)

# in sports, change messi to andres
sports_directory['soccer'][0] = 'Andres'
print(sports_directory)

# change 20 to 30 in z
z[0]['y'] = 30
print(z)


# create a function that prints out each name side by side
students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]


def iterateDictionary(students):
    for i in students:
        print(i)


iterateDictionary(students)

# create a function that prints out first names


def iterateDictionary2(key_name, some_list):
    for obj in some_list:
        if key_name in obj:
            print(obj[key_name])
        else:
            return


iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)

# Create a function printInfo(some_dict) that given a dictionary whose values are all lists, prints the name of each key along with the size of its list, and then prints the associated values within each key's list.

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}


def printInfo(some_dict):
    for key in some_dict:
        print(len(some_dict[key]), key)
        for value in some_dict[key]:
            print(value)


printInfo(dojo)
