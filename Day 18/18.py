import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("employee.csv")
dept_salary = df.groupby("Department")["Salary"].mean()

dept_salary.plot(kind="bar")
plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")
#plt.show()
top5 = df.nlargest(5, "Salary")

top5.plot(x="Employee", y="Salary", kind="bar")
plt.title("Top 5 Highest-Paid Employees")
plt.show()