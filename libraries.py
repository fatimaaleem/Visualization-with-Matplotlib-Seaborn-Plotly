print("Data visualization is crucial in data analysis and communication because it allows us to quickly understand patterns, trends, and outliers that might be hidden within raw data. Visual representations make complex information more accessible and help in conveying insights effectively to various audiences.")
print("\nMatplotlib is a foundational plotting library in Python. Its strength lies in its flexibility and fine-grained control over every element of a plot, making it suitable for creating highly customized visualizations. However, this flexibility often comes at the cost of verbosity, especially when creating complex plots.")
print("\nSeaborn is a library built on top of Matplotlib. It simplifies the creation of aesthetically pleasing and statistically informative graphics. Its strength is its ease of use for common statistical plots, providing built-in themes and color palettes that produce visually appealing results with less code compared to Matplotlib.")
print("\nPlotly is a library for creating interactive and web-based visualizations. Its key strengths are its interactivity, allowing users to hover, zoom, and pan, and its ability to generate standalone HTML files that can be easily shared. While powerful, Plotly might have a slightly steeper learning curve for some users compared to static libraries like Matplotlib and Seaborn.")
import matplotlib.pyplot as plt
import numpy as np

# Step 1 & 2: Explain Figure, Axes, and plotting functions
print("Matplotlib's core building blocks are the Figure and Axes.")
print("A Figure is the overall window or page on which everything is drawn. Think of it as the canvas.")
print("An Axes is the area within the Figure where the data is plotted. A Figure can contain multiple Axes.")
print("Plotting functions like plot(), scatter(), bar(), and hist() are typically methods of the Axes object. They draw data onto that specific Axes.")

# Step 3: Simple line plot with customization
print("\n--- Line Plot Example ---")
fig1, ax1 = plt.subplots()
x = np.linspace(0, 10, 100)
y = np.sin(x)
ax1.plot(x, y, label='sin(x)', color='blue', linestyle='--')
ax1.set_title('Simple Line Plot')
ax1.set_xlabel('x-axis')
ax1.set_ylabel('y-axis')
ax1.legend()
plt.show(block=True)  # Ensures plot window stays open in VS Code

# Step 4: Simple scatter plot with customization
print("\n--- Scatter Plot Example ---")
fig2, ax2 = plt.subplots()
x_scatter = np.random.rand(50)
y_scatter = np.random.rand(50)
ax2.scatter(x_scatter, y_scatter, marker='o', color='red', alpha=0.7)
ax2.set_title('Simple Scatter Plot')
ax2.set_xlabel('Random X')
ax2.set_ylabel('Random Y')
plt.show(block=True)

# Step 5: Simple bar plot with customization
print("\n--- Bar Plot Example ---")
fig3, ax3 = plt.subplots()
categories = ['A', 'B', 'C', 'D']
values = [25, 50, 30, 45]
bars = ax3.bar(categories, values, color=['purple', 'orange', 'green', 'brown'])
ax3.set_title('Simple Bar Plot')
ax3.set_xlabel('Category')
ax3.set_ylabel('Value')
plt.show(block=True)

# Step 6: Simple histogram with customization
print("\n--- Histogram Example ---")
fig4, ax4 = plt.subplots()
data_hist = np.random.randn(200)
ax4.hist(data_hist, bins=20, color='skyblue', edgecolor='black', alpha=0.7)
ax4.set_title('Simple Histogram')
ax4.set_xlabel('Value')
ax4.set_ylabel('Frequency')
plt.show(block=True)
import seaborn as sns
import matplotlib.pyplot as plt # Import matplotlib for displaying plots

# 1. Explain how Seaborn extends Matplotlib and its focus on statistical plotting.
print("Seaborn is a Python data visualization library based on matplotlib. It provides a high-level interface for drawing attractive and informative statistical graphics. While Matplotlib provides the fundamental building blocks (Figures, Axes), Seaborn offers refined aesthetics and functions specifically designed for common statistical plotting tasks, making it easier to create complex visualizations like heatmaps, time series plots, and multi-variate distributions with less code.")
print("Seaborn is particularly good at handling pandas DataFrames and automatically maps data columns to visual attributes, simplifying the process of creating informative plots from structured data.")

# 2. Discuss the key categories of plots Seaborn provides.
print("\nSeaborn organizes its plotting functions into several categories:")
print("- **Distribution plots:** Show the distribution of a single variable or the relationship between two variables and their distributions (e.g., histplot, kdeplot, displot, rugplot, jointplot).")
print("- **Relationship plots:** Show the relationship between two or more variables (e.g., scatterplot, lineplot, relplot, regplot).")
print("- **Categorical plots:** Show the relationship between a numerical variable and one or more categorical variables (e.g., boxplot, violinplot, stripplot, swarmplot, barplot, countplot, pointplot, catplot).")
print("- **Regression plots:** Plot data and a linear regression model fit (e.g., regplot, lmplot).")
print("- **Matrix plots:** Plot data as a matrix (e.g., heatmap, clustermap).")
print("- **Multi-plot grids:** Draw plots onto a FacetGrid or PairGrid (e.g., FacetGrid, PairGrid).")

# 3. Import the seaborn library (already done above)
# import seaborn as sns - This was done at the beginning of the code block.# 4. Load one of Seaborn's built-in datasets
tips = sns.load_dataset('tips')
print("\n--- First 5 rows of the 'tips' dataset ---")
print(tips.head())

# 5. Create a distribution plot (e.g., histplot)
print("\n--- Distribution Plot (Histogram of Total Bill) ---")
sns.histplot(data=tips, x='total_bill', kde=True)
plt.title('Distribution of Total Bill')
plt.xlabel('Total Bill ($)')
plt.ylabel('Frequency')
plt.show()

# 6. Create a scatter plot with a regression line (regplot)
print("\n--- Scatter Plot with Regression Line (Total Bill vs. Tip) ---")
sns.regplot(data=tips, x='total_bill', y='tip')
plt.title('Total Bill vs. Tip with Regression Line')
plt.xlabel('Total Bill ($)')
plt.ylabel('Tip ($)')
plt.show()

# 7. Create a box plot (boxplot)
print("\n--- Box Plot (Total Bill by Day) ---")
sns.boxplot(data=tips, x='day', y='total_bill')
plt.title('Total Bill by Day')
plt.xlabel('Day of the Week')
plt.ylabel('Total Bill ($)')
plt.show()

# 8. Create a violin plot (violinplot)
print("\n--- Violin Plot (Tip by Time) ---")
sns.violinplot(data=tips, x='time', y='tip')
plt.title('Tip by Time of Day')
plt.xlabel('Time of Day')
plt.ylabel('Tip ($)')
plt.show()
# 1. Print an explanation of Plotly's strengths and structure.
print("Plotly is a powerful interactive graphing library that excels in creating web-based visualizations. Its key strength lies in its built-in interactivity, allowing users to zoom, pan, hover, and select data points directly within the plot without needing additional code for these interactions.")
print("\nPlotly's focus on web-based visualizations means that plots can be easily exported as standalone HTML files or integrated into web applications and dashboards, making them highly shareable and accessible.")
print("\nPlotly's structure is based on JSON-like figure dictionaries or using the `graph_objects` module, which represents figures and their components as Python objects. The high-level `plotly.express` module simplifies creating complex plots with minimal code.")
print("\nInteractivity in Plotly is primarily handled by JavaScript libraries (like Plotly.js) running in the web browser. When you create a plot in Python, Plotly generates a JSON representation of the figure, which is then interpreted by the JavaScript library to render the interactive plot in a web environment.")
# 2. Import the plotly.express module.
import plotly.express as px

# 3. Create an interactive scatter plot using plotly.express.
# Use the tips DataFrame, mapping 'total_bill' to x, 'tip' to y, color by 'sex', and include tooltips.
fig_scatter = px.scatter(tips,
                         x='total_bill',
                         y='tip',
                         color='sex', # Add color mapping by 'sex'
                         hover_data=['size', 'day', 'time', 'smoker'], # Add tooltips for relevant columns
                         title='Total Bill vs. Tip by Sex') # Add a title

# Display the plot.
fig_scatter.show()# 4. Create an interactive bar chart using plotly.express.
# Use the tips DataFrame, grouping by 'day' and showing the average 'total_bill'.
# Plotly Express automatically handles aggregation for bar charts if y is numerical and x is categorical.
fig_bar = px.bar(tips,
                 x='day',
                 y='total_bill',
                 title='Average Total Bill by Day', # Add a title
                 labels={'total_bill': 'Average Total Bill ($)', 'day': 'Day of the Week'}) # Add axis labels

# Display the plot.
fig_bar.show()
import pandas as pd

# 5. Create an interactive line plot using plotly.express.
# For simplicity, we'll sort by day and plot a cumulative sum to show a trend-like visualization.
# First, ensure the 'day' column has a defined order for plotting.
day_order = ['Thur', 'Fri', 'Sat', 'Sun']
tips['day_ordered'] = pd.Categorical(tips['day'], categories=day_order, ordered=True)
tips_sorted = tips.sort_values('day_ordered')

# Calculate cumulative sum of total_bill over the sorted days
tips_sorted['cumulative_total_bill'] = tips_sorted['total_bill'].cumsum()

fig_line = px.line(tips_sorted,
                   x=tips_sorted.index, # Use index as a sequential x-axis proxy
                   y='cumulative_total_bill',
                   color='day', # Color by day to show progression
                   title='Cumulative Total Bill Over Time (Ordered by Day)',
                   labels={'index': 'Order of Entry (Sorted by Day)', 'cumulative_total_bill': 'Cumulative Total Bill ($)'})

# Display the plot.
fig_line.show()
print("--- Comparison of Matplotlib, Seaborn, and Plotly ---")
print("\n**1. Level of Abstraction:**")
print("- Matplotlib: Low-level. Provides fine-grained control over plot elements but requires more code for complex plots.")
print("- Seaborn: High-level. Built on Matplotlib, simplifies creating aesthetically pleasing and statistically informative plots.")
print("- Plotly: High-level. Offers a high-level API (Plotly Express) for quick plotting and a lower-level API (graph_objects) for detailed customization. Focuses on interactive plots.")

print("\n**2. Focus:**")
print("- Matplotlib: General-purpose plotting library for creating a wide variety of static plots.")
print("- Seaborn: Primarily focused on statistical data visualization, providing functions for exploring relationships and distributions.")
print("- Plotly: Focused on creating interactive, web-based visualizations that can be embedded in dashboards or exported as HTML.")

print("\n**3. Ease of Use for Common Tasks:**")
print("- Matplotlib: Can be verbose for common tasks like adding labels or legends, especially for complex layouts.")
print("- Seaborn: Generally easier than Matplotlib for creating standard statistical plots with good default aesthetics.")
print("- Plotly: Plotly Express is very easy for creating many standard interactive plots. Graph_objects requires more code but offers full control.")

print("\n**4. Customization Capabilities:**")
print("- Matplotlib: Highly customizable at a granular level. Allows control over almost every visual aspect.")
print("- Seaborn: Provides good customization options, often through parameters in its functions or by accessing the underlying Matplotlib objects.")
print("- Plotly: Offers extensive customization through its figure dictionaries or graph objects API, allowing control over layout, annotations, hover information, etc.")

print("\n**5. Output Format:**")
print("- Matplotlib: Primarily generates static images (PNG, JPG, PDF, SVG) and can be used in interactive environments.")
print("- Seaborn: Also primarily generates static images, leveraging Matplotlib's output capabilities.")
print("- Plotly: Generates interactive plots that can be displayed inline in notebooks, saved as HTML files, or used in web applications.")

print("\n--- Guidance on When to Use Each Library ---")
print("\n**Use Matplotlib when:**")
print("- You need complete, fine-grained control over every aspect of your plot.")
print("- You are creating simple, basic plots where the overhead of other libraries is not necessary.")
print("- You are building custom plot types or need to integrate tightly with other libraries that expect Matplotlib objects.")
print("- Your primary output is static images and you don't require interactivity.")

print("\n**Use Seaborn when:**")
print("- You are focused on creating statistical visualizations (e.g., distributions, relationships, categorical comparisons).")
print("- You want to quickly generate aesthetically pleasing plots with good default styles.")
print("- You are working with pandas DataFrames and want easy mapping of data columns to visual attributes.")
print("- You need common statistical plots like box plots, violin plots, heatmaps, or regression plots with minimal code.")

print("\n**Use Plotly when:**")
print("- You need interactive visualizations (zooming, panning, hovering) for data exploration or presentation.")
print("- Your target audience or sharing method requires web-based plots (e.g., dashboards, websites, standalone HTML).")
print("- You want to create plots that can be easily embedded or shared without requiring users to run Python code.")
print("- You are working with large datasets where interactivity can help in exploring specific data points.")