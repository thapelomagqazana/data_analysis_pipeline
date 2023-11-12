Feature: Subset Extraction
  Scenario: Extract subset of data based on limit
    Given an input file "co2-mm-mlo_csv.csv"
    When the command is executed with the "--limit 3" option
    Then the output file contains 3 data points

  Scenario: Extract all data if limit is not specified
    Given an input file "co2-mm-mlo_csv.csv"
    When the command is executed without a limit option
    Then the output file contains all data points
