Project Overview
----------------

Who
~~~
The project was led and created by Thapelo Magqazana. The primary stakeholders are analysts, decision-makers, and developers.

What
~~~~
The project aims to create a data acquisition tool leveraging the Kaggle platform's RESTful API. Specifically, it targets the retrieval of datasets, initially focusing on the Anscombe's Quartet dataset, offering a CLI application for data extraction and exploration.

When
~~~~
The project's timeline spans 11 Nov 2023 to --, with specific milestones and deliverables outlined in the project plan.

Where
~~~~
The development and implementation will occur within the Linux Operating System, with the resulting application intended for internal use within the organization.

Why
~~~
The primary objective is to provide analysts and decision-makers with a versatile and user-friendly tool for acquiring data. It offers a CLI interface to retrieve datasets, emphasizing the Anscombe's Quartet initially, with potential expansion to alternative datasets available on Kaggle.

Definition of Done (DoD)
-------------------------

CLI Application Development
~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Develop a command-line interface application (acquire.py) for data extraction from the Kaggle platform.
- Implement functionality to retrieve the Anscombe's Quartet dataset using specified commands.

API Integration and Authentication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Successfully integrate with the Kaggle RESTful API using a unique API token.
- Enable authentication for data retrieval, ensuring secure and authorized access.

Data Processing and Extraction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Extract relevant metadata fields from JSON documents to facilitate dataset identification.
- Implement functionality to navigate and extract data from ZIP archives using Python's zipfile package.

Security Measures
~~~~~~~~~~~~~~~~~
- Emphasize security practices by keeping the Kaggle API token file separate from the application's code.
- Make the file read-only and add it to .gitignore to prevent accidental exposure in code repositories.

Documentation and Testing
~~~~~~~~~~~~~~~~~~~~~~~~
- Maintain comprehensive documentation describing the application’s usage, features, and functionalities.
- Perform testing to ensure the application operates as expected under various scenarios and input conditions.
