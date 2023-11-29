from csvextract import *
import argparse
from dataclasses import asdict
import json
import sys
import csv
from pathlib import Path
import logging

# Create and configure a logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Create a file handler
handler = logging.FileHandler("app.log")
handler.setLevel(logging.INFO)

# Create a console handler with a higher log level
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.ERROR)

# Create a formatter and set it for the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Add the handlers to the logger
logger.addHandler(handler)
logger.addHandler(console_handler)


def get_options(argv: list[str]) -> argparse.Namespace:
    """
    Parse command-line arguments and return an argparse.Namespace object.
    """
    defaults = argparse.Namespace(
        extract_class=Extract,
        series_classes=[Series1Pair, Series2Pair, Series3Pair, Series4Pair],
    )

    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--output", type=Path)
    parser.add_argument("--limit", type=int, help="Limit the number of the rows to be extracted")
    parser.add_argument("source", type=Path, nargs="*")

    return parser.parse_args(argv, defaults)


EXTRACT_CLASS: type[Extract] = Extract
SUBSET_CLASS: type[SubsetExtract] = SubsetExtract
BUILDER_CLASSES: list[type[PairBuilder]] = [Series1Pair, Series2Pair, Series3Pair, Series4Pair]


def findFile(argv: list[str]) -> str:
    file1 = ""
    for file in argv:
        if ".csv" == file[-4:]:
            file1 = file
    return file1


def findDirectory(argv: list[str]) -> str:
    directory = ""
    for dir1 in argv:
        if dir1[-4:] != ".csv" and not dir1.isdigit():
            directory = dir1

    return directory


def main(argv: list[str]) -> None:
    """
    Main function to extract data from CSV files and write to JSON files.
    """
    builders = [cls() for cls in BUILDER_CLASSES]

    options = get_options(argv)

    if not options.source:
        logger.error("No input file provided.")
        return  # Exit the function if no input file is provided

    if not options.output:
        logger.error("No output directory provided.")
        return  # Exit the function if no output directory is provided

    if options.limit is not None:
        # extracting data subsets using the --limit flag
        extractor = SUBSET_CLASS(builders, limit=options.limit)
    else:
        extractor = EXTRACT_CLASS(builders)

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

        print(f"Extracting data from {findFile(argv)}...")
        print(f"Data successfully extracted to {findDirectory(argv)}/Series_1.ndjson, {findDirectory(argv)}/Series_2.ndjson, and so on.")
        print("Extraction completed!")
    except FileNotFoundError as e:
        logger.error(f"File not found: {argv[-1]}")


if __name__ == "__main__":
    main(sys.argv[1:])
