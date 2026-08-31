import sys

from BlockNode import markdown_to_html_node
import os
import shutil

def main():
    # root = "static/"
    #
    # copy_static_to_public(root, "",True)
    #
    # generate_pages_recursive("content/", "template.html", "public/")
    basepath = sys.argv[1]

    if basepath == "":
        basepath = "content/"

    generate_pages_recursive("content/", "template.html", "docs/", basepath)

def copy_static_to_public(dir, curr_path, is_root = False):
    target = "public/"

    print(f"Dir: {dir}")
    print(f"Current Path: {curr_path}")
    print(f"Is Root: {is_root}")

    if is_root:
        print("Clearing Public...")
        shutil.rmtree(target)
        os.mkdir(target)

    print()

    files = os.listdir(dir)

    print(f"Files in {dir}: {files}")

    for file in files:
        print(f"{file} Is File: {os.path.isfile(dir + file)}")
        if os.path.isfile(dir + file):
            print(f"Copying {file}...")
            print(f"Destination Path: {target + curr_path}")
            print(f"Origin Path: {dir + file}")
            if not os.path.isdir(target + curr_path):
                print("Creating Destination Path...")
                os.mkdir(target + curr_path)
            shutil.copy(dir + file, target + curr_path)
            print(f"{file} Copied Sucessfully!")
            print("---------------------------------------------------")
        else:
            file = file + "/"
            print(f"Moving to {file}...")
            print(f"New Directory: {dir + file}")
            print(f"New Path: {curr_path + file}")
            print("*---------------------------------------------------*")
            copy_static_to_public(dir + file, curr_path + file)

def extract_title(markdown):
    lines = markdown.split("\n")

    for line in lines:
        if line[:2] == "# ":
            return line.strip().strip("# ")

    raise Exception("No Header Found")

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, "r") as file:
        markdown = file.read()
    with open(template_path, "r") as file:
        template = file.read()

    if from_path[-4:] != ".css":
        md_html = markdown_to_html_node(markdown)
        md_html = md_html.to_html()
        title = extract_title(markdown)

        page = template.replace("{{ Title }}", title).replace("{{ Content }}", md_html).replace('href="/', f'href="{basepath}/').replace('src="/', f'src="{basepath}/')
    else:
        page = markdown
        dest_path = dest_path.split(".")[0] + ".css"

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, "w") as f:
        f.write(page)

    print(f"Page written sucessfully.")

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    recursive_helper(basepath, dest_dir_path, template_path, dest_dir_path, dir_path_content, "", True)

def recursive_helper(basepath, dest, template, content, dir, curr_path, is_root = False):
    print(f"Dir: {dir}")
    print(f"Current Path: {curr_path}")
    print(f"Is Root: {is_root}")

    print()

    files = os.listdir(dir)

    print(f"Files in {dir}: {files}")

    for file in files:
        print(f"{file} Is File: {os.path.isfile(dir + file)}")
        if os.path.isfile(dir + file):
            print(f"Generating {file} as html...")
            print(f"Destination Path: {dest + curr_path}")
            print(f"Origin Path: {dir + file}")
            generate_page(dir + file, template, dest + curr_path + file.split(".")[0] + ".html", basepath)
            print(f"{file} Generated Sucessfully!")
            print("---------------------------------------------------")
        else:
            file = file + "/"
            print(f"Moving to {file}...")
            print(f"New Directory: {dir + file}")
            print(f"New Path: {curr_path + file}")
            print("*---------------------------------------------------*")
            recursive_helper(basepath, dest, template, content, dir + file, curr_path + file)


main()