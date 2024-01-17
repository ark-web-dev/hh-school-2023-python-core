from datetime import datetime

def convert_string_to_date(date_string: str) -> datetime:
    if date_string is None or not isinstance(date_string, str):
        return
    
    return datetime.strptime(date_string, '%Y-%m-%d')
