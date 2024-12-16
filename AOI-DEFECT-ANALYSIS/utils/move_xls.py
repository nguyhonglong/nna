import os
import shutil

def move_xls_files(source_dir, target_dir):
    # Create target directory if it doesn't exist
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    
    # Walk through all directories and subdirectories
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            # Check if file is an Excel file
            if file.lower().endswith('.xls'):
                source_path = os.path.join(root, file)
                target_path = os.path.join(target_dir, file)
                
                # Handle duplicate filenames
                counter = 1
                base_name = os.path.splitext(file)[0]
                extension = os.path.splitext(file)[1]
                while os.path.exists(target_path):
                    new_name = f"{base_name}_{counter}{extension}"
                    target_path = os.path.join(target_dir, new_name)
                    counter += 1
                
                # Move the file
                try:
                    shutil.move(source_path, target_path)
                    print(f"Moved: {source_path} -> {target_path}")
                except Exception as e:
                    print(f"Error moving {source_path}: {str(e)}")

source_directory = "."
target_directory = "defect_data"
move_xls_files(source_directory, target_directory)