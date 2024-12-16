import pandas as pd
import os
from pathlib import Path

def combine_excel_files():
    # Path to the defect_data folder
    folder_path = Path('defect_data')
    
    # List to store all dataframes
    all_dataframes = []
    
    # Iterate through all xlsx files in the folder
    for file in folder_path.glob('*.xlsx'):
        try:
            # Read each Excel file without headers
            df = pd.read_excel(file, engine='openpyxl', header=None)
            # Add a column to identify the source file (optional)
            df['Source_File'] = file.name
            # Append to our list
            all_dataframes.append(df)
        except Exception as e:
            print(f"Error reading {file.name}: {str(e)}")
            continue
    
    # Combine all dataframes
    if all_dataframes:
        combined_df = pd.concat(all_dataframes, ignore_index=True)
        
        # Save the combined data to a new Excel file
        output_path = folder_path / 'combined_defects.xlsx'
        combined_df.to_excel(output_path, index=False)
        print(f"Combined data saved to {output_path}")
    else:
        print("No Excel files found in the specified folder")

if __name__ == "__main__":
    combine_excel_files()
