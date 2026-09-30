import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr"]
sales = [120, 150, 180, 140]

plt.figure(figsize=(8, 5))

plt.plot(months, sales, marker="o", label="Sales")

plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.xticks(rotation=45)
plt.yticks([100, 120, 140, 160, 180, 200])

plt.legend()
plt.grid(axis="y")

plt.tight_layout()

plt.savefig("monthly_sales.png", dpi=300, bbox_inches="tight")

plt.show()