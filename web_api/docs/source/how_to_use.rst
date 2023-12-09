How to Use
----------

To effectively utilize the data acquisition application, follow these usage instructions:

1. **Local Extract:**
   If extracting data from a local CSV file, use the following command:
   `python src/acquire.py -o <output_directory> <input_csv_file>`

2. **Download and Extract:**
    To download and extract data from Kaggle, use the following command:
    `python src/acquire.py -k <kaggle_credentials_file> -o <output_directory> --zip <kaggle_dataset_reference>`

3. **Survey Data Sets:**
    For searching and listing Kaggle data sets, use the following command:
    `python src/acquire.py --search --maxSize <int> --filetype <file extension e.g csv> -k <kaggle_credentials_file>`