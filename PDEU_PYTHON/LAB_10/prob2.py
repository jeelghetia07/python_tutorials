import csv

students = {}
with open('students.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        total = int(row['Subject1']) + int(row['Subject2']) + int(row['Subject3'])
        students[row['Roll No']] = {
            'name': row['Name'],
            'marks': [int(row['Subject1']), int(row['Subject2']), int(row['Subject3'])],
            'total': total
        }

print(students)
