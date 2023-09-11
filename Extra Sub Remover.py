import os
import threading



def operate_files(directory,file_type,old_name,new_name):
    if not os.path.exists(directory):
        print(f"Directory '{directory}' does not exist.")
        return

    files = os.listdir(directory)

    target_files = [f for f in files if f.endswith(file_type)]

    if not target_files:
        print(f"No {file_type} files found in the directory.")
        return

    for target_file in target_files:
        file_path = os.path.join(directory, target_file)

        file = open(file_path, 'r', encoding='utf-8')
        if old_name in file.name:
            old_file_name = file.name
            new_file_name = file.name.replace(old_name, new_name)
            file.close()
            os.rename(old_file_name, new_file_name)
        else:
            file.close()
            os.remove(file.name)


def explore_subdirectories(parent_directory,file_type,old_name,new_name):
    operate_files(parent_directory,file_type,old_name,new_name)

    child_directories = os.listdir(parent_directory)

    for child in child_directories:
        item_path = os.path.join(parent_directory, child)
        if os.path.isdir(item_path):
            print("Subdirectory:", item_path)
            threading.Thread(explore_subdirectories(item_path,file_type,old_name,new_name)).start()


if __name__ == "__main__":
    print('\n-------Read Instruction in README.md The Changes Cannot be Reversed-------\n')
    file_type =input('Enter The Extension Of Files to remove (with exclusion to files of this type having a particular charcters in the name): ')
    old_name = input("Enter The Exluded File Name's Charcters You Want To Replace From Name: ")
    new_name = input("Enter The Exluded File Name's New Charcters To Be Placed (leave it empty if just removing old charcaters): ")
    start_directory = os.curdir
    explore_subdirectories(start_directory,file_type,old_name,new_name)
    input("\nAny Key To Exit")
