import os
import shutil
from pathlib import Path

def copy_data(src, dest):
    for item in os.listdir(src):
        from_path = os.path.join(src, item)
        to_path = os.path.join(dest, item)
        
        if os.path.isdir(from_path):
            os.mkdir(to_path)
            print(f"Directory {to_path} created successfully")
            copy_data(from_path, to_path)
        else:
            shutil.copy(from_path, to_path)
            print(f"File {to_path} created successfully")

def copye(source, dest):
    if Path(dest).exists:
        shutil.rmtree(dest)
        print(f"Directory {dest} deleted successfully")
    os.mkdir(dest)
    print(f"Directory {dest} created successfully")

    copy_data(source, dest)