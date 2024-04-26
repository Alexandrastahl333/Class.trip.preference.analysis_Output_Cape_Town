import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

# Create a random 5x5 matrix
data = np.random.rand(5, 5)

# Generate row and column labels
row_labels = ['A', 'B', 'C', 'D', 'E']
column_labels = ['X', 'Y', 'Z', 'W', 'V']

# Create the heatmap
plt.figure(figsize=(8, 6))
heatmap = sns.heatmap(data, annot=True, cmap='viridis', xticklabels=column_labels, yticklabels=row_labels, fmt=".2f")

# Add plot details
plt.title("Example Heatmap with Random Data")  # Title
plt.show()  # Display the heatmap
