from parsing import data                        # Importing the data variable from the parsing module

def get_latest_emergency():
    latest_emergency = data[-1]                  # Get the last row of the data, which represents the latest emergency

    # Extract relevant information from the latest emergency
    date_reported = latest_emergency[0]          # Date Reported
    date_completed = latest_emergency[1] if latest_emergency[1] else "Ongoing"   # Date Completed (if available)
    county = latest_emergency[2]                 # County
    municipality = latest_emergency[3]           # Municipality
    location = latest_emergency[4]               # Location
    unit = latest_emergency[5]                   # Unit
    category = latest_emergency[6]               # Category
    subcategory = latest_emergency[7] if latest_emergency[7] else "-"  # Subcategory (if available)

    # Construct the modified string with the latest emergency data
    modified_string = f"Latest Emergency:\n" \
                     f"Date Reported: {date_reported}\n" \
                     f"Date Completed: {date_completed}\n" \
                     f"County: {county}\n" \
                     f"Municipality: {municipality}\n" \
                     f"Location: {location}\n" \
                     f"Unit: {unit}\n" \
                     f"Category: {category}\n" \
                     f"Subcategory: {subcategory}\n"

    return modified_string

