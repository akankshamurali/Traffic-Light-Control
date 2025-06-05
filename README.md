How It Works
Edge Detection: Uses Canny edge detection to identify visual features.
Baseline Subtraction: Subtracts emptyroad.jpeg from each lane image to isolate active traffic.
Traffic Scoring: Estimates congestion by summing the active edge pixels.
Signal Decision: The lane with the highest congestion gets the green light first.

Code Versions Overview
Version	Highlights

v1	Basic prototype with manual input, repetitive logic, and hard-coded thresholds

v2	Introduces functions, better readability, error handling

v3	Fully modular with CLI (argparse), structured logging, and unit testing support

Running the Final Version
python traffic_lightv3.py --image_dir ./images
Running Unit Tests
pytest test_traffic_light_control.py

Sample Images
You should include:
emptyroad.jpeg: no vehicles, used as baseline
lane2.jpg, lane3.jpg, lane4.jpg: traffic-heavy lanes for comparison

Requirements
Python 3.x
OpenCV (pip install opencv-python)
NumPy
Colorama
pytest (for running tests)

Future Work
Add real-time webcam/video input
Integrate vehicle detection with YOLO or SSD
Deploy on Jetson Nano for edge computing
