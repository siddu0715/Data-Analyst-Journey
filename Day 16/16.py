import matplotlib.pyplot as plt

departments = ["IT", "HR", "Sales", "Finance"]
salary = [67500, 47500, 52500, 58000]

plt.bar(departments, salary)
plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")
#plt.show()
import pandas as pd
df=pd.read_csv("Employee.csv")
df.groupby("Department")["Salary"].mean().plot(kind="bar")
#plt.title("Average Salary by Department")
#plt.show()
df.groupby("Department").count().plot(kind="bar")
#plt.title("Number of Employees by Department")
#plt.show()
df.groupby("ExperienceInCurrentDomain")["Salary"].plot(kind="bar")
plt.title("Salary by Experience in Current Domain")
plt.show()