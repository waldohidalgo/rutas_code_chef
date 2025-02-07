import matplotlib.pyplot as plt

expenses = ['Rent', 'Food', 'Utilities', 'Entertainment']
amounts = [1200, 400, 200, 200]
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']
plt.pie(amounts, labels=expenses, autopct='%1.1f%%', startangle=90,colors=colors)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
plt.title('Sample Pie Chart')
plt.show()