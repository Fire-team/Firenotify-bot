import io
import matplotlib.pyplot as plt
from parsing import column_names, data


def visualize_incidents():
    # Clear previous plot to avoid overlapping
    plt.clf()

    # Count the number of incidents per category
    categories = {}
    for row in data:
        category = row[column_names.index("Rodzaj")]
        categories[category] = categories.get(category, 0) + 1

    # Sort the categories by the number of incidents
    sorted_categories = sorted(categories.items(), key=lambda x: x[1], reverse=True)

    # Create a bar chart
    x = range(len(sorted_categories))
    y = [c[1] for c in sorted_categories]
    labels = [c[0] for c in sorted_categories]
    plt.bar(x, y)
    plt.xticks(x, labels, rotation=90)
    plt.xlabel('Category')
    plt.ylabel('Number of Incidents')
    plt.title('Incidents by Category')

    # Save plot as bytes
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)

    return buffer
