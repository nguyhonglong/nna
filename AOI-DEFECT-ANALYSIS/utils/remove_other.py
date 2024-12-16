import pandas as pd
import os

def remove_first_row_xlsx():
    # Path to the defect_data folder
    folder_path = 'defect_data'
    
    # Iterate through all files in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith('.xlsx'):
            file_path = os.path.join(folder_path, filename)
            
            # Read the Excel file
            df = pd.read_excel(file_path)
            
            # Remove the first row
            df = df.iloc[1:]
            
            # Save the file back without header
            df.to_excel(file_path, index=False, header=False)
            print(f"Processed: {filename}")

if __name__ == "__main__":
    remove_first_row_xlsx()
