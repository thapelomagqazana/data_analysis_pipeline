========================
Design Principles Report
========================

Introduction
------------

This document presents the design philosophy, guiding principles, and choices made while developing the Data Acquisition Base Application.

Design Philosophy
------------------

The project adopts the following design principles:
- **Modularity:** Components are designed as independent modules for maintainability and reusability.
- **Abstraction:** Utilizes abstraction to separate concerns and enhance the flexibility of implementations.
- **Test-Driven Approach:** Embraces test-driven development for both unit and acceptance testing.

Guiding Principles
------------------

- **Single Responsibility:** Each module/class is designed to have a single responsibility.
- **Scalability:** The architecture is structured to accommodate future expansions or changes.
- **Ease of Testing:** Designs components to be easily testable.

Design Choices
--------------

1. **Model Module:**
    - Utilizes `dataclasses` to structure data (e.g., `XYPair`) effectively.
    - Introduces `PairBuilder` as an abstract class for diverse data pair strategies.

2. **CSV Extract Module:**
    - Implements the `Extract` class for data extraction using various `PairBuilder` subclasses.
    - Leverages multiple strategies to build `RawData` from CSV rows.

3. **User Interface (acquire.py):**
    - Employs command-line interface for user interaction and application execution.
    - Uses the `argparse` library for handling command-line arguments.

Conclusion
----------

The design principles and choices adopted in the Data Acquisition Base Application aim to ensure modularity, scalability, and ease of maintenance. This approach enables flexible and robust functionality while ensuring testability and extensibility of the system.
