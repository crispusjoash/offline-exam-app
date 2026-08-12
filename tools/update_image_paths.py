import os
import re

def update_image_paths(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.js'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Replace .png, .jpg, .jpeg with .webp
                updated_content = re.sub(r'\.png(?=["\'])', '.webp', content, flags=re.IGNORECASE)
                updated_content = re.sub(r'\.jpg(?=["\'])', '.webp', updated_content, flags=re.IGNORECASE)
                updated_content = re.sub(r'\.jpeg(?=["\'])', '.webp', updated_content, flags=re.IGNORECASE)
                
                if content != updated_content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(updated_content)
                    print(f"Updated paths in: {file}")

if __name__ == '__main__':
    data_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'src', 'data')
    update_image_paths(data_dir)
    print("Path updates complete.")
