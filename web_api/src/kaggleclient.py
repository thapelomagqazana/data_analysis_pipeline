import json
from pathlib import Path
import requests.auth
from zipfile import ZipFile
from web_api.src.csvextract import Extract, Series1Pair
from typing import Iterator
import time


class RestAccess:
    """
        Class for accessing Kaggle API using RESTful methods.

        Attributes:
        - auth: HTTP authentication object for Kaggle API.

        Methods:
        - __init__(self, keyfile_path: Path): Constructor that initializes the authentication object.
        - dataset_iter(self, url: str, query: dict) -> Iterator[dict]: Iterator to retrieve datasets from Kaggle.
        - make_request(self, method: str, endpoint: str, params=None, data=None): Make a generic HTTP request to Kaggle API.
        - get_zip(self, owner_slug: str, dataset_slug: str): Download a dataset as a ZIP file.

        """
    def __init__(self, credentials: dict):
        """
        Initialize the RestAccess object.

        Parameters:
        - keyfile_path (Path): Path to the Kaggle API key file.
        """
        self.credentials = credentials
        self.auth = requests.auth.HTTPBasicAuth(
            self.credentials["username"], self.credentials["key"]
        )

    def dataset_iter(self, url: str, query: dict) -> Iterator[dict]:
        """
        Iterator to retrieve datasets from Kaggle.

        Parameters:
        - url (str): Kaggle API endpoint for dataset listing.
        - query (dict): Query parameters for filtering datasets.

        Returns:
        - Iterator[dict]: Iterator yielding dataset details.
        """
        page = 1
        while True:
            response = requests.get(url, params=query | {"page": str(page)}, auth=self.auth)

            if response.status_code == 200:
                details = response.json()
                print(details)
                if details:
                    yield from iter(details)
                    page += 1
                else:
                    break
            elif response.status_code == 429:
                # Too Many Requests
                # Pause and try again processing goes here...
                retry_after = int(response.headers.get("Retry-After", 1))
                print(f"Rate limited. Retrying after {retry_after} seconds.")
                time.sleep(retry_after)
            else:
                # Unexpected response
                # Error processing goes here...
                print(f"Unexpected response: {response.status_code}")
                break

    def make_request(self, method: str, endpoint: str, params=None, data=None):
        """
        Make a generic HTTP request to Kaggle API.

        Parameters:
        - method (str): HTTP method (GET, POST, etc.).
        - endpoint (str): Kaggle API endpoint.
        - params (dict): Query parameters for the request.
        - data: Data to be sent with the request.

        Returns:
        - dict or bytes: JSON response or binary content.
        """
        url = f"https://www.kaggle.com/api/v1/{endpoint}"

        response = requests.request(
            method, url, auth=self.auth, params=params, data=data
        )

        # print(response.content)

        if response.status_code != 200:
            raise Exception(f"Request failed with status code {response.status_code}")

        try:
            json_response = response.json()
            return json_response
        except json.JSONDecodeError:
            # If it's not JSON, assume it's binary content (e.g., ZIP file)
            return response.content

    def get_zip(self, owner_slug: str, dataset_slug: str):
        """
        Download a dataset as a ZIP file.

        Parameters:
        - owner_slug (str): Owner's username on Kaggle.
        - dataset_slug (str): Dataset's slug on Kaggle.

        Returns:
        - Path: Path to the downloaded ZIP file.
        """
        endpoint = f"datasets/download/{owner_slug}/{dataset_slug}"

        # Create a Path object for saving the ZIP file
        zip_path = Path(f"{owner_slug}_{dataset_slug}.zip")

        # Making a GET request to download the ZIP file
        response = self.make_request("GET", endpoint)

        # Saving the content to a local file
        with open(zip_path, "wb") as zip_file:
            if type(response) is bytes:
                zip_file.write(response)
            else:
                zip_file.write(response.content)

        return zip_path


# Separate client class or function
class ZipProcessor:
    """
    Class for processing content of ZIP files.

    Methods:
    - process_zip_content(self, zip_file_path: Path, builder, logger): Process the content of a ZIP file.
    """

    def process_zip_content(self, zip_file_path: Path, builder, logger):
        """
        Process the content of a ZIP file.

        Parameters:
        - zip_file_path (Path): Path to the ZIP file.
        - builder: Builder object for constructing processed data.
        - logger: Logger object for logging information.
        """
        with ZipFile(zip_file_path, "r") as zip_archive:
            # Assuming the CSV file is named in the ZIP archive
            csv_member_name = "Anscombe_quartet_data.csv"

            with zip_archive.open(csv_member_name) as csv_member:
                # Read and process the CSV content using the Extract class
                csv_content = [line.decode("utf-8").strip().split(",") for line in csv_member]
                extract_instance = Extract(builder)
                processed_data = extract_instance.process_csv_content(csv_content)

                # Print or use the processed data as needed
                logger.info(processed_data)


if __name__ == "__main__":
    # Assuming you have the kaggle.json file in the Downloads folder
    keyfile_path = Path.home() / "data_analysis_pipeline" / "web_api" / "kaggle.json"

    try:
        with keyfile_path.open() as keyfile:
            credentials = json.load(keyfile)

            # Create an instance of the RestAccess class
            kaggle_client = RestAccess(credentials)

            # # Specify the last URL
            # list_url = "https://www.kaggle.com/api/v1/datasets/list"
            #
            # # Define query parameters based on your requirements
            # query_params = {
            #     "maxSize": "1000000",
            #     "filetype": "csv"
            # }
            #
            # # Use the RestAccess class to scan data sets
            # for row in kaggle_client.dataset_iter(list_url, query_params):
            #     print(row["title"], row["ref"], row["url"], row["totalBytes"])

            # Specify the owner and dataset_slug
            owner_slug = "carlmcbrideellis"
            dataset_slug = "data-anscombes-quartet"

            # Download the ZIP archive
            zip_file_path = kaggle_client.get_zip(owner_slug, dataset_slug)

            print(f"ZIP archive downloaded and saved at: {zip_file_path}")

            # Create an instance of the ZipProcessor class
            zip_processor = ZipProcessor()

            # Process the content of the ZIP archive
            # zip_processor.process_zip_content(zip_file_path, Series1Pair())

    except FileNotFoundError:
        print("kaggle.json doesn't exist")


