import numpy as np
from traffic_lightv3 import compute_traffic_level

def test_compute_traffic_level_zero():
    # Test with an all-zero image (no traffic)
    dummy = np.zeros((10, 10), dtype=np.uint8)
    assert compute_traffic_level(dummy) == 0

def test_compute_traffic_level_nonzero():
    # Test with one bright pixel (simulated vehicle presence)
    dummy = np.zeros((10, 10), dtype=np.uint8)
    dummy[0][0] = 255
    assert compute_traffic_level(dummy) == 255
