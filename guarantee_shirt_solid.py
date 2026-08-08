import cv2
import numpy as np

def guarantee_shirt_and_body_solid(input_path, output_path):
    img = cv2.imread(input_path)
    if img is None:
        print("Error loading original photo")
        return

    h, w, c = img.shape
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Threshold for background white (>= 242)
    is_white = (gray >= 242)

    alpha = np.zeros((h, w), dtype=np.uint8)

    # For each row, find the outermost non-white bounds (body span)
    for y in range(h):
        row_non_white = np.where(~is_white[y, :])[0]
        if len(row_non_white) > 0:
            x_min = row_non_white[0]
            x_max = row_non_white[-1]
            
            # Fill the entire span between x_min and x_max as 100% SOLID (255)
            alpha[y, x_min:x_max+1] = 255

    # Combine original BGR + Alpha
    b, g, r = cv2.split(img)
    rgba = cv2.merge((b, g, r, alpha))

    cv2.imwrite(output_path, rgba)
    print(f"Guaranteed 100% solid shirt & body! Saved to {output_path}")

if __name__ == '__main__':
    src = "C:/Users/85293/.gemini/antigravity-ide/brain/5fa43e0a-ed25-472e-a06b-33dec1805eed/media__1786209324924.jpg"
    out = "c:/xampp2/htdocs/KhrtCv/static/images/daveson_portrait.png"
    guarantee_shirt_and_body_solid(src, out)
