import cv2
import numpy as np
import time
from colorama import Fore


def preprocess_image(image_path):
    img = cv2.imread(image_path)
    if img is None:
        raise FileNotFoundError(f"Image not found: {image_path}")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (3, 3), 0)
    edges = cv2.Canny(blur, 100, 200)
    resized = cv2.resize(edges, (20, 10))
    return resized


def compute_difference(lane_img, base_img):
    return cv2.subtract(lane_img, base_img)


def compute_traffic_level(diff_img):
    return int(np.sum(diff_img[diff_img > 0]))


def simulate_traffic_lights(levels):
    print("\nEstimated Traffic Levels:")
    for i, level in enumerate(levels, start=1):
        print(f"Lane {i}: {level}")

    max_lane = np.argmax(levels) + 1
    print(f"\n{Fore.GREEN}Lane {max_lane} gets GREEN light first. Others remain RED.\n")
    for i in range(1, 5):
        if i == max_lane:
            print(f"{Fore.GREEN}Lane {i}: GREEN")
        else:
            print(f"{Fore.RED}Lane {i}: RED")
    time.sleep(10)


def main():
    try:
        base_img = preprocess_image("../images/emptyroad.jpeg")
        lane_imgs = [
            preprocess_image("../images/lane2.jpg"),
            preprocess_image("../images/lane3.jpg"),
            preprocess_image("../images/lane4.jpg"),
            preprocess_image("../images/lane4.jpg")  # Reusing lane4 for demo
        ]
        traffic_levels = [compute_traffic_level(compute_difference(lane, base_img)) for lane in lane_imgs]
        simulate_traffic_lights(traffic_levels)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
