# importing necessary libraries
import os, shutil

# specifying the input file path
path = r"Input file path here"  # The r specified indicates it's a RAW TEXT(String)
print(path)

# GOAL:- Check if folders exist if not create ==> check individual file extension and put file into appropriate folder
file_names = os.listdir(path)

# defining a list of folder names to check and create if they don't exist
folder_names = ["csv files", "text files", "images files", "audio files"]

# checking if each folder exists, creating it if it doesn't, and printing the appropriate messages
for loop in range(0, len(folder_names) - 1):
    if not os.path.exists(path + folder_names[loop]):
        os.makedirs(path + folder_names[loop])
        print(f'{folder_names[loop]} was just Created.')
        print('\n')
    else:
        print(f'{folder_names[loop]} Already Exist!')
        print('\n')
        
# getting the list of file names in the specified path
file_names = os.listdir(path)
        
# moving each file to the appropriate folder based on its file extension
for file in file_names:
    if ".csv" in file and not os.path.exists(path + "csv files/" + file):
        # shulil.move(FROM folder, TO folder)
        shutil.move(path + file, path + 'csv files/' + file)
        print(f"{file} was moved into csv files folder")
    elif ".txt" in file and not os.path.exists(path + "text files/" + file):
        shutil.move(path + file, path + 'text files/' + file)
        print(f"{file} was moved into text files folder")
    elif ".jpeg" in file and not os.path.exists(path + "images files/" + file):
        shutil.move(path + file, path + 'images files/' + file)
        print(f"{file} was moved into images files folder")
    else:
        print(f"The file {file} was not moved..")
        print('\n')