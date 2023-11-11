from csvextract import *
import argparse
from dataclasses import asdict
import json
import sys
import csv
from pathlib import Path

def get_options(argv: list[str]) -> argparse.Namespace:
    """
    Parse command-line arguments and return an argparse.Namespace object.
    """
    defaults = argparse.Namespace(
        extract_class=Extract,
        series_classes=[Series1Pair, Series2Pair, Series3Pair, Series4Pair],
    )

    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--output", type=Path, default="data")
    parser.add_argument("source", type=Path, nargs="*")

    return parser.parse_args(argv, defaults)


EXTRACT_CLASS: type[Extract] = Extract
BUILDER_CLASSES: list[type[PairBuilder]] = [Series1Pair, Series2Pair, Series3Pair, Series4Pair]

def main(argv: list[str]) -> None:
    """
    Main function to extract data from CSV files and write to JSON files.
    """
    builders = [cls() for cls in BUILDER_CLASSES]
    extractor = EXTRACT_CLASS(builders)
    # etc.

    options = get_options(argv)

    targets = [
        options.output / "Series_1.ndjson",
        options.output / "Series_2.ndjson",
        options.output / "Series_3.ndjson",
        options.output / "Series_4.ndjson",
    ]

    try: 
        target_files = [
            target.open("w") for target in targets
        ]
        for source in options.source:
            with source.open() as source:
                rdr = csv.reader(source)
                for row in rdr:
                    for row, wtr in zip(extractor.build_pair(row), target_files):
                        wtr.write(json.dumps(asdict(row)) + "\n")
        
        for target in target_files:
            target.close()
    except FileNotFoundError:
        print("File not found: "+ argv[-1])

if __name__ == "__main__":
    main(sys.argv[1:])
