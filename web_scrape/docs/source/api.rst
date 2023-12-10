API
===

This section provides details about the application's programming interface (API).

The application includes the following classes and functions:

- **Download Class:**
  - Responsible for downloading HTML data and extracting the table.
  - Uses urllib.request to make HTML requests.
  - Utilizes BeautifulSoup for parsing HTML.

- **PairBuilder Class Hierarchy:**
  - Four implementations, each suitable for one of the four data series.
  - Handles differences in data organization between the Wikipedia page and the CSV source file.

- **Functions:**
  - `get_page(url: str) -> BeautifulSoup`: Opens the URL as a file-like object and parses HTML.
  - `find_table_caption(soup: BeautifulSoup, caption_text: str) -> Tag`: Locates the desired table with a specific caption.

This API section provides insights into the internal structure and functionality of the application.
