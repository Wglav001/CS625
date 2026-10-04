import matplotlib.pyplot as plt

plt.plot(age_summary["player_age"], age_summary["avg_woba"], marker="o")

plt.xlabel("Age")
plt.ylabel("Average wOBA")
plt.title("Average MLB Hitter wOBA by Age")

plt.show()