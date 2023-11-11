from model import RawData, XYPair
from abc import ABC, abstractmethod

class PairBuilder(ABC):
    """
    Abstract base class for pair builders.
    """
    target_class = type[RawData]

    @abstractmethod
    def from_row(self, row: list[str]) -> RawData:
        """
        Abstract method to create RawData object from a row.
        """
        ...

class Series1Pair(PairBuilder):
    """
    PairBuilder implementation for Series 1.
    """
    target_class = XYPair

    def from_row(self, row: list[str]) -> RawData:
        """
        Create XYPair object from a row.
        """
        cls = self.target_class
        # the rest of the implementation...
        # return cls(arguments based on the value of row)
        return cls(row[0], row[1])

class Series2Pair(PairBuilder):
    target_class = XYPair

    def from_row(self, row: list[str]) -> RawData:
        cls = self.target_class
        # the rest of the implementation...
        # return cls(arguments based on the value of row)
        return cls(row[0], row[2])

class Series3Pair(PairBuilder):
    target_class = XYPair

    def from_row(self, row: list[str]) -> RawData:
        cls = self.target_class
        # the rest of the implementation...
        # return cls(arguments based on the value of row)
        return cls(row[0], row[3])

class Series4Pair(PairBuilder):
    target_class = XYPair

    def from_row(self, row: list[str]) -> RawData:
        cls = self.target_class
        # the rest of the implementation...
        # return cls(arguments based on the value of row)
        return cls(row[4], row[5])

# Extract class that utilizes the PairBuilder
class Extract:
    """
    Extract class that utilizes the PairBuilder to build pairs from rows.
    """
    def __init__(self, builder: PairBuilder):
        self.builder = builder

    def build_pair(self, row: list[str]) -> list[RawData]:
        """
        Build RawData objects based on the given row.
        """
        return [bldr.from_row(row) for bldr in self.builder]
    

EXTRACT_CLASS: type[Extract] = Extract
BUILDER_CLASSES: list[type[PairBuilder]] = [Series1Pair,]

def test_series1pair() -> None:
    """
    Test for Series1Pair implementation.
    """
    from unittest.mock import Mock, sentinel, call

    mock_raw_class = Mock()
    p1 = Series1Pair()
    p1.target_class = mock_raw_class
    xypair = p1.from_row([sentinel.X, sentinel.Y])
    assert mock_raw_class.mock_calls == [call(sentinel.X, sentinel.Y)]