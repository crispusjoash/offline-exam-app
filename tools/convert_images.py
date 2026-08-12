import os
from pathlib import Path
try:
    from PIL import Image
except ImportError:
    import subprocess
    import sys
    subprocess.check_call([sys.executable, "-m", "pip", "install", "Pillow"])
    from PIL import Image

def optimize_images(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            ext = os.path.splitext(file)[1].lower()
            if ext in ['.png', '.jpg', '.jpeg']:
                file_path = os.path.join(root, file)
                webp_path = os.path.splitext(file_path)[0] + '.webp'
                
                try:
                    with Image.open(file_path) as img:
                        # Convert RGBA to RGB if saving to webp without alpha, but WebP supports alpha.
                        img.save(webp_path, 'webp', optimize=True, quality=80)
                    print(f"Converted: {file} -> {os.path.basename(webp_path)}")
                    
                    # Delete original
                    os.remove(file_path)
                    print(f"Deleted: {file}")
                except Exception as e:
                    print(f"Error converting {file_path}: {e}")

if __name__ == '__main__':
    assets_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'public', 'assets')
    optimize_images(assets_dir)
    print("Optimization complete.")
