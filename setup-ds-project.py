# Start Date: 30th January 2024
# Python Developer: Sulaiha Subi
# Objective: 

    # To setup Data Science Project Directory - 
    # This structure follows common best practices for Data Science projects, promoting organization and clarity, especially in collaborative environments.

# Instructions:

    # Please read README.md file to better understands the workflow
    # Copy this script into your Python environment and run it. 
    # It should create the necessary directories and files in the specified base path, given that you have the necessary permissions.

    # Make sure you run your script in an environment where you have the required permissions, or run your script as an administrator if you're on Windows. 
    # If you encounter any more issues, the error messages printed by the script should give you more insight into what's going wrong.

########################################################################### setup-ds--project START ###########################################################################

# Import libraries
import os

# Define the base path for your Data Science project
# Use & copy this directory: C:\Users\hayat\HAYAT TECHNOLOGIES SDN BHD\Data Science - General\[2024] Data Science Projects\D. DS Projects\{your-project-file}
# Make sure to create the folder under "D. DS Projects" as this is the base path
base_path = r"C:\Users\hayat\HAYAT TECHNOLOGIES SDN BHD\Data Science - General\[2024] Data Science Projects\B. Guidelines to start the Projects"

# List of folders to be created under the base path
folders = [
    "data", # To store the data transformation & preprocessing
    "data/processed", # The final, canonical data sets for modeling
    "data/raw", # The original, immutable data dump
    "data/external", # Data from third party sources.
    "data/transformed", # Intermediate data that has been transformed
    "docs", # A documentations file - may refer 
    "models", # Trained and serialized models, model predictions, or model summaries
    "notebooks", # Jupyter notebooks. Naming convention is a number (for ordering),the creator's initials, and a short `-` delimited description, e.g. `1.0-jqp-initial-data-exploration`
    "references", # Data dictionaries, documentations, manuals, and all other explanatory materials
    "reports", # Generated analysis as HTML, PDF, LaTeX, PowerBI report etc.
    "reports/figures", #  Generated graphics and figures to be used in reporting
    "src", # Source code for use in this project
    "src/data", # Scripts to download or generate data
    "src/features", # Scripts to turn raw data into features for modeling
    "src/models", # Scripts to train models and then use trained models to make predictions
    "src/visualization", # Scripts to create exploratory and results oriented visualizations
]

# Create folders
for folder in folders:
    folder_path = os.path.join(base_path, folder)
    try:
        os.makedirs(folder_path, exist_ok=True)
        with open(os.path.join(folder_path, ".gitkeep"), "w") as f:
            pass
    except Exception as e:
        print(f"Error creating folder {folder_path}: {e}") # error handling to shows you the error if fail to create the folders

# List of files to be created under the base path
files = [
    "src/__init__.py", # Makes src a Python module
    "src/data/make_dataset.py", # Scripts to download or generate data
    "src/features/build_features.py", # Scripts to turn raw data into features for modeling
    "src/models/train_model.py", # Scripts to train model
    "src/models/predict_model.py", # Scripts to trained models to make predictions
    "src/visualization/visualize.py", # Scripts to create exploratory and results oriented visualizations
    "requirements.txt" # The requirements file for reproducing the analysis environment, e.g. generated with `pip freeze > requirements.txt`
]

# Create files
for file in files:
    file_path = os.path.join(base_path, file)
    try:
        # Ensure the directory exists before creating a file
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w") as f:
            pass
    except Exception as e:
        print(f"Error creating file {file_path}: {e}") # error handling to shows you the error if fail to create the folders
