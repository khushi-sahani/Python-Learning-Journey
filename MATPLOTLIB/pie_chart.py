import matplotlib.pyplot as plt

subjects = ["Python", "Pandas", "OOP"]
hours = [5, 3, 2]

plt.pie(
    hours,
    labels=subjects,
    autopct="%1.1f%%"
)

plt.title("Study Time Distribution")

plt.show()