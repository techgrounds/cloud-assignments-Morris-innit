import csv
import os

user_dict = {
    "First name": input(f"What is your first name? "),
    "Last name": input(f"What is your last name? "),
    "Job title": input(f"What is your job title? "),
    "Company": input(f"What company do you work for? ")
}

# Check if the file exists
if os.path.exists('mycsvfile.csv'):
    print("The file 'mycsvfile.csv' already exists. Writing process cancelled.")
    exit()  # This stops the execution of the script if the file exists

with open('mycsvfile.csv','w') as f:
    w = csv.writer(f)
    w.writerows(user_dict.items())
    


