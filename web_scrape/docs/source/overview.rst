Overview
========

**Who**
------

The project is designed for developers and data enthusiasts who need to acquire data from a web page, specifically focusing on scenarios where the data is embedded in HTML markup. The target audience is individuals interested in building a command-line application using Python for web scraping.

**What**
-------

The project involves the creation of a Python command-line application that scrapes data from a web page. The application's primary goal is to extract information embedded in HTML markup, with a specific focus on tables marked up with the <table> tag and a unique <caption> tag. The data extraction process utilizes libraries such as `urllib.request` for making HTML requests and `Beautiful Soup` for parsing HTML content.

**When**
-------

The project is initiated to address the need for acquiring data from websites lacking a tidy API. It builds upon the concepts introduced in the previous project (web api) and extends the functionality to handle data embedded within HTML pages. The project timeline is flexible and accommodates the development and testing phases.

**Where**
--------

The application is intended to be run on the user's personal computer. It interacts with the Wikipedia website as a data source. The choice of the Wikipedia website is for demonstration purposes, and the application can be adapted to work with other websites by modifying the URL and caption parameters.

**Why**
-------

The motivation behind the project is to provide a solution for acquiring data from websites with irregular structures that lack a convenient API. By focusing on a specific use case (Anscombe’s Quartet data set), the project aims to keep the complexity manageable while demonstrating the principles of web scraping and data extraction. The command-line interface provides a flexible and accessible way for users to fine-tune the data gathering process.

**Definition of Done**
-----------------------

The project is considered complete when the command-line application successfully extracts the desired data from the specified web page, saves the results in the specified output directory, and provides a user-friendly interface with options for customization.

This overview document covers the essential "Who-What-When-Where-Why" aspects of the project, providing a clear understanding of the target audience, objectives, timeline, environment, and motivation behind the development.
