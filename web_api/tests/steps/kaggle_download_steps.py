# Import necessary modules and classes
import subprocess
import logging
from unittest.mock import call
from pathlib import Path
import behave

@behave.given('proper keys are in "kaggle.json"')
def given_proper_keys(context):
    # Your implementation for providing proper keys in kaggle.json
    pass

@behave.when('we run the kaggle download command')
def when_run_kaggle_download_command(context):
    command = [
        'python',
        'web_api/src/acquire.py',
        '-k', str(Path.home() / 'data_analysis_pipeline' / 'project_1_2' / 'kaggle.json'),
        '-o', 'quartet',
        '--zip', 'carlmcbrideellis/data-anscombes-quartet'
    ]

    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        print("Command output:", result.stdout)
    except subprocess.CalledProcessError as e:
        print("Command failed. Exit code:", e.returncode)
        print("Command output (stderr):", e.stderr)
        raise e

# @behave.then('log has INFO line with "{text}"')
# def then_log_has_info_line_with_text(context, text):
#     # Your implementation for checking the log for INFO lines with specific text
#     actual_count = sum(1 for record in context.log_records if "INFO" in record.levelname and text in record.message)
#     print("Actual INFO lines count:", actual_count)
#     assert any("INFO" in record.levelname and text in record.message for record in context.log_records)

@behave.then('log has INFO line with "{text}"')
def then_log_has_info_line_with_text_count(context, text):
    # Assuming context.log_records contains log records captured during the scenario
    info_lines = [record.msg for record in context.log_records if record.levelname == 'INFO']
    count = info_lines.count(text)
    assert count == 1, f"Expected INFO line with '{text}' to appear once, but found {count} times."