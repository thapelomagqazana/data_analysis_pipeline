Architecture
=============

This section provides an overview of the software architecture used in the project.

**Context Diagram**
--------------------

The context diagram illustrates the interaction between the user's personal computer and the Wikipedia website.

**Containers**
--------------

- **User's Personal Computer:**
  - Where the command-line application is executed.

- **Wikipedia Website:**
  - The source of the data, providing the HTML page to be scraped.

**Components**
--------------

- **html_extract Module:**
  - New module for capturing and parsing data.
  - Includes a `Download` class for downloading HTML data and extracting the table.
  - Incorporates a `PairBuilder` class hierarchy with four implementations for each data series.

**Code Design**
----------------

- **HTML Request:**
  - Utilizes `urllib.request` to make HTML requests.

- **HTML Parsing:**
  - Uses `BeautifulSoup` for parsing HTML content.

This architectural overview provides a high-level understanding of the project's software structure.
