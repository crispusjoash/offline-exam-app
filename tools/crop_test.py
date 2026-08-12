from PIL import Image

def crop_and_save(img_path, coords, out_name):
    # coords: (left, top, right, bottom)
    img = Image.open(img_path)
    cropped = img.crop(coords)
    cropped.save(out_name)

# 1. Q1-5
img1 = r"C:\Users\JOASH\.gemini\antigravity\brain\8ad7f170-147c-4fcb-8ed4-53a319ca7f66\media__1784401454003.jpg"
crop_and_save(img1, (40, 200, 310, 380), "test_q2.png")
crop_and_save(img1, (350, 80, 620, 280), "test_q4.png")

# 2. Q6-13
img2 = r"C:\Users\JOASH\.gemini\antigravity\brain\8ad7f170-147c-4fcb-8ed4-53a319ca7f66\media__1784401556762.jpg"
crop_and_save(img2, (30, 90, 280, 310), "test_q6.png")
crop_and_save(img2, (320, 110, 560, 180), "test_q10.png")

# 3. Q14-20
img3 = r"C:\Users\JOASH\.gemini\antigravity\brain\8ad7f170-147c-4fcb-8ed4-53a319ca7f66\media__1784401671249.jpg"
crop_and_save(img3, (20, 380, 320, 520), "test_q16.png")
crop_and_save(img3, (340, 60, 640, 220), "test_q18.png")
crop_and_save(img3, (340, 430, 640, 620), "test_q19.png")

# 4. Q21-28
img4 = r"C:\Users\JOASH\.gemini\antigravity\brain\8ad7f170-147c-4fcb-8ed4-53a319ca7f66\media__1784401726004.jpg"
crop_and_save(img4, (30, 70, 300, 270), "test_q21.png")

print("Cropping complete.")
