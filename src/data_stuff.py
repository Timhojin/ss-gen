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
            copy_data(from_path, to_path)
        else:
            shutil.copy(from_path, to_path)

def copye(source, dest):
    if Path(dest).exists:
        shutil.rmtree(dest)
    os.mkdir(dest)

    copy_data(source, dest)

def get_content(path):
    with open(path, "r") as f:
        return f.read()

def generate_page(from_path, template_path, dest_path):
    
    from_content = get_content(from_path)
    template_content = get_content(template_path)

    html = markdown_to_html_node(from_content).to_html()
    title = extract_title(from_content)

    final_content = template_content.replace("{{ Title }}", title)
    final_content = final_content.replace("{{ Content }}", html)

    with open(dest_path, "w") as f:
        f.write(final_content)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    items = os.listdir(dir_path_content)
    for item in items:
        from_path = os.path.join(dir_path_content, item)
        to_path = os.path.join(dest_dir_path, item)
        
        if os.path.isdir(from_path):
            os.mkdir(to_path)
            generate_pages_recursive(from_path, template_path, to_path)
        else:
            generate_page(from_path, template_path, os.path.join(dest_dir_path, "index.html"))
