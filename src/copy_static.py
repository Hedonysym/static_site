import shutil
import os

# Base directory (relative to the script's location)
base_dir = os.path.dirname(__file__)

# Define paths relative to the script's location
public_path = os.path.join(base_dir, "../public/")
static_path = os.path.join(base_dir, "../static/")

def clear_public():
    if os.path.exists(public_path) == True:
        shutil.rmtree(public_path)
        os.mkdir(public_path)
        return os.path.exists(public_path)
    else:
        raise Exception("no dir at static_site/public/")

def copy_static_dir():
    if os.path.exists(static_path) == True:
        copy_dir_to_dir(static_path, public_path)
        return os.path.exists(public_path)
    else:
        raise Exception("no dir at static_site/static/")

def copy_dir_to_dir(old_path, target_path):
    listdir = os.listdir(old_path)
    for file in listdir:
        path = os.path.join(old_path, file)
        if os.path.isfile(path) == True:
           shutil.copy(path, target_path)
        else:
            new_path = os.path.join(target_path, file)
            if not os.path.exists(new_path):
                os.mkdir(new_path)
            copy_dir_to_dir(path, new_path)

def public_to_static():
    try:
        if clear_public() == True:
            print("public cleared!")
    except Exception as e:
        print(e)
        if not os.path.exists(public_path):
            os.mkdir(public_path)
    try:
        if copy_static_dir() == True:
            print("static copied to public!")
    except Exception as e:
        print(e)
        print("failed!")