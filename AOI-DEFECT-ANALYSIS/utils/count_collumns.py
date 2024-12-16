import pandas as pd
import os

# Specify the folder path
folder_path = 'defect_data'

# Iterate through all xlsx files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.xlsx'):
        # Create full file path
        file_path = os.path.join(folder_path, filename)
        
        try:
            # Read the Excel file
            df = pd.read_excel(file_path)
            
            # Get number of columns
            num_columns = len(df.columns)
            
            # Print results
            print(f"File: {filename} - Number of columns: {num_columns}")
            
        except Exception as e:
            print(f"Error reading {filename}: {str(e)}")
