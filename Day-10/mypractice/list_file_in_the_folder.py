import os

folder_list = input("Please Provide list of folder names with spaces in between: ").split()

for folder in folder_list:
    try:
    
        files = os.listdir(folder)
    except FileNotFoundError:
        print("Please provide a valid folder name")
        break
    except PermissionError:
        print("No access to this folder:" + folder)
    
    print("=== listing files for the folder - " + folder)
    
    for file in files:
        print(file)