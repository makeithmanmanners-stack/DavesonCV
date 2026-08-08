import cv2
import numpy as np
from PIL import Image

def remove_white_background(input_path, output_path):
    img = cv2.imread(input_path, cv2.IMREAD_UNCHANGED)
    if img is None:
        print("Failed to load image.")
        return

    # Convert to RGBA
    if img.shape[2] == 3:
        b, g, r = cv2.split(img)
        alpha = np.ones(b.shape, dtype=b.dtype) * 255
        img = cv2.merge((b, g, r, alpha))

    b, g, r, a = cv2.split(img)

    # Detect white/near-white pixels
    # Threshold for pure/near white background
    white_mask = (r > 235) & (g > 235) & (b > 235)

    # Use FloodFill from top-left and top-right corners to only remove connected background white
    height, width = img.shape[:2]
    bg_mask = np.zeros((height + 2, width + 2), np.uint8)

    # Convert to grayscale for floodFill
    gray = cv2.cvtColor(cv2.merge((b, g, r)), cv2.COLOR_BGR2GRAY)

    # Seed points at corners
    seed_points = [(0, 0), (width - 1, 0), (0, height - 1), (width - 1, height - 1)]
    for sp in seed_points:
        if gray[sp[1], sp[0]] > 230:
            cv2.floodFill(gray, bg_mask, sp, 255, loDiff=10, upDiff=10)

    # Connected background mask
    connected_bg = (bg_mask[1:-1, 1:-1] == 1) | white_mask

    # Smooth the alpha channel mask edges for anti-aliased clean boundary
    alpha_mask = np.ones((height, width), dtype=np.uint8) * 255
    alpha_mask[connected_bg] = 0

    # Soften edges slightly with GaussianBlur to avoid harsh pixelated edges
    alpha_mask = cv2.GaussianBlur(alpha_mask, (3, 3), 0)

    # Merge RGBA
    rgba = cv2.merge((b, g, r, alpha_mask))
    cv2.imwrite(output_path, rgba)
    print(f"Background removed successfully. Saved to {output_path}")

if __name__ == '__main__':
    src = "c:/xampp2/htdocs/KhrtCv/static/images/daveson_portrait.png"
    out = "c:/xampp2/htdocs/KhrtCv/static/images/daveson_portrait.png"
    remove_white_background(src, out)
