def avg_employee_sal(salaries):
    return sum(salaries) / len(salaries)

salaries = [1000, 2000, 3000, 4000, 5000]
print(avg_employee_sal(salaries))