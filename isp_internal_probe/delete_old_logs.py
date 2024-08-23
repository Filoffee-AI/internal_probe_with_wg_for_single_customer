import os
import datetime

# Specify the directory path where you want to delete old files
directory_path = '/home/isp_internal_probe/logs'

# Specify the age limit in days (in this case, 3 days)
age_limit = 2

# Get the current date and time
current_time = datetime.datetime.now()

# Iterate through the files in the directory
for filename in os.listdir(directory_path):
    file_path = os.path.join(directory_path, filename)
    
    # Check if the file is a regular file (not a directory) and it's old enough
    if os.path.isfile(file_path):
        file_stat = os.stat(file_path)
        file_mtime = datetime.datetime.fromtimestamp(file_stat.st_mtime)
        delta = current_time - file_mtime
        
        if delta.days >= age_limit:
            # Delete the file
            os.remove(file_path)
            print(f"Deleted {filename} (age: {delta.days} days)")
