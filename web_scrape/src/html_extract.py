from urllib.request import urlopen, HTTPError
from bs4 import BeautifulSoup, Tag
from urllib.error import URLError


class Download:
    def __init__(self, logger):
        """
        Initialize the Download object with a logger.

        Args:
        - logger: An instance of a logger for handling logs.
        """
        self.logger = logger

    def get_page(self, url: str) -> BeautifulSoup:
        """
        Fetch the HTML page content from the specified URL and parse it using BeautifulSoup.

        Args:
        - url (str): The URL to be fetched.

        Returns:
        - BeautifulSoup: The parsed HTML content.

        Raises:
        - HTTPError: If an HTTP error occurs during the request.
        - URLError: If a URL error occurs during the request.
        - Exception: For any other unexpected errors.
        """
        try:
            return BeautifulSoup(
                urlopen(url), "html.parser"
            )
        except HTTPError as e:
            self.logger.error(f"HTTP Error: {e.code} - {e.reason}")
            raise HTTPError(e)
        except URLError as e:
            self.logger.error(f"URL Error: {e.reason}")
            raise URLError(e)
        except Exception as e:
            self.logger.error(f"An unexpected error occurred: {e}")
            raise Exception(e)

    def find_table_caption(
            self,
            soup: BeautifulSoup,
            caption_text: str = "Anscombe's quartet"
    ) -> Tag:
        """
        Find a table with a specific caption in a BeautifulSoup object representing an HTML document.

        Args:
        - soup (BeautifulSoup): The BeautifulSoup object representing the HTML document.
        - caption_text (str): The text of the caption to search for.

        Returns:
        - Tag: The <table> tag with the specified caption.

        Raises:
        - RuntimeError: If no matching <table> tag is found.
        """
        for table in soup.find_all("table"):
            if table.caption:
                if table.caption.text.strip() == caption_text.strip():
                    return table
        raise RuntimeError(f"<table> with caption {caption_text!r} not found")