"""
traffic_light_control.py

Simulates intelligent traffic light control based on visual traffic density analysis.
"""

import cv2
import numpy as np
import time
import os
import logging
import argparse
from colorama import Fore

# Configure logging
logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')

def preprocess_image(image_path):
    """Load and preprocess the image for edge detection."""
    img = cv2.imread(image_path)
    if img is None:
        raise FileNotFoundError(f"Image not found: {image_path}")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (3, 3), 0)
    edges = cv2.Canny(blur, 100, 200)
    resized = cv2.resize(edges, (20, 10))
    return resized

def compute_difference(lane_img, base_img):
    """Compute difference from base empty road image."""
    return cv2.subtract(lane_img, base_img)

def compute_traffic_level(diff_img):
    """Sum of all non-zero values to estimate traffic level."""
    return int(np.sum(diff_img[diff_img > 0]))

def simulate_traffic_lights(levels):
    """Simulate traffic light sequencing based on congestion."""
    logging.info("Estimated Traffic Levels:")
    for i, level in enumerate(levels, start=1):
        logging.info(f"Lane {i}: {level}")

    max_lane = np.argmax(levels) + 1
    print(f"\n{Fore.GREEN}Lane {max_lane} gets GREEN light first. Others remain RED.\n")
    for i in range(1, 5):
        if i == max_lane:
            print(f"{Fore.GREEN}Lane {i}: GREEN")
        else:
            print(f"{Fore.RED}Lane {i}: RED")
    time.sleep(10)

def main(image_dir):
    try:
        base_img = preprocess_image(os.path.join(image_dir, "emptyroad.jpeg"))
        lane_images = [
            "lane2.jpg",
            "lane3.jpg",
            "lane4.jpg",
            "lane4.jpg"  # Reusing for demo
        ]
        lane_imgs = [preprocess_image(os.path.join(image_dir, fname)) for fname in lane_images]
        traffic_levels = [compute_traffic_level(compute_difference(lane, base_img)) for lane in lane_imgs]
        simulate_traffic_lights(traffic_levels)
    except Exception as e:
        logging.error(f"Error occurred: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Traffic Light Controller based on image analysis")
    parser.add_argument('--image_dir', type=str, default="../images", help="Directory containing lane images")
    args = parser.parse_args()
    main(args.image_dir)
