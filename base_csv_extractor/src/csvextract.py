from base_csv_extractor.src.model import RawData, XYPair
from abc import ABC, abstractmethod
import logging

# logger = logging.getLogger(__name__)

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

    def __init__(self):
        # Initialize logging for this class
        # self.logger = logging.getLogger(__name__ + ".Series1Pair")
        super().__init__()

    def from_row(self, row: list[str]) -> RawData:
        """
        Create XYPair object from a row.
        """
        try:
            cls = self.target_class
            # the rest of the implementation...
            # return cls(arguments based on the value of row)
            return cls(row[0], row[1])
        except Exception as e:
            # self.logger.error(f"Error in {self.__class__.__name__} - from_row: {str(e)}")
            raise

class Series2Pair(PairBuilder):
    target_class = XYPair

    def __init__(self):
        # Initialize logging for this class
        # self.logger = logging.getLogger(__name__ + ".Series2Pair")
        super().__init__()

    def from_row(self, row: list[str]) -> RawData:
        try:
            cls = self.target_class
            # the rest of the implementation...
            # return cls(arguments based on the value of row)
            return cls(row[0], row[2])
        except Exception as e:
            # self.logger.error(f"Error in {self.__class__.__name__} - from_row: {str(e)}")
            raise

class Series3Pair(PairBuilder):
    target_class = XYPair

    def __init__(self):
        # Initialize logging for this class
        # self.logger = logging.getLogger(__name__ + ".Series3Pair")
        super().__init__()

    def from_row(self, row: list[str]) -> RawData:
        try:
            cls = self.target_class
            # the rest of the implementation...
            # return cls(arguments based on the value of row)
            return cls(row[0], row[3])
        except Exception as e:
            # self.logger.error(f"Error in {self.__class__.__name__} - from_row: {str(e)}")
            raise


class Series4Pair(PairBuilder):
    target_class = XYPair

    def __init__(self):
        # Initialize logging for this class
        # self.logger = logging.getLogger(__name__ + ".Series4Pair")
        super().__init__()

    def from_row(self, row: list[str]) -> RawData:
        try:
            cls = self.target_class
            # the rest of the implementation...
            # return cls(arguments based on the value of row)
            return cls(row[4], row[5])
        except Exception as e:
            # self.logger.error(f"Error in {self.__class__.__name__} - from_row: {str(e)}")
            raise

# Extract class that utilizes the PairBuilder
class Extract:
    """
    Extract class that utilizes the PairBuilder to build pairs from rows.
    """

    def __init__(self, builder: PairBuilder):
        self.builder = builder
        # self.logger = logging.getLogger("Extract")

    def build_pair(self, row: list[str]) -> list[RawData]:
        """
        Build RawData objects based on the given row.
        """
        try:
            return [bldr.from_row(row) for bldr in self.builder]
        except Exception as e:
            # self.logger.error(f"Error in Extract - build_pair: {str(e)}")
            raise

    def process_csv_content(self, csv_content):
        try:
            return [self.builder.from_row(row) for row in csv_content]
        except Exception as e:
            # self.logger.error(f"Error in Extract - process_csv_content: {str(e)}")
            raise

class SubsetExtract(Extract):
    def __init__(self, builders, limit):
        super().__init__(builders)
        self.limit = limit
        # self.logger = logging.getLogger("SubsetExtract")

    def build_pair(self, row):
        try:
            pairs = super().build_pair(row)
            return pairs[:self.limit] if self.limit is not None else pairs
        except Exception as e:
            # self.logger.error(f"Error in SubsetExtract - build_pair: {str(e)}")
            raise


EXTRACT_CLASS: type[Extract] = Extract
BUILDER_CLASSES: list[type[PairBuilder]] = [Series1Pair, ]


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

# if __name__ == "__main__":
#     test_series1pair()
