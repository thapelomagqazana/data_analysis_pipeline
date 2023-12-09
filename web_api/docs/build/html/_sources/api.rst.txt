Kaggle RESTful API
------------------

Overview
--------
The Kaggle platform offers a robust RESTful API, providing programmatic access to its vast dataset repositories, competitions, and user-related functionalities.

Key Functions
--------------
- **Dataset Access:** Retrieve metadata and data from a variety of available datasets.
- **Competition Interaction:** Access competition-related data, submit entries, and retrieve competition details.
- **User Account Operations:** Perform actions related to user accounts, including managing datasets, kernels, and competition participation.

Integration within the Project
------------------------------
The project leverages the Kaggle RESTful API for data acquisition, specifically focusing on extracting datasets, initially centered around the Anscombe's Quartet dataset.

API Token Authentication
------------------------
To interact with the Kaggle API, a unique API token is required. This token, stored in a separate file (kaggle.json), provides secure access to Kaggle's API endpoints.

API Endpoints and Requests
--------------------------
The project utilizes specific API endpoints to access datasets and related functionalities. These endpoints are accessed via HTTP requests (GET, POST, etc.) using Python's requests library.

Functionality Utilization
-------------------------
- **Dataset Metadata Retrieval:** API endpoints are used to retrieve JSON documents containing dataset summaries and metadata.
- **ZIP Archive Handling:** Access API endpoints to acquire ZIP archives housing dataset contents. Python's zipfile package is used to navigate and extract data from these archives.
