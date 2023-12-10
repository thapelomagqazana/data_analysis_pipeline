Feature: Web Scraping

  Scenario: Downloading HTML content from a URL
    Given the user provides a valid URL "https://example.com"
    When the user initiates the download process
    Then the HTML content should be successfully retrieved
    And the HTML content should not be empty