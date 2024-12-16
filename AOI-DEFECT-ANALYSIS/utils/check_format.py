import os
import pandas as pd

def process_xls_files(folder_path):
    # Check if folder exists
    if not os.path.exists(folder_path):
        print(f"Folder {folder_path} does not exist!")
        return
    
    # Get all xls files in the folder
    xls_files = [f for f in os.listdir(folder_path) if f.lower().endswith('.xls')]
    
    for file in xls_files:
        file_path = os.path.join(folder_path, file)
        try:
            # Read the Excel file with engine specification
            df = pd.read_excel(file_path, engine='xlrd')
            
            # Check if A8 (row 7, column 0) contains "Model Name"
            if len(df) >= 8 and str(df.iloc[6, 0]).strip() == "Model Name":
                # Remove first 8 rows
                df = df.iloc[8:].reset_index(drop=True)
                
                # Save as xlsx instead of xls
                new_file_path = file_path.replace('.xls', '.xlsx')
                df.to_excel(new_file_path, index=False)
                
                # Remove the old xls file
                os.remove(file_path)
                print(f"Processed {file}: Removed first 8 rows and converted to xlsx")
            else:
                print(f"Skipped {file}: A8 is not 'Model Name'")
                
        except Exception as e:
            print(f"Error processing {file}: {str(e)}")

# Process files in defect_data folder
defect_data_folder = "defect_data"
process_xls_files(defect_data_folder)
