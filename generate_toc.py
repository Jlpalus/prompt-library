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

        # Add clickable folder link
        if rel_folder == ".":
            toc.append(f"{indent}- [`./`]({rel_folder}/)")
        else:
            toc.append(f"{indent}- [`{rel_folder}/`]({rel_folder}/)")

        # If there's a README.md, include first non-blank line
        readme_path = os.path.join(foldername, "README.md")
        if os.path.isfile(readme_path):
            with open(readme_path, "r", encoding="utf-8") as f:
                for line in f:
                    stripped = line.strip()
                    if stripped:
                        toc.append(f"{indent}  > {stripped}")
                        break

        # Add links for other files (but skip readme and script)
        for filename in sorted(filenames):
            if (
                filename.startswith(".") or 
                filename in skip_files or 
                filename.endswith(".py") or 
                filename.lower() == "readme.md"
            ):
                continue
            file_path = os.path.join(rel_folder, filename).replace("\\", "/")
            toc.append(f"{indent}  - [`{filename}`]({file_path})")

    with open("TOC.md", "w", encoding="utf-8") as f:
        f.write("\n".join(toc))

    print("✅ TOC.md generated with links and README descriptions.")

generate_toc()
