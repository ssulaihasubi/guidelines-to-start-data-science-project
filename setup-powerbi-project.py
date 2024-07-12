# Start Date: 30th January 2024
# Python Developer: Sulaiha Subi
# Objective: 
    # To set up Power BI Dashboard Project structure
    # This structure follows common best practices for Power BI projects, promoting organization and clarity, especially in collaborative environments.

# Instructions:
    # Please read README.md file to better understand the workflow
    # Copy this script into your Python environment and run it. 
    # It should create the necessary directories and files in the specified base path, given that you have the necessary permissions.
    # Make sure you run your script in an environment where you have the required permissions, or run your script as an administrator if you're on Windows. 
    # If you encounter any more issues, the error messages printed by the script should give you more insight into what's going wrong.

########################################################################### setup-powerbi-project START ###########################################################################

# Import libraries
import os

# Define the base path for your Power BI Dashboard project
# Use & copy this directory:C:\Users\hayat\HAYAT TECHNOLOGIES SDN BHD\Data Science - General\[2024] Data Science Projects\E. PowerBi-Dashboard-Projects
# Make sure to create a folder of the powerbi project, as this is the base path
base_path = r"C:\Users\hayat\HAYAT TECHNOLOGIES SDN BHD\Data Science - General\[2024] Data Science Projects\E. PowerBi-Dashboard-Projects\test"

# List of folders to be created under the base path
folders = [
    "data_sources/raw_data",
    "data_sources/processed_data",
    "data_models",
    "reports",
    "documentation",
    "assets/images",
    "assets/themes",
    "changelog"
]

print(f"Creating folder structure at: {base_path}\n")

# Create folders and print the structure
for folder in folders:
    folder_path = os.path.join(base_path, folder)
    try:
        os.makedirs(folder_path, exist_ok=True)
        print(f"Created: {folder_path}")
        # Create .gitkeep file to keep the folder in git even if it's empty
        with open(os.path.join(folder_path, ".gitkeep"), "w") as f:
            pass
    except Exception as e:
        print(f"Error creating folder {folder_path}: {e}")

print("\nFolder structure creation complete.")

########################################################################### setup-powerbi-project END ###########################################################################
