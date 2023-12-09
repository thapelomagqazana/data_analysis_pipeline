Feature: Downloading Kaggle Datasets

@fixture.kaggle_server
Scenario: Request for carlmcbrideellis/data-anscombes-quartet extracts file from ZIP archive
    Given proper keys are in "kaggle.json"
    When we run the kaggle download command
    Then log has INFO line with "header: ['mock', 'data']"
    And log has INFO line with "count: 1"
