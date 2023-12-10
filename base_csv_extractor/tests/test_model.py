from unittest.mock import sentinel
from dataclasses import asdict

from ..src.model import XYPair

from base_csv_extractor.src.csvextract import *

BUILDER_CLASSES: list[type[PairBuilder]] = [Series1Pair, Series2Pair, Series3Pair, Series4Pair]

class MockBuilder:
    def from_row(self, row):
        return row  # Or any particular behavior you're testing


def test_xypair():
    pair = XYPair(x=sentinel.X, y=sentinel.Y)
    assert pair.x == sentinel.X
    assert pair.y == sentinel.Y
    assert asdict(pair) == {"x": sentinel.X, "y": sentinel.Y}

def test_subset_extract_limit():
    builders = [cls() for cls in BUILDER_CLASSES]
    extractor = SubsetExtract(builders, limit=3)

    # Dummy input rows
    row = ["1", "2", "3", "4", "5", "6"]

    result = extractor.build_pair(row)

    assert len(result) == 3  # Should be limited to 3 pairs

def test_subset_extract_unlimited():
    builders = [cls() for cls in BUILDER_CLASSES]
    extractor = SubsetExtract(builders, limit=None)

    # Dummy input rows
    row = ["1", "2", "3", "4", "5", "6"]

    result = extractor.build_pair(row)

    assert len(result) == 4  # No limit, should return all pairs


