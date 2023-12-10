Feature: HTML Extraction

  Scenario: Finds captioned table and extracts data
    Given an HTML page "example_1.html"
      """
      <!DOCTYPE html>
      <html>
      etc. with multiple tables.
      </html>
      """
    When we run the html extract command
    Then log has INFO line with "header: ['Keep this', 'Data']"
    And log has INFO line with "count: 1"