import cv2
import numpy as np

def force_fix_portrait(input_path, output_path):
    # Load original unedited uploaded photo (JPEG)
    img = cv2.imread(input_path)
    if img is None:
        print("Error: Could not load original photo")
        return

    h, w, c = img.shape
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Threshold for pure/near white background
    # Background in the original photo is pure white (>= 245)
    # White shirt inside the collar is near the center (x: 250 to 550, y: 350 to 750)
    
    # Create mask: initially all 255 (opaque)
    alpha = np.ones((h, w), dtype=np.uint8) * 255

    # Floodfill starting strictly from the outer border edges ONLY (top-left, top-right)
    # To find ONLY the outer background
    is_white = (gray >= 242).astype(np.uint8) * 255
    ff_mask = np.zeros((h + 2, w + 2), np.uint8)

    # Seed strictly at the top-left corner (0,0) and top-right corner (w-1, 0)
    cv2.floodFill(is_white, ff_mask, (0, 0), 255, loDiff=2, upDiff=2)
    cv2.floodFill(is_white, ff_mask, (w - 1, 0), 255, loDiff=2, upDiff=2)

    # Outer background is ONLY where floodfill reached from top corners
    outer_bg = (ff_mask[1:-1, 1:-1] == 1)

    # Set alpha = 0 ONLY on the outer background!
    alpha[outer_bg] = 0

    # Ensure EVERY SINGLE PIXEL inside Daveson's shirt & body area (y > 300) that is NOT outer_bg is 255
    # Combine original BGR + Alpha
    b, g, r = cv2.split(img)
    rgba = cv2.merge((b, g, r, alpha))

    cv2.imwrite(output_path, rgba)
    print(f"Force fix portrait successful! Saved to {output_path}")

if __name__ == '__main__':
    src = "C:/Users/85293/.gemini/antigravity-ide/brain/5fa43e0a-ed25-472e-a06b-33dec1805eed/media__1786209324924.jpg"
    out = "c:/xampp2/htdocs/KhrtCv/static/images/daveson_portrait.png"
    force_fix_portrait(src, out)
