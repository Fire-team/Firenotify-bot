import io                                      # Importing the io module
import matplotlib.pyplot as plt                # Importing the matplotlib.pyplot module
from parsing import column_names, data          # Importing the column_names and data variables from the parsing module

def visualize_incidents():                      # Defining a function called 'visualize_incidents'
    # Clear previous plot to avoid overlapping
    plt.clf()                                   # Clearing the previous plot to avoid overlapping

    # Count the number of incidents per category
    categories = {}                             # Initializing an empty dictionary called 'categories'
    for row in data:                            # Looping over each row in the 'data' variable
        category = row[column_names.index("Rodzaj")]  # Extracting the category from the 'column_names' variable
        categories[category] = categories.get(category, 0) + 1  # Updating the category count in the 'categories' dictionary

    # Sort the categories by the number of incidents
    sorted_categories = sorted(categories.items(), key=lambda x: x[1], reverse=True)   # Sorting the 'categories' dictionary by the count of incidents in each category

    # Create a bar chart
    x = range(len(sorted_categories))           # Creating a range object with the length of the sorted_categories
    y = [c[1] for c in sorted_categories]       # Creating a list of the values in the sorted_categories dictionary
    labels = [c[0] for c in sorted_categories]  # Creating a list of the keys in the sorted_categories dictionary
    plt.bar(x, y)                               # Creating a bar chart with the x and y values
    plt.xticks(x, labels, rotation=0)          # Setting the x-axis labels and rotating them by 90 degrees
    plt.xlabel('Category')                      # Setting the x-axis label to 'Category'
    plt.ylabel('Number of Incidents')           # Setting the y-axis label to 'Number of Incidents'
    plt.title('Incidents by Category')          # Setting the title of the chart to 'Incidents by Category'

    # Save plot as bytes
    buffer = io.BytesIO()                       # Creating a buffer object using the io module
    plt.savefig(buffer, format='png')           # Saving the plot in png format to the buffer object
    buffer.seek(0)                              # Setting the position of the buffer object to the beginning

    return buffer                                # Returning the buffer object