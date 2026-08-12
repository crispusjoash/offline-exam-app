from PIL import Image

def process(img_path, coords, out_name):
    # coords: (left, top, right, bottom)
    img = Image.open(img_path).convert("RGBA")
    img = img.crop(coords)
    
    # Enhance: Make background transparent and drawing black
    data = img.getdata()
    new_data = []
    for item in data:
        # average color
        avg = (item[0] + item[1] + item[2]) // 3
        # if it's light (grey paper), make it transparent
        if avg > 140:
            new_data.append((255, 255, 255, 0))
        else:
            # make the dark ink black
            new_data.append((0, 0, 0, 255))
    
    img.putdata(new_data)
    # Save to public/assets
    img.save(f"public/assets/{out_name}")

# 1. Q1-5
img1 = r"C:\Users\JOASH\.gemini\antigravity\brain\8ad7f170-147c-4fcb-8ed4-53a319ca7f66\media__1784401454003.jpg"
process(img1, (40, 200, 310, 380), "q2_roots.png")
process(img1, (350, 80, 620, 280), "q4_heart.png")

# 2. Q6-13
img2 = r"C:\Users\JOASH\.gemini\antigravity\brain\8ad7f170-147c-4fcb-8ed4-53a319ca7f66\media__1784401556762.jpg"
process(img2, (10, 80, 290, 360), "q6_activities.png")
process(img2, (310, 60, 560, 210), "q10_ball_ring.png")

# 3. Q14-20
img3 = r"C:\Users\JOASH\.gemini\antigravity\brain\8ad7f170-147c-4fcb-8ed4-53a319ca7f66\media__1784401671249.jpg"
process(img3, (20, 380, 320, 520), "q16_farmer.png")
process(img3, (340, 40, 640, 220), "q18_organic.png")
process(img3, (340, 430, 640, 620), "q19_livestock.png")

# 4. Q21-28
img4 = r"C:\Users\JOASH\.gemini\antigravity\brain\8ad7f170-147c-4fcb-8ed4-53a319ca7f66\media__1784401726004.jpg"
process(img4, (20, 60, 310, 270), "q21_farmer.png")

print("Images perfectly cropped and enhanced!")
