===========================
Project Architecture Report
===========================

Introduction
------------

This document provides an overview of the architecture, design decisions, and technologies utilized in the Data Acquisition Base Application project.

System Architecture
-------------------

The system comprises the following major components:
- `src`: Holds the source code for the application.
- `tests`: Contains both unit and acceptance tests.
- `docs`: Includes project documentation.
- `requirements`: Lists all required dependencies for the project.

Design Decisions
----------------

Model Module:
- Houses classes such as `XYPair` and `SomeOtherStructure`.
- Defines abstract classes used for data extraction like `PairBuilder`.

CSV Extract Module:
- Implements the `Extract` class used to build `RawData` from CSV rows.
- Uses various `PairBuilder` subclasses to create `XYPair` instances.

User Interface (acquire.py):
- Command-line interface to interact with the application.
- Takes input file(s), processes data, and generates output files.

Technology Stack
----------------

- Python: Core language used for development.
- Libraries: Utilizes `argparse`, `json`, and `csv` for data processing.
- Testing: Employs `pytest` for unit tests and `behave` for acceptance tests.
- Tools: Relies on `pathlib` for file handling and `dataclasses` for defining data structures.

Significant Design Choices
--------------------------

- Use of `PairBuilder` abstract class: Allows multiple strategies for creating data pairs.
- Data structuring: Employed `dataclasses` for creating structured data types.
- Test-driven approach: Leveraged `pytest` for unit testing and `behave` for acceptance tests.
- File handling: Utilizes `pathlib` for handling file paths.

Conclusion
----------

This document outlines the architecture, design decisions, and technology stack for the Data Acquisition Base Application. It aims to provide insights into the choices made and technologies used in the development process.
