import os
import subprocess
from shutil import rmtree, which

def verify_installed_tool():
    DEFAULT_PROGRAMS=["terraform", "aws", "ansible"]
    for program in DEFAULT_PROGRAMS:
        if not which(program):
            print(f" ❌  The following software wasn't found in the system")
            print(f"        {program.capitalize()}")
            print(" ⚠️  Install the required software and try again...\n")
            return False
    print(f" ✅ All softwares are ok!")
    return True
def change_directory(PATH):
    print(f" ℹ️  Switching directory to {PATH}")
    os.chdir(PATH)
    print(f" ✅ Successful to switch")

def create_directory(DIR_NAME):
    os.mkdir(DIR_NAME)
    print(f" ✅  Successful to create: {DIR_NAME}")

def remove_file(PATH):
    print(f" ℹ️  Removing the following file: {PATH}")
    os.rmdir(PATH)
    print(f" ✅ Sucessful to remove the following file: {PATH}")

def remove_directory(PATH):
    rmtree(PATH)
    print(f" ✅ Successful to remove the following directory: {PATH}")

def run_command(COMMAND, **kwargs):
    print(f" ℹ️  Running the following command: {COMMAND}")
    result = subprocess.run(
            COMMAND,
            **kwargs 
        )
    return result.stdout
    
if __name__ == '__main__':
    print("Please, run init.py script located in the Root Directory of this repository")