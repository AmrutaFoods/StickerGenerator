#!/usr/bin/env python3
'''utility functions'''

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
