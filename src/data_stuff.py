import os
import shutil
from pathlib import Path
from md_to_html import markdown_to_html_node
from htmlnode import *
from split_nodes import extract_title

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

def get_content(path):
    with open(path, "r") as f:
        return f.read()

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    from_content = get_content(from_path)
    template_content = get_content(template_path)

    html = markdown_to_html_node(from_content).to_html()
    title = extract_title(from_content)

    final_content = template_content.replace("{{ Title }}", title)
    final_content = final_content.replace("{{ Content }}", html)

    with open(dest_path, "w") as f:
        f.write(final_content)