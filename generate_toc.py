import os

def generate_toc(root_dir="."):
    skip_dirs = {'.git', '__pycache__'}
    skip_files = {'.DS_Store'}

    toc = ["# Prompt Library Table of Contents", ""]

    for foldername, subfolders, filenames in os.walk(root_dir):
        rel_folder = os.path.relpath(foldername, root_dir)

        # Skip hidden/system folders
        if any(part.startswith('.') or part in skip_dirs for part in rel_folder.split(os.sep)):
            continue

        indent = "  " * rel_folder.count(os.sep)
        display_name = os.path.basename(foldername) or "."
        toc.append(f"{indent}- `{rel_folder}/`" if rel_folder != "." else "- `./`")

        for filename in sorted(filenames):
            if filename.startswith(".") or filename in skip_files or filename.endswith(".py") or filename.lower() == "readme.md":
                continue
            toc.append(f"{indent}  - `{filename}`")

    with open("TOC.md", "w", encoding="utf-8") as f:
        f.write("\n".join(toc))

    print("✅ TOC.md generated with contents.")

generate_toc()
