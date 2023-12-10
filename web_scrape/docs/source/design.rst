Design Decisions
================

This section outlines key design decisions made during the development of the project.

- **New html_extract Module:**
  - Introduced to handle the download of HTML data and extraction of a table.

- **Download Class:**
  - Uses `urllib.request` to open the given URL and read the contents.
  - Utilizes `Beautiful Soup` to parse HTML, locate the table with the desired caption, and extract the body of the table.

- **PairBuilder Class Hierarchy:**
  - Four implementations, each appropriate for one of the four data series.
  - Handles the differences in data organization between the Wikipedia page and the CSV source file.

- **HTML Scraping with Beautiful Soup:**
  - Utilizes `find_all()` method to traverse the HTML structure and locate the desired table.

- **Error Handling:**
  - Encourages the addition of simple error reporting for potential issues with web service interaction.

This section provides insights into the rationale behind key design choices made in the project.
