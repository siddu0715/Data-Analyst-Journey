import pandas as pd
df=pd.read_csv("Employee.csv")
#print(df)
avg_salary = df.groupby('Department')['Salary'].mean().reset_index()
dept_more_than_one = df.groupby('Department').size().reset_index(name='Employee_Count')
dept_more_than_one = dept_more_than_one[dept_more_than_one['Employee_Count'] > 1]
highest_salary = df.groupby('Department')['Salary'].max().reset_index()
total_salary = df.groupby('Department')['Salary'].sum().reset_index()
employees_by_city = df.groupby('City').size().reset_index(name='Employee_Count')
top3_salaries = df.nlargest(3, 'Salary')[['Department','Salary']]
bottom3_salaries = df.nsmallest(3, 'Salary')[['Department','Salary']]
print(
    "Average Salary by Department:\n", avg_salary,
    "\n\nDepartments with >1 Employee:\n", dept_more_than_one,
    "\n\nHighest Salary in Each Department:\n", highest_salary,
    "\n\nTotal Salary by Department:\n", total_salary,
    "\n\nEmployees by City:\n", employees_by_city,
    "\n\nTop 3 Salaries:\n", top3_salaries,
    "\n\nBottom 3 Salaries:\n", bottom3_salaries
)
