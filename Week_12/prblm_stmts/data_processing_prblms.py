# === Employee Payroll & Performance System ===
def employee():
    emp_id = int(input("Enter the employee ID:"))
    emp_name = input("Enter the employee name:")
    dept = input("Enter the employee dept:")
    salary = float(input("Enter the employee salary:"))
    exp = int(input("Enter the employee experience:"))
    performance = float(input("Enter the employee performance score:"))

    # Validations
    if emp_id <= 0:
        print("Invalid employee ID")
        return

    if salary <= 0:
        print("Invalid salary")
        return

    if exp < 0:
        print("Invalid experience")
        return

    # Calculating the performance category
    if performance < 0 or performance > 100:
        print("Invalid performance score.")
        return
    elif performance >= 90:
        perf_category = "Excellent"
    elif performance >= 80:
        perf_category = "Very Good"
    elif performance >= 70:
        perf_category = "Good"
    elif performance >= 60:
        perf_category = "Average"
    else:
        perf_category = "Needs Improvement"

    # Calculate Bonus percentage
    if exp >= 5 and performance >= 80:
        bonus_percent = 15
    elif exp >= 3 and performance >= 70:
        bonus_percent = 10
    else:
        bonus_percent = 5

    # Calculate bonus
    bonus = salary * bonus_percent / 100

    # Final Salary
    final_salary = salary + bonus

    print("\n========== EMPLOYEE DETAILS ==========")
    print("ID:", emp_id)
    print("Name:", emp_name)
    print("Department:", dept)
    print("Experience:", exp)
    print("Performance:", performance)
    print("Performance Category:", perf_category)
    print("Salary:", salary)
    print("Bonus:", bonus)
    print("Final Salary:", final_salary)
    print("----------------------------")

    employee_data = {
        'id': emp_id,
        'name': emp_name,
        'dept': dept,
        'experience': exp,
        'performance': performance,
        'performance_category': perf_category,
        'salary': salary,
        'bonus_percent': bonus_percent,
        'bonus': bonus,
        'final_salary': final_salary
    }

    return employee_data

employees = []
num_of_emps = int(input("Enter the number of employees:"))

if num_of_emps <= 0:
    print("Number of employees must be greater than 0.")
    exit()

for e in range(num_of_emps):
    emp_data = employee()
    employees.append(emp_data)

total_sal = 0
total_bonus = 0

print("\n========== PAYROLL REPORT ==========")
for emp in employees:
    print("ID:", emp['id'])
    print("Name:", emp['name'])
    print("Department:", emp['dept'])
    print("Salary:", emp['salary'])
    print("Bonus:", emp['bonus'])
    print("Final Salary:", emp['final_salary'])

    total_sal += emp['salary']
    total_bonus += emp['bonus']

    print("-------------------------------------")

# Company payroll
total_payroll = total_sal + total_bonus
avg_salary = total_sal/len(employees)

print("========== COMPANY PAYROLL ==========")
print("Total Basic Salary:", total_sal)
print("Total Bonus:", total_bonus)
print("Total Payroll:", total_payroll)
print("Average Basic Salary:", avg_salary)

# Highest paid employee
high_paid = employees[0]

print("========== HIGHEST PAID EMPLOYEE ==========")
for emp in employees:
    if emp['final_salary'] > high_paid['final_salary']:
        high_paid = emp

print("Name:", high_paid['name'])
print("Department:", high_paid['dept'])
print("Final Salary:", high_paid['final_salary'])

# Highest performer employee
high_perf = employees[0]

print("========== HIGHEST PERFORMER ==========")
for emp in employees:
    if emp['performance'] > high_perf['performance']:
        high_perf = emp
print("Highest Performer:", high_perf['name'])

# Bonus Category Count
fifteen_percent_bonus = ten_percent_bonus = five_percent_bonus = 0
for e in employees:
    if e['bonus_percent'] == 15:
        fifteen_percent_bonus += 1
    elif e['bonus_percent'] == 10:
        ten_percent_bonus += 1
    else:
        five_percent_bonus += 1

print("========== BONUS CATEGORY SUMMARY ==========")
print("Count of Employees with 15% bonus:", fifteen_percent_bonus)
print("Count of Employees with 10% bonus:", ten_percent_bonus)
print("Count of Employees with 5% bonus:", five_percent_bonus)

# Performance Category Count
excellent = very_good = good = average = needs_improvement = 0
for e in employees:
    if e['performance_category'] == 'Excellent':
        excellent += 1
    elif e['performance_category'] == 'Very Good':
        very_good += 1
    elif e['performance_category'] == 'Good':
        good += 1   
    elif e['performance_category'] == 'Average':
        average += 1
    elif e['performance_category'] == 'Needs Improvement':
        needs_improvement += 1

print("========== PERFORMANCE CATEGORY COUNT ==========")
print("Count of Employees with 'Excellent' performance:", excellent)
print("Count of Employees with 'Very Good' performance:", very_good)
print("Count of Employees with 'Good' performance:", good)
print("Count of Employees with 'Average' performance:", average)
print("Count of Employees with 'Needs Improvement' performance:", needs_improvement)

# Department-wise Employee Count
dept_count = {}

for emp in employees:
    dept = emp['dept']
    if dept in dept_count:
        dept_count[dept] += 1
    else:
        dept_count[dept] = 1

print("========== DEPARTMENT-WISE EMPLOYEE COUNT ==========")
for dept, count in dept_count.items():
    print(dept, ":", count)

# Search Employee by ID
search_id = int(input("\nEnter employee ID to search: "))
found = False

for emp in employees:
    if emp['id'] == search_id:
        print("\n========== EMPLOYEE FOUND ==========")
        print("ID:", emp['id'])
        print("Name:", emp['name'])
        print("Department:", emp['dept'])
        print("Experience:", emp['experience'])
        print("Performance:", emp['performance'])
        print("Performance Category:", emp['performance_category'])
        print("Basic Salary:", emp['salary'])
        print("Bonus:", emp['bonus'])
        print("Final Salary:", emp['final_salary'])
        found = True
        break
if not found:
    print("\nEmployee with ID", search_id, "not found.")