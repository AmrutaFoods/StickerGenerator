#!/usr/bin/env python3
'''utility functions'''

import os
import shutil
from datetime import datetime

def get_current_date():
    ''' method provides current month and year '''
    # Get the current date
    current_date = datetime.now()

    # Extract the current month and year
    current_month = current_date.strftime("%B")
    current_year = current_date.year
    return current_month, current_year

def batch_number():
    '''Method to generate the batch number'''
    # Get the current month and year
    current_month = datetime.now().month
    current_year = datetime.now().year

    # Calculate the next year
    next_year = current_year + 1

    # Format the batch number
    batch_no = f"AF-{current_month:02d}/{current_year % 100:02d}-{next_year % 100:02d}"
    return batch_no

def folder_creation(directory):
    ''' method to check if there is already a directory
    if not create new and also clean up the old files inside directory'''

    # Check if the directory exists
    if os.path.exists(directory):
        print(f"The directory '{directory}' already exists.")

        # Check if the directory is not empty
        if os.listdir(directory):
            print(f"The directory '{directory}' is not empty. Removing its contents.")

            # Remove all files and subdirectories within the directory
            for item in os.listdir(directory):
                item_path = os.path.join(directory, item)
                if os.path.isfile(item_path):
                    os.remove(item_path)
                elif os.path.isdir(item_path):
                    shutil.rmtree(item_path)  # Use shutil.rmtree() to remove subdirectories recursively

            print("Contents removed successfully.")
        else:
            print(f"The directory '{directory}' is empty.")
    else:
        print(f"The directory '{directory}' does not exist. Creating it.")
        os.makedirs(directory)

    print("Process completed.")
