import json
from pathlib import Path
import requests.auth
from zipfile import ZipFile
from project_1_1.src import *
from project_1_1.src.csvextract import Extract, Series1Pair


class RestAccess:
    def __init__(self, keyfile_path: Path):
        try:
            with keyfile_path.open() as keyfile:
                credentials = json.load(keyfile)
                self.auth = requests.auth.HTTPBasicAuth(
                    credentials["username"], credentials["key"]
                )
        except FileNotFoundError:
            print("kaggle.json doesn't exist")

    def make_request(self, method: str, endpoint: str, params=None, data=None):
        url = f"https://www.kaggle.com/api/v1/{endpoint}"
        # print(url)

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
    def process_zip_content(self, zip_file_path: Path, builder):
        with ZipFile(zip_file_path, "r") as zip_archive:
            # Assuming the CSV file is named in the ZIP archive
            csv_member_name = "Anscombe_quartet_data.csv"

            with zip_archive.open(csv_member_name) as csv_member:
                # Read and process the CSV content using the Extract class
                csv_content = [line.decode("utf-8").strip().split(",") for line in csv_member]
                extract_instance = Extract(builder)
                processed_data = extract_instance.process_csv_content(csv_content)

                # Print or use the processed data as needed
                print(processed_data)


if __name__ == "__main__":
    # Assuming you have the kaggle.json file in the Downloads folder
    keyfile_path = Path.home() / "data_analysis_pipeline" / "project_1_2" / "kaggle.json"

    # Create an instance of the RestAccess class
    kaggle_client = RestAccess(keyfile_path)

    # Specify the owner and dataset_slug
    owner_slug = "carlmcbrideellis"
    dataset_slug = "data-anscombes-quartet"

    # Download the ZIP archive
    zip_file_path = kaggle_client.get_zip(owner_slug, dataset_slug)

    print(f"ZIP archive downloaded and saved at: {zip_file_path}")

    # Create an instance of the ZipProcessor class
    zip_processor = ZipProcessor()

    # Process the content of the ZIP archive
    zip_processor.process_zip_content(zip_file_path, Series1Pair())
