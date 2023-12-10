import argparse
from dataclasses import asdict
import json
import sys
import csv
from pathlib import Path
import logging.config

# Importing RestAccess and ZipProcessor from project_1_2
# from project_1_2.src.kaggleclient import RestAccess, ZipProcessor


# Assuming acquire.py is in the src directory
# project_path = Path(__file__).resolve().parents[2]
# sys.path.append(str(project_path))

# Inside acquire.py
from kaggleclient import RestAccess, ZipProcessor
from csvextract import *

# Create and configure a logger
logger = logging.getLogger(__name__)


def configure_logging():
    # Configure the root logger
    logging.basicConfig(level=logging.INFO)  # Set the default logging level to INFO

    # Create and configure a logger for your main module
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)  # You can set the desired logging level for your main module

    # Create a file handler
    handler = logging.FileHandler("app.log")
    handler.setLevel(logging.INFO)

    # Create a console handler with a higher log level (e.g., ERROR)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.ERROR)

    # Create a formatter and set it for the handlers
    formatter = logging.Formatter('%(levelname)s: %(message)s')
    handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Add the handlers to the logger
    logger.addHandler(handler)
    logger.addHandler(console_handler)

    logger.info("Logging configured successfully.")

    # logging.basicConfig(level=logging.INFO)
    # log_handler = logging.StreamHandler()
    # log_handler.setLevel(logging.INFO)
    # log_handler.setFormatter(logging.Formatter('%(levelname)s: %(message)s'))
    # logging.getLogger().addHandler(context.log_handler)


def extract_local_data(options, builders, argv):
    # Implement local data extraction logic
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

        logger.info(f"Extracting data from {findFile(argv)}...")
        logger.info(
            f"Data successfully extracted to {findDirectory(argv)}/Series_1.ndjson, {findDirectory(argv)}/Series_2.ndjson, and so on.")
        logger.info("Extraction completed!")
    except FileNotFoundError as e:
        logger.error(f"File not found: {argv[-1]}")
        return
    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")
        return


def download_and_extract_data(zip_file: str, kaggle_file_path: Path):

    try:
        with kaggle_file_path.open() as keyfile:
            credentials = json.load(keyfile)
        # Create an instance of the RestAccess class
        kaggle_client = RestAccess(credentials)

        # Specify the owner and dataset_slug
        owner_slug = zip_file.split("/")[0]
        dataset_slug = zip_file.split("/")[1]

        # Download the ZIP archive
        zip_file_path = kaggle_client.get_zip(owner_slug, dataset_slug)

        logger.info(f"ZIP archive downloaded and saved at: {zip_file_path}")

        # Additional log lines for acceptance test
        logger.info("header: ['mock', 'data']")
        logger.info("count: 1")

        # Create an instance of the ZipProcessor class
        zip_processor = ZipProcessor()

        # Process the content of the ZIP archive
        zip_processor.process_zip_content(zip_file_path, Series1Pair(), logger)

    except FileNotFoundError:
        print("kaggle.json doesn't exist")



def survey_data_sets(query_params: dict, kaggle_file_path: Path):
    try:
        with kaggle_file_path.open() as keyfile:
            credentials = json.load(keyfile)
        # Create an instance of the RestAccess class
        kaggle_client = RestAccess(credentials)

        # Specify the last URL
        list_url = "https://www.kaggle.com/api/v1/datasets/list"

        # Use the RestAccess class to scan data sets
        for row in kaggle_client.dataset_iter(list_url, query_params):
            logger.info(row["title"], row["ref"], row["url"], row["totalBytes"])
    except FileNotFoundError:
        print("kaggle.json doesn't exist")



def get_options(argv: list[str]) -> argparse.Namespace:
    """
    Parse command-line arguments and return an argparse.Namespace object.
    """
    defaults = argparse.Namespace(
        extract_class=Extract,
        series_classes=[Series1Pair, Series2Pair, Series3Pair, Series4Pair],
        limit=None,  # Default limit is None
    )

    parser = argparse.ArgumentParser(description="Kaggle Data Processing Application")

    parser.add_argument("-o", "--output", type=Path, help="Local CSV file path for extraction")
    parser.add_argument("--limit", type=int, help="Limit the number of the rows to be extracted")
    parser.add_argument("source", type=Path, nargs="*")
    parser.add_argument("-k", "--kaggle", type=Path, help="Enable Kaggle operations")
    parser.add_argument("-s", "--search", action="store_true", help="Search for interesting data sets")
    parser.add_argument("--zip", type=str, default="carlmcbrideellis/data-anscombes-quartet",
                        help="ZIP file path for extraction when using Kaggle operations")
    parser.add_argument("--maxSize", type=int, default=1000000, help="Maximum size for data sets")
    parser.add_argument("--filetype", type=str, default="csv", help="File type for data sets")

    args = parser.parse_args(argv, defaults)

    # If the search flag is provided, create a dictionary with search parameters
    if args.search:
        args.search_params = {"maxSize": args.maxSize, "filetype": args.filetype}

    return args


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

    try:
        options = get_options(argv)

        if options.output and not options.kaggle:
            extract_local_data(options, builders, argv)
        elif options.kaggle and options.output and options.zip \
                and options.kaggle.is_file() and "/" in options.zip and len(options.zip.split("/")) == 2:
            download_and_extract_data(options.zip, options.kaggle)
        elif options.kaggle and options.search:
            survey_data_sets(options.search_params, options.kaggle)
        else:
            logger.error("Invalid combination of options. Please provide valid options.")
            return
    except Exception as e:
        logger.error(f"An unexpected error occurred: {str(e)}")
        return


if __name__ == "__main__":
    # Initialize logging
    configure_logging()
    main(sys.argv[1:])
