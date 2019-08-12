grades = [100, 20, 99, 45.4, 100, 99]
print(grades)

# appending to the end of the list
grades.append(500)
print(grades)

# count return how many dups
print(grades.count(99))

# remove the item from the given index
grades.pop(2)

print(grades)

# insert the item at the given index
grades.insert(2, 500)

print(grades)

# make a copy of the object
grade_copy = grades.copy()

grades.sort()

print(grades)

grades.reverse()

print(grades)

print(grades[2])

grades[2] = 2.2

print(grades)
