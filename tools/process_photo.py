from PIL import Image, ImageEnhance

img_path = r"C:\Users\JOASH\.gemini\antigravity\brain\8ad7f170-147c-4fcb-8ed4-53a319ca7f66\media__1784408478632.png"
img = Image.open(img_path).convert("L")  # Convert to grayscale

# Increase contrast
enhancer_contrast = ImageEnhance.Contrast(img)
img = enhancer_contrast.enhance(1.4)  # 40% more contrast

# Increase brightness slightly to make the paper background white
enhancer_brightness = ImageEnhance.Brightness(img)
img = enhancer_brightness.enhance(1.2)  # 20% brighter

# Save to public assets
out_path = r"C:\Users\JOASH\Desktop\CBC\offline-exam-app\public\assets\q6_activities.png"
img.save(out_path, "PNG")

print("Photo processed and saved to", out_path)
