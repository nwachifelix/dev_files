print('''DICTIONARIES: Dictionaries is one of the four container data types in python. That is one of the data types for storing variables. Just like in the normal dictionary of words like the Oxford dictionary, it saves data in key:value pairs. Where 'key' is the place holder and 'value' is the item in it. Dictionaries are ordered/indexed, meaning they are numbered and particular items can be accessed. Its values can be changed or replaced but it does not store duplicate values just like sets. They are also stored in curly braces just like set. In this exercise, we will be creating a dictionary holding key information of the 3 major contestasnts in the Anambra governorship election, 2021 and applying the different dictionary functionalities to them.''')
print('')
contestant1 = {
    'Name' : 'Prof. Chukwuma Soludo',
    'Age' : '61 years',
    'Political Party' : 'APGA',
    'Educational Qualification' : 'Professor of Economics'
}
print(contestant1)
print('')
contestant2 = {
    'Name' : 'Valentine Ozigbo',
    'Age' : '51 years',
    'Political Party' : 'PDP'
}
print(contestant2)
print('')
contestant3 = {
    'Name' : 'Andy Uba',
    'Age' : '62 years',
    'Political Party' : 'APC'
}
print(contestant3)
print('')

print(len(contestant1))
print(contestant1.items())
print(contestant2.keys())
print(contestant3.values())
print(contestant3.get('Educational Qualification', 'Not found'))
contestant2['Educational Qualification'] = 'MBA Banking & Finance'
print(contestant2)
for key in contestant2:
    print(contestant2)
contestant1.update(contestant2)
print(contestant1)