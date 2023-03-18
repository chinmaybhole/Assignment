import csv
import math
import matplotlib.pyplot as plt

# Open the CSV file and read the data
with open('marks.csv', 'r') as file:
    reader = csv.DictReader(file)
    marks = []
    for row in reader:
        marks.append(float(row['Mark']))

# Calculate the mean, variance, and standard deviation
mean = sum(marks) / len(marks)
variance = sum((x - mean) ** 2 for x in marks) / len(marks)
std_dev = math.sqrt(variance)

# Plot a histogram of the marks with the mean and standard deviation marked on it
plt.hist(marks, bins=10)
plt.axvline(mean, color='red', linestyle='dashed', linewidth=2)
plt.axvline(mean + std_dev, color='green', linestyle='dashed', linewidth=2)
plt.axvline(mean - std_dev, color='green', linestyle='dashed', linewidth=2)
plt.xlabel('Mark')
plt.ylabel('Frequency')
plt.title('Distribution of Marks')
plt.savefig('marks_distribution.png')

# Show the plot
plt.show()
