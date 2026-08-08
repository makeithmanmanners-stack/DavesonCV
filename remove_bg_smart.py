import cv2
import numpy as np

def smart_background_removal(input_path, output_path):
    # Load original image
    img = cv2.imread(input_path)
    if img is None:
        print("Error loading image")
        return

    h, w, c = img.shape

    # Convert to RGB and Gray
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Background threshold: pure/near white pixels
    # Background in the photo is pure white (>= 245)
    is_white = (gray >= 240).astype(np.uint8) * 255

    # Floodfill from the outer border ONLY to find outer background
    # Create mask padded by +2 for OpenCV floodFill
    ff_mask = np.zeros((h + 2, w + 2), np.uint8)

    # Floodfill from all 4 borders (top line, bottom line left/right corners, left line, right line)
    # Background starts at top/left/right outer edges
    for x in range(w):
        if is_white[0, x] == 255 and ff_mask[1, x + 1] == 0:
            cv2.floodFill(is_white, ff_mask, (x, 0), 255, loDiff=5, upDiff=5)
        if is_white[h - 1, x] == 255 and ff_mask[h, x + 1] == 0:
            cv2.floodFill(is_white, ff_mask, (x, h - 1), 255, loDiff=5, upDiff=5)

    for y in range(h):
        if is_white[y, 0] == 255 and ff_mask[y + 1, 1] == 0:
            cv2.floodFill(is_white, ff_mask, (0, y), 255, loDiff=5, upDiff=5)
        if is_white[y, w - 1] == 255 and ff_mask[y + 1, w] == 0:
            cv2.floodFill(is_white, ff_mask, (w - 1, y), 255, loDiff=5, upDiff=5)

    # Outer background is where ff_mask == 1
    outer_bg = (ff_mask[1:-1, 1:-1] == 1)

    # Create Alpha Channel: 0 for outer background, 255 for EVERYTHING ELSE (including white shirt!)
    alpha = np.ones((h, w), dtype=np.uint8) * 255
    alpha[outer_bg] = 0

    # Slight 3x3 GaussianBlur on alpha for clean smooth edges
    alpha_smooth = cv2.GaussianBlur(alpha, (3, 3), 0)

    # Combine BGR + Alpha into RGBA
    b, g, r = cv2.split(img)
    rgba = cv2.merge((b, g, r, alpha_smooth))

    cv2.imwrite(output_path, rgba)
    print(f"Smart background removal completed. Saved to {output_path}")

if __name__ == '__main__':
    src = "C:/Users/85293/.gemini/antigravity-ide/brain/5fa43e0a-ed25-472e-a06b-33dec1805eed/media__1786209324924.jpg"
    out = "c:/xampp2/htdocs/KhrtCv/static/images/daveson_portrait.png"
    smart_background_removal(src, out)
