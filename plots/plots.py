

import pandas as pd
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('files/cells.csv')
print(df)

# df has a 'time' column, 'cells' column

# 1. Scatter Plot
# Use When: You have two continuous variables and want to show the relationship between them.
# Example: Plotting time vs cells from a dataset.

# plt.xlabel('time')
# plt.ylabel('cells')
# plt.scatter(df.time, df.cells,color='red',marker='+')
# plt.show()

# 2. Line Plot
# Use When: You have data points ordered in time (or any other continuous variable), and you want to show trends or changes.
# Example: Plotting time vs cells.
# plt.plot(df['time'], df['cells'], color='blue', marker='o')
# plt.xlabel('Time')
# plt.ylabel('Cells')
# plt.title('Line Plot')
# plt.show()


# 3. Bar Plot
# Use When: You have categorical data and you want to compare quantities across categories.
# Example: Plotting sales in different categories.
# categories = ['A', 'B', 'C', 'D']
# values = [5, 7, 3, 4]
# plt.bar(categories, values, color='green')
# plt.xlabel('Category')
# plt.ylabel('Sales')
# plt.title('Bar Plot')
# plt.show()


# 4. Histogram
# Use When: You have continuous data and want to visualize the distribution (frequency) of the data.
# Example: Plotting the distribution of cells.
# plt.hist(df['cells'], bins=10, color='purple', edgecolor='black')
# plt.xlabel('Cells')
# plt.ylabel('Frequency')
# plt.title('Histogram')
# plt.show()

# 5. Box Plot
# Use When: You want to display the distribution of data based on a five-number summary (minimum, first quartile, median, third quartile, and maximum), and identify outliers.
# Example: Showing the distribution of cells.
# plt.boxplot(df['cells'], vert=False)
# plt.xlabel('Cells')
# plt.title('Box Plot')
# plt.show()

# 6. Pie Chart
# Use When: You want to show proportions of a whole.
# Example: Showing the percentage distribution of sales categories.

# sizes = [10, 20, 30, 40]
# labels = ['Category A', 'Category B', 'Category C', 'Category D']
# plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
# plt.title('Pie Chart')
# plt.show()


# 7. Heatmap
# Use When: You want to visualize matrix data (e.g., correlation matrix or any data with two dimensions).
# Example: Creating a heatmap from a correlation matrix.

# data = np.random.rand(10, 12)
# sns.heatmap(data, annot=True, cmap='coolwarm')
# plt.title('Heatmap')
# plt.show()


# 8. Violin Plot
sns.violinplot(x='time', y='cells', data=df)
plt.title('Violin Plot')
plt.show()


