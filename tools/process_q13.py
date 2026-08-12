from PIL import Image

# Read image
img_path = r"C:\Users\JOASH\.gemini\antigravity-ide\brain\f792ea54-54ae-49d1-a665-6f5c779624ea\media__1785358395622.png"
img = Image.open(img_path).convert("L")  # Convert to grayscale

# Create a new RGBA image
out = Image.new("RGBA", img.size)

width, height = img.size
for y in range(height):
    for x in range(width):
        l = img.getpixel((x, y))
        
        a = 255 - l
        
        if a < 60:
            a = 0
        elif a > 150:
            a = 255
        else:
            a = int((a - 60) * (255.0 / (150 - 60)))
            
        out.putpixel((x, y), (0, 0, 0, a))

# Save to public assets
out_path = r"C:\Users\JOASH\Desktop\CBC\offline-exam-app\public\assets\kjsea_sst_2025_q13.png"
out.save(out_path, "PNG")

print("Image processed with transparency and saved to", out_path)
