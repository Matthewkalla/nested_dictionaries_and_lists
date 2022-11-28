"""
1. Update Values in Dictionaries and Lists
"""

x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# #1.1 Change the value 10 in x to 15
x[1][0] = 15


# #1.2 Change the last_name of the first student from "Jordan" to "Bryant"
students[0]['last_name'] = 'Bryant'


# #1.3 In the sports_directory, change "Messi" to "Andres"
sports_directory['soccer'][0] = 'Andres'

# #1.4 Change the value 20 in z to 30
z[0]['y'] = 30



students = [
        {
            'first_name':  'Michael',
            'last_name' : 'Jordan'
        },
        {
            'first_name' : 'John',
            'last_name' : 'Rosales'
        },
        {
            'first_name' : 'Mark',
            'last_name' : 'Guillen'
        },
        {
            'first_name' : 'KB',
            'last_name' : 'Tonel'
        }
    ]

"""
2. Iterate Trhough a List of Dictionaries
Create a function that, given a list of dictionaries, the function loops through each dicionary
in the list and prints each key and the associated value:
"""

def iterateDictionary(some_list):
    for dictionary in some_list:
        for key, value in dictionary.items():
            if key == "first_name":
                print(f" {key} - {value}", end=", ")
            else:
                print(f" {key} - {value}")    
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

iterateDictionary(students)

"""
3. Get Values From a List of Dictionaries
"""

def iterateDictionary2(key_name, some_list):
    # Go through the list
    for dictionary in some_list:
        if key_name in dictionary:
            print(dictionary[key_name])
    # for name in range(len(some_list)):
    #     print(some_list[name][key_name])


iterateDictionary2('first_name', students)

"""
4. Iterate Through a Dictionary with List Values
"""
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}


def printInfo(some_dict):
    for each_key in some_dict:
        print(f"{len(some_dict[each_key])} {each_key.upper()}")
        for list_item in some_dict[each_key]:
            print(list_item)
        print()
        # for values in range(len(each_key)):
        #     print(each_key[values])


printInfo(dojo)

