import csv

with open('students.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Roll No', 'Name', 'Subject1', 'Subject2', 'Subject3'])
    writer.writerow([1, 'Jeel', 85, 90, 92])
    writer.writerow([2, 'Sidhu', 78, 82, 88])
