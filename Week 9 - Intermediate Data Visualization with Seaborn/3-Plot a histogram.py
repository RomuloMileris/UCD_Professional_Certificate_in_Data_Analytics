# Create a distplot
sns.distplot(df['Award_Amount'],
             kde=False,
             bins=20)

# Display a plot
plt.show()