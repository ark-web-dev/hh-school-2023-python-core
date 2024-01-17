from datetime import datetime

def convert_string_to_date(date_string):
    return datetime.strptime(date_string, '%Y-%m-%d')
