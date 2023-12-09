from dataclasses import dataclass
from typing import TypeAlias

@dataclass
class XYPair:
    # Definition goes here
    x: str
    y: str

@dataclass
class SomeOtherStructure:
    # Some other definition, here
    x: list[str]
    y: list[str]

RawData: TypeAlias = XYPair | SomeOtherStructure