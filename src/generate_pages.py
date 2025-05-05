from markdown_blocks import *
from copy_static import *
import os

base_dir = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.join(base_dir, "../"))

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, "r", encoding="utf-8") as mdfile:
        mdtext = mdfile.read()
    with open(template_path, "r", encoding="utf-8") as templatefile:
        htmltemplate = templatefile.read()

    title = extract_title(mdtext)
    htmlnodes = markdown_to_html_node(mdtext)
    content = htmlnodes.to_html()
    html = htmltemplate.replace("{{ Title }}", title).replace("{{ Content }}", content)
    new_html = html.replace('href="/', f'href="{basepath}').replace('src="/', f'src="{basepath}')

    newpath = dest_path.replace(".md", ".html")
    os.makedirs(os.path.dirname(newpath), exist_ok=True)
    with open(newpath, "w", encoding="utf-8") as file:
        file.write(new_html)
    if os.path.exists(newpath) == True:
        print("page generated successfully")
    else:
        print("something happened")

def extend_path_to_root(path):
    return os.path.join(project_root, path)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    if os.path.exists(dir_path_content) == False:
        raise Exception("content directory not found")
    if os.path.exists(template_path) == False:
        raise Exception("template not found")
    if os.path.exists(dest_dir_path) == False:
        raise Exception("target directory not found")
    
    listdir = os.listdir(dir_path_content)
    for file in listdir:
        oldpath = os.path.join(dir_path_content, file)
        newpath = os.path.join(dest_dir_path, file)
        if os.path.isfile(oldpath) == True:
            generate_page(oldpath, template_path, newpath, basepath)
        else:
            os.mkdir(newpath)
            generate_pages_recursive(oldpath, template_path, newpath, basepath)
    