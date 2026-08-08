import cv2
import numpy as np

def perfect_white_shirt_collar(input_path, output_path):
    # Load original image
    img = cv2.imread(input_path)
    if img is None:
        print("Error loading original photo")
        return

    h, w, c = img.shape
    b, g, r = cv2.split(img)

    # 1. Precise Outer Background Detection
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    is_bg_white = (gray >= 242).astype(np.uint8) * 255

    # FloodFill from top row ONLY to get outer background mask
    ff_mask = np.zeros((h + 2, w + 2), np.uint8)
    for x in range(w):
        if is_bg_white[0, x] == 255 and ff_mask[1, x + 1] == 0:
            cv2.floodFill(is_bg_white, ff_mask, (x, 0), 255, loDiff=2, upDiff=2)

    outer_bg_mask = (ff_mask[1:-1, 1:-1] == 1)

    # 2. Extract White Shirt Region (Enclosed inside neck & jacket lapels)
    # The shirt is high brightness (gray > 200) inside the torso area (y from 35% to 75%, x from 30% to 70%)
    torso_mask = np.zeros((h, w), dtype=bool)
    torso_mask[int(h * 0.35):int(h * 0.75), int(w * 0.30):int(w * 0.70)] = True

    # Shirt pixels: bright white areas inside the torso
    shirt_pixels = (gray >= 190) & torso_mask & (~outer_bg_mask)

    # Clean up shirt pixels using Morphological Closing to remove noise & fill any tiny holes
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    shirt_mask_cleaned = cv2.morphologyEx(shirt_pixels.astype(np.uint8) * 255, cv2.MORPH_CLOSE, kernel)

    # Brighten and enhance the white shirt colors to be crisp, pristine white while preserving natural shading
    enhanced_b = b.copy()
    enhanced_g = g.copy()
    enhanced_r = r.copy()

    # Boost shirt brightness & crispness
    boost_mask = shirt_mask_cleaned > 0
    enhanced_r[boost_mask] = np.clip(r[boost_mask].astype(np.float32) * 1.1 + 15, 0, 255).astype(np.uint8)
    enhanced_g[boost_mask] = np.clip(g[boost_mask].astype(np.float32) * 1.1 + 15, 0, 255).astype(np.uint8)
    enhanced_b[boost_mask] = np.clip(b[boost_mask].astype(np.float32) * 1.1 + 15, 0, 255).astype(np.uint8)

    # Re-merge channels
    img_enhanced = cv2.merge((enhanced_b, enhanced_g, enhanced_r))

    # 3. Create Smooth Alpha Channel (0 for outer background, 255 for full body)
    body_alpha = np.ones((h, w), dtype=np.uint8) * 255
    body_alpha[outer_bg_mask] = 0

    # Smooth the alpha mask edge with a refined 3x3 bilateral/Gaussian filter for clean edges
    alpha_smooth = cv2.GaussianBlur(body_alpha, (3, 3), 0)

    # Build final RGBA
    eb, eg, er = cv2.split(img_enhanced)
    rgba = cv2.merge((eb, eg, er, alpha_smooth))

    cv2.imwrite(output_path, rgba)
    print(f"Pristine white shirt collar perfected! Saved to {output_path}")

if __name__ == '__main__':
    src = "C:/Users/85293/.gemini/antigravity-ide/brain/5fa43e0a-ed25-472e-a06b-33dec1805eed/media__1786209324924.jpg"
    out = "c:/xampp2/htdocs/KhrtCv/static/images/daveson_portrait.png"
    perfect_white_shirt_collar(src, out)
