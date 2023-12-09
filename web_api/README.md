# Data Acquisition With Web API Project

## Overview

This project involves the development of a command-line interface (CLI) application, named `acquire.py`, designed to facilitate data acquisition from Kaggle's RESTful web service. The application caters to data analysts, decision-makers, and users who need to acquire and analyze datasets from Kaggle.

### Definition of Done

#### Who
- **Stakeholders:**
  - Data analysts
  - Decision-makers
  - Users
  - Developers and maintainers

#### What
1. **Local Extract:**
   - Extract data from a local CSV file.

2. **Download and Extract:**
   - Download ZIP archives from Kaggle.
   - Extract data from a specified CSV member of the ZIP archive.

3. **Survey Data Sets:**
   - Search for interesting Kaggle data sets based on specified criteria.
   - List relevant metadata of the data sets.

#### When
- **Development:** Ongoing implementation and refinement of the CLI application.
- **Testing:** Rigorous testing to ensure functionality, reliability, and error handling.
- **Documentation:** Creation of comprehensive documentation, including code comments, README files, and Sphinx-generated documentation.

#### Where
- **Project Location:** `src` directory of the overall project structure.
- **Key Modules:**
  - `acquire.py`: Main CLI application for data acquisition.
  - `kaggle_client`: Module handling interactions with Kaggle's API.

#### Why
- **Motivation:**
  - Provide a practical solution for acquiring data from Kaggle.
  - Cater to users who need to gather data for analysis.
  - Focus on the Anscombe's Quartet dataset as a starting point.
  - Enhance user experience, flexibility, and efficiency in data acquisition.

### Project Structure

The project follows a modular architecture with the following components:

- **acquire.py:**
  The main CLI application responsible for coordinating data acquisition.

- **kaggle_client:**
  A module handling interactions with Kaggle's API.

- **... (Other modules):**
  Additional modules for specific functionalities.

The overall architecture adheres to best practices, promoting modularity, maintainability, and extensibility.

## API

For detailed information about the API and its functionalities, refer to the [API Documentation](api.rst).

## Design Decisions

This section outlines key design decisions made during the development of the project. It provides insights into the rationale behind certain choices, contributing to a better understanding of the project's structure and behavior. For more details, refer to [Design Decisions](design_decisions.rst).

## How to Test

To ensure the reliability and functionality of the project, follow these testing guidelines:

1. **Unit Tests:**
   Run unit tests using a testing framework such as pytest. Execute the following command:
   `pytest tests`
2. **Acceptance Tests:**
   Run acceptance tests using behave framework. Execute the following command:
   `behave tests`


## How to Use

To effectively utilize the data acquisition application, follow these usage instructions:

1. **Local Extract:**
If extracting data from a local CSV file, use the following command:
`python src/acquire.py -o <output_directory> <input_csv_file>`

2. **Download and Extract:**
To download and extract data from Kaggle, use the following command:
`python src/acquire.py -k <kaggle_credentials_file> -o <output_directory> --zip <kaggle_dataset_reference>`

3. **Survey Data Sets:**
For searching and listing Kaggle data sets, use the following command:
`python src/acquire.py --search --maxSize <int> --filetype <file_extension e.g csv> -k <kaggle_credentials_file>`


## Installation

1. Clone the repository:
```bash
git clone <repository_url>
cd <project_directory>
```
2. Install dependencies:
`pip install -r requirements.txt`

