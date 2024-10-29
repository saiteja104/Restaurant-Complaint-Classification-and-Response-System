
import pandas as pd
import pickle

# Load the DataFrame
df = pd.read_csv("Final_AB_Complaint_Classification_Restaurant.csv")

# # Updated get_complaint_info function
# def get_complaint_info(df, days):
#     # Filter the DataFrame to get rows where Review_Days is less than or equal to the specified days
#     filtered_df = df[df['Review_Days'] <= days]

#     # Define the category columns explicitly
#     category_columns = [
#         'Service Issue',
#         'Food Options',
#         'Food Quality',
#         'Atmosphere',
#         'Value for Money',
#         'Hygiene',
#         'Others'
#     ]

#     # Count occurrences for each specified category
#     category_counts = filtered_df[category_columns].sum()  # Use the list of column names

#     # Create a dictionary to hold the categories and their counts
#     complaint_info = {
#         'categories': category_counts.index.tolist(),
#         'counts': category_counts.values.tolist(),
#         'total_complaints': filtered_df.shape[0],  # Count of total complaints
#         'reviews': filtered_df[['Review', 'Category', 'Severity', 'Urgency', 'Is_Repeated']]
#     }
    
#     # Order the reviews by severity (assuming severity is categorical: 'High', 'Medium', 'Low')
#     severity_order = {'High': 1, 'Medium': 2, 'Low': 3}
#     complaint_info['reviews']['Severity'] = complaint_info['reviews']['Severity'].map(severity_order)
#     complaint_info['reviews'] = complaint_info['reviews'].sort_values(by='Severity')
    
#     return complaint_info

# # Create a dictionary to hold the function
# functions_dict = {
#     'get_complaint_info': get_complaint_info
# }

# # Save the dictionary to a pickle file
# with open('complaint_functions1.pkl', 'wb') as f:
#     pickle.dump(functions_dict, f)

# print("Pickle file created successfully.")
import pandas as pd
import pickle

# Define the function to get complaint information
def get_complaint_info(df, days):
    # Filter the DataFrame to get rows where Review_Days is less than or equal to the specified days
    filtered_df = df[df['Review_Days'] <= days]

    # Define the category columns explicitly
    category_columns = [
        'Service Issue',
        'Food Options',
        'Food Quality',
        'Atmosphere',
        'Value for Money',
        'Hygiene',
        'Others'
    ]

    # Count occurrences for each specified category
    category_counts = filtered_df[category_columns].sum()  # Use the list of column names

    # Create a dictionary to hold the categories and their counts
    complaint_info = {
        'categories': ', '.join(category_counts.index[category_counts > 0].tolist()),  # Join non-zero categories into a string
        'counts': ', '.join(map(str, category_counts[category_counts > 0].values.tolist())),  # Join counts into a string
        'total_complaints': filtered_df.shape[0],  # Count of total complaints
        'reviews': filtered_df[['Review', 'Category', 'Severity', 'Urgency', 'Is_Repeated']]
    }

    # Convert categories to strings
    complaint_info['reviews']['Category'] = complaint_info['reviews']['Category'].astype(str)

    # No need to convert Severity to numerical values; keep them as strings
    complaint_info['reviews'] = complaint_info['reviews'].sort_values(by='Severity')
    
    return complaint_info

# Create a dictionary to hold the function
functions_dict = {
    'get_complaint_info': get_complaint_info
}

# Save the dictionary to a pickle file
try:
    with open('complaint_functions3.pkl', 'wb') as f:
        pickle.dump(functions_dict, f)
    print("Pickle file created successfully.")
except Exception as e:
    print(f"An error occurred while saving the pickle file: {e}")
