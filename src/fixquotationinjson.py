import os
import glob
import re

def replace_quotes_in_code_blocks(text):
    # Pattern to find the value of "code" keys, non-greedy match within double quotes
    pattern = re.compile(r'("code"\s*:\s*")(.*?)(\s*"\s*,)', re.DOTALL)
    
    # Function to replace double quotes with single quotes within the code block
    def replace_double_quotes(match):
        before_code = match.group(1)
        code_block = match.group(2)
        after_code = match.group(3)
        
        # Replace double quotes within the code block with single quotes
        code_block = code_block.replace('\\"', '"')  # Handle escaped quotes
        code_block = code_block.replace('"', "'")  # Replace double quotes with single quotes
        
        # Reconstruct the entire "code" key-value pair
        return f'{before_code}{code_block}{after_code}'
    
    return pattern.sub(replace_double_quotes, text)

def fix_json_files(directory):
    json_files = glob.glob(os.path.join(directory, "*.json"))

    for json_file in json_files:
        try:
            with open(json_file, 'r', encoding='utf-8') as file:
                text = file.read()

            fixed_text = replace_quotes_in_code_blocks(text)

            with open(json_file, 'w', encoding='utf-8') as file:
                file.write(fixed_text)
            print(f"Processed {json_file}")
        except Exception as e:
            print(f"Failed to process {json_file}: {e}")

# Specify the directory containing your JSON files
directory_path = 'data/submissions-8/submissions-8'
fix_json_files(directory_path)
