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
