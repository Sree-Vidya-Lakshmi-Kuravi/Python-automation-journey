# === Employee Payroll & Performance System ===
def employee():
    emp_id = int(input("Enter the employee ID:"))
    emp_name = input("Enter the employee name:")
    dept = input("Enter the employee dept:")
    salary = float(input("Enter the employee salary:"))
    exp = int(input("Enter the employee experience:"))
    performance = float(input("Enter the employee performance score:"))

    # Validations
    if emp_id < 0:
        print("Invalid employee ID")
        return

    if salary < 0:
        print("Invalid salary")
        return

    if performance < 0:
        print("Invalid performance score")
        return

    if exp < 0:
        print("Invalid experience")
        return

    # Calculating the performance category
    if performance < 0 or performance >100:
        print("Invalid performance score.")
        return
    elif 90 <= performance <= 100:
        perf_category = "Excellent"
    elif 80 <= performance <= 89:
        perf_category = "Very Good"
    elif 70 <= performance <= 79:
        perf_category = "Good"
    elif 60 <= performance <= 69:
        perf_category = "Average"
    elif performance < 60:
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

# employee()