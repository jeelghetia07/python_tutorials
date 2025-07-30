employees = [{'dept_no' : 101 , 'emp_roll no ' : 'E001', 'salary' : 50000}, 
             {'dept_no' : 101 , 'emp_roll no ' : 'E002', 'salary' : 60000},
             {'dept_no' : 102 , 'emp_roll no ' : 'E003', 'salary' : 45000},
             {'dept_no' : 102 , 'emp_roll no ' : 'E004', 'salary' : 70000},
             {'dept_no' : 103 , 'emp_roll no ' : 'E005', 'salary' : 80000},
             {'dept_no' : 103 , 'emp_roll no ' : 'E006', 'salary' : 85000}
            ]

dept_sal = {}
for i in employees:
    depart_no = i['dept_no']  
    salary = i['salary']   
    
    if depart_no not in dept_sal:
        dept_sal[depart_no] = []  
    
    dept_sal[depart_no].append(salary)

for dep,sal in dept_sal.items():
    print(f"Department {dep} , Min Salary : {min(sal)} , Max salary : {max(sal)}")

# Output : 
# Department 101 , Min Salary : 50000 , Max salary : 60000
# Department 102 , Min Salary : 45000 , Max salary : 70000
# Department 103 , Min Salary : 80000 , Max salary : 85000