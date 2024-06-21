from datetime import datetime, timedelta
import pytz
from tzlocal import get_localzone

# Function to get the local timezone dynamically
def get_local_timezone():
    # tzlocal.get_localzone() returns the local timezone
    return get_localzone()

# Function to convert UTC time to the local timezone
def convert_utc_to_local_timezone(utc_dt, local_timezone):
    # Define the UTC timezone
    utc_tz = pytz.utc
    
    # Convert the naive datetime to an aware datetime in UTC
    utc_aware_dt = utc_tz.localize(utc_dt)
    
    # Convert the UTC time to the local timezone
    local_tz_dt = utc_aware_dt.astimezone(local_timezone)
    
    return local_tz_dt

def time_ago(date):
    """Calculates the time difference in a human-readable format."""

    # Get the local timezone
    local_timezone = get_local_timezone()

    # Get the current time in the local timezone
    now = datetime.now(local_timezone)

    # Ensure the date is in the local timezone
    date = convert_utc_to_local_timezone(date, local_timezone)

    # Calculate the difference
    diff = now - date

    # Calculate the different components of the time difference
    seconds = diff.total_seconds()
    minutes = seconds // 60
    hours = minutes // 60
    days = diff.days
    weeks = days // 7
    months = days // 30
    years = days // 365

    # Determine the appropriate human-readable format based on the time difference
    if seconds < 60:
        return f"{int(seconds)} seconds ago"
    elif minutes < 60:
        return f"{int(minutes)} minutes ago"
    elif hours < 24:
        return f"{int(hours)} hours ago"
    elif days < 7:
        return f"{days} days ago"
    elif weeks < 4:
        return f"{weeks} weeks ago"
    elif months < 12:
        return f"{months} months ago"
    else:
        return f"{years} years ago"

# Example usage
if __name__ == "__main__":
    # Define a UTC datetime (naive)
    utc_dt = datetime.utcnow()
    
    # Example: convert and calculate time ago
    print(time_ago(utc_dt))
