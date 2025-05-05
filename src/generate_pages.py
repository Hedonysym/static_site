from markdown_blocks import *
from copy_static import *
import os

base_dir = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.join(base_dir, "../"))

def generate_page(page, template, dest):
    from_path = os.path.join(project_root, page)
    template_path = os.path.join(project_root, template)
    dest_path = os.path.join(project_root, dest)
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, "r", encoding="utf-8") as mdfile:
        mdtext = mdfile.read()
    with open(template_path, "r", encoding="utf-8") as templatefile:
        htmltemplate = templatefile.read()

    title = extract_title(mdtext)
    htmlnodes = markdown_to_html_node(mdtext)
    content = htmlnodes.to_html()
    new_html = htmltemplate.replace("{{ Title }}", title).replace("{{ Content }}", content)
    
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, "w", encoding="utf-8") as file:
        file.write(new_html)
    if os.path.exists(dest_path) == True:
        print("page generated successfully")
    else:
        print("something happened")
    