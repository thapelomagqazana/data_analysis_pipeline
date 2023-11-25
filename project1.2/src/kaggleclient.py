import json
from pathlib import Path
import requests.auth


class RestAccess:
    def __init__(self, keyfile_path: Path):
        with keyfile_path.open() as keyfile:
            credentials = json.load(keyfile)
            self.auth = requests.auth.HTTPBasicAuth(
                credentials["username"], credentials["key"]
            )

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


if __name__ == "__main__":
    # Assuming you have the kaggle.json file in the Downloads folder
    keyfile_path = Path.home() / "data_analysis_pipeline" / "project1.2" / "kaggle.json"

    # Create an instance of the RestAccess class
    kaggle_client = RestAccess(keyfile_path)

    # Specify the owner and dataset_slug
    owner_slug = "carlmcbrideellis"
    dataset_slug = "data-anscombes-quartet"

    # Download the ZIP archive
    zip_file_path = kaggle_client.get_zip(owner_slug, dataset_slug)

    print(f"ZIP archive downloaded and saved at: {zip_file_path}")
