from unittest.mock import sentinel
from dataclasses import asdict

import sys
sys.path.append("/home/thapelo/data_analysis_pipeline/project_1.1/src")
from model import XYPair


def test_xypair():
    pair = XYPair(x=sentinel.X, y=sentinel.Y)
    assert pair.x == sentinel.X
    assert pair.y == sentinel.Y
    assert asdict(pair) == {"x": sentinel.X, "y": sentinel.Y}