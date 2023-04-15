import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file
data = pd.read_csv('C:/Users/Az/Desktop/wiki article count/wiki_article_counts.csv')

# Set up the plot
plt.figure(figsize=(10, 8))
plt.title('Language Translation Ratio vs. Wiki Article Count')
plt.xlabel('article Count')
plt.ylabel('wiki')

# Plot the data
plt.scatter(data['article_count'], data['wiki'], alpha=0.5, s=10)

# Use a logarithmic scale for the x-axis
plt.xscale('log')

# Show the plot
plt.show()



