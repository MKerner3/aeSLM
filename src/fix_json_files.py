import os
import glob
import re
import json

def replace_multiline_code_blocks(text):
    # Pattern to find triple-quoted strings
    pattern = re.compile(r'"""(.*?)"""', re.DOTALL)
    
    # Replace newlines within the triple-quoted strings with "\n"
    def replace_newlines(match):
        content = match.group(1).replace('\n', '\\n')
        return f'"{content}"'
    
    return pattern.sub(replace_newlines, text)

def fix_json_files(directory):
    json_files = glob.glob(os.path.join(directory, "*.json"))

    for json_file in json_files:
        try:
            with open(json_file, 'r', encoding='utf-8') as file:
                text = file.read()

            fixed_text = replace_multiline_code_blocks(text)

            with open(json_file, 'w', encoding='utf-8') as file:
                file.write(fixed_text)
            print(f"Processed {json_file}")
        except Exception as e:
            print(f"Failed to process {json_file}: {e}")

# Specify the directory containing your JSON files
directory_path = 'data/submissions-8/submissions-8'
fix_json_files(directory_path)