import shutil
import os
import datetime

# Define the source and destination folders
source = r'C:/Users/ThinkPad/Desktop/AWS/Projects/Pratice'
destination = r'C:\Users\ThinkPad\Desktop\AWS\Projects\Pratice\backups'

def backup_files(source,destination):
    # Get the current date
    today = datetime.date.today()
    backup_files_name = os.path.join(destination, f"backup_{today}.zip")
    shutil.make_archive(backup_files_name.replace('.zip', ''),'zip', source)

backup_files(source,destination)