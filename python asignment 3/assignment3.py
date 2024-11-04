
student_names = ['sandra', 'patricia', 'phiona', 'Anita']
student_marks = [80, 56, 78, 90]

# print Patricia, faith, Phionah and Anitah
# the list of student names
students_names = ['Sandra', 'Patricia', 'Phiona', 'Anita']

# i Print the specific names
print(students_names[1])  # Patricia
print('Faith')             # 'Faith' is not in the list, but added as a string
print(students_names[2])  # Phiona
print(students_names[3])  # Anita

# Add Masha at the forth position.

# the real list of student names
students_names = ['Sandra', 'Patricia', 'Phiona', 'Anita']

# i put  'Masha' at the fourth position (index 3)
students_names.insert(3, 'Masha')

#i Print the updated list
print(students_names)



# update the name phionah to phionah aladkna
# the real  list of student names
students_names = ['Sandra', 'Patricia', 'Phiona', 'Masha', 'Anita']

# i Update 'Phiona' to 'Phiona Aladkna'
students_names[2] = 'Phiona Aladkna'  # Index 2 corresponds to 'Phiona'

# i Print the updated list
print(students_names)

# display the length of the student list 
# the real list of student names
students_names = ['Sandra', 'Patricia', 'Phiona Aladkna', 'Masha', 'Anita']

# i Get the length of the list
length_of_list = len(students_names)

# Print the length
print("Length of the student list:", length_of_list)

#print all the student names using a for loop 

# List of student names
students_names = ['Sandra', 'Patricia', 'Phiona Aladkna', 'Masha', 'Anita']

# Print each name using a for loop
for name in students_names:
    print(name)

# calculate the total marks for the students marks variable

# List of student marks
student_marks = [80, 56, 78, 90]

# Calculate the total marks
total_marks = sum(student_marks)

# Print the total marks
print("Total marks:", total_marks)