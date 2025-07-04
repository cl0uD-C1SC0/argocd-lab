import os
import subprocess
from shutil import rmtree

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

def run_command(COMMAND):
    print(f" ℹ️  Running the following command: {COMMAND}")
    subprocess.run(
        COMMAND,
        shell=True,
    )

if __name__ == '__main__':
    print("Please, run init.py script located in the Root Directory of this repository")