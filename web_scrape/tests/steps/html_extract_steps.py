import subprocess
import shlex
from pathlib import Path
from behave import given, when, then
from bs4 import BeautifulSoup
from web_scrape.src.html_extract import Download  # Adjust import path based on your directory structure

# Define a logger for testing purposes
class MockLogger:
    def info(self, message):
        print(f"INFO: {message}")

    def error(self, message):
        print(f"ERROR: {message}")

logger_instance = MockLogger()
download_instance = Download(logger_instance)

@given(u'an HTML page "{filename}"')
def step_given_html_page(context, filename):
    context.path = Path(filename)
    context.path.write_text(context.text)
    context.add_cleanup(context.path.unlink)

@when(u'we run the html extract command')
def step_when_run_html_extract_command(context):
    command = [
        'python', 'src/acquire.py',
        '-o', 'quartet',
        '--page', f'file://{str(context.path.absolute())}',
        '--caption', "Anscombe’s quartet"
    ]

    context.command = shlex.join(command)
    context.result = subprocess.run(command, capture_output=True, text=True)

@then(u'log has INFO line with "header: {expected_header}"')
def step_then_check_log_header(context, expected_header):
    assert f"header: {expected_header}" in context.result.stdout, f"Expected log not found in output:\n{context.result.stdout}"

@then(u'log has INFO line with "count: {expected_count}"')
def step_then_check_log_count(context, expected_count):
    assert f"count: {expected_count}" in context.result.stdout, f"Expected count not found in output:\n{context.result.stdout}"