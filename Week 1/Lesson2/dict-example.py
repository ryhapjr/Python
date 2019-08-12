student = {
    'Name': 'Randy',
    'Age': 28,
    'Address': '56 Bay Street, Staten Island, 1001',
    'Grades': [100, 100, 100],
    'Account_Numbers': (1001, 1002, 1003)
}

print(type(student))
print(student)

print(student.keys())
print(student.values())

student['Height'] = 5.6

print(student)

student['Name'] = 'John'

print(student)

print(type(student['Name']))
print(type(student['Age']))
print(type(student['Address']))
print(type(student['Grades']))
print(type(student['Account_Numbers']))
print(type(student['Height']))
