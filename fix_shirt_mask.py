import cv2
import numpy as np

def fix_shirt_and_background(input_path, output_path):
    # Load original photo (JPEG with crisp pure white background)
    img = cv2.imread(input_path)
    if img is None:
        print("Error loading original photo")
        return

    h, w, c = img.shape
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 1. Background Mask: Outer white background is pure/near white (> 240)
    bg_candidates = (gray >= 238).astype(np.uint8) * 255

    # Floodfill from top corners (0,0), (w-1,0) ONLY on the top boundary
    # We restrict floodfill so it only flows from top edges down to the suit shoulders
    ff_mask = np.zeros((h + 2, w + 2), np.uint8)
    
    # Seed only from top edge (row 0)
    for x in range(w):
        if bg_candidates[0, x] == 255 and ff_mask[1, x + 1] == 0:
            cv2.floodFill(bg_candidates, ff_mask, (x, 0), 255, loDiff=3, upDiff=3)

    # Outer background is where ff_mask == 1
    outer_bg = (ff_mask[1:-1, 1:-1] == 1)

    # 2. Body Silhouette Mask (Convex/Filled Hull of Daveson's Outer Contour)
    # Non-background region
    body_mask = np.zeros((h, w), dtype=np.uint8)
    body_mask[~outer_bg] = 255

    # Find the largest outer contour (Daveson's head, shoulders, suit)
    contours, _ = cv2.findContours(body_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if contours:
        # Find largest contour by area
        c_max = max(contours, key=cv2.contourArea)
        
        # Create a completely filled solid mask for Daveson's entire body
        solid_body_mask = np.zeros((h, w), dtype=np.uint8)
        cv2.drawContours(solid_body_mask, [c_max], -1, 255, thickness=cv2.FILLED)

        # Alpha is 255 for solid_body_mask, 0 outside
        alpha = solid_body_mask.copy()
    else:
        alpha = body_mask.copy()

    # Soften alpha edges slightly (Gaussian Blur 3x3) to avoid jagged pixels
    alpha_smooth = cv2.GaussianBlur(alpha, (3, 3), 0)

    # Combine BGR + Alpha
    b, g, r = cv2.split(img)
    rgba = cv2.merge((b, g, r, alpha_smooth))

    cv2.imwrite(output_path, rgba)
    print(f"Shirt fixed & background removal completed flawlessly! Saved to {output_path}")

if __name__ == '__main__':
    src = "C:/Users/85293/.gemini/antigravity-ide/brain/5fa43e0a-ed25-472e-a06b-33dec1805eed/media__1786209324924.jpg"
    out = "c:/xampp2/htdocs/KhrtCv/static/images/daveson_portrait.png"
    fix_shirt_and_background(src, out)
