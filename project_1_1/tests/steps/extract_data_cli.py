"""
    Python Real-World Projects
    Project 1.1: Data Acquisition Base Application
"""

# These step definitions will "pass" a test run.
# These serve to confirm the Feature file syntax.

import subprocess
import os

def run_extraction_process(command_options):
    command = f"python src/acquire.py -o output_folder {command_options} co2-mm-mlo_csv.csv"
    process = subprocess.run(command, shell=True, capture_output=True, text=True)
    output = process.stdout
    return output


@given(u'the "Anscombe_quartet_data.csv" source file exists')
def step_impl(context):
    file_path = "Anscombe_quartet_data.csv"
    assert os.path.exists(file_path)

@given(u'the "quartet" directory exists')
def step_impl(context):
    directory_path = "quartet"
    assert os.path.exists(directory_path)


@when(u'we run command "python src/acquire.py -o quartet Anscombe_quartet_data.csv"')
def step_impl(context):
    command = "python src/acquire.py -o quartet Anscombe_quartet_data.csv"
    subprocess.run(command, shell=True)


@then(u'the "quartet/series_1.json" file exists')
def step_impl(context):
    file_path = "quartet/Series_1.ndjson"
    assert os.path.exists(file_path)

@then(u'the "quartet/Series_2.json" file exists')
def step_impl(context):
    file_path = "quartet/Series_2.ndjson"
    assert os.path.exists(file_path)

@then(u'the "quartet/series_3.json" file exists')
def step_impl(context):
    file_path = "quartet/Series_3.ndjson"
    assert os.path.exists(file_path)


@then(u'the "quartet/series_1.json" file starts with \'{"x": "10.0", "y": "8.04"}\'')
def step_impl(context):
    file_path = "quartet/Series_1.ndjson"
    with open(file_path, "r") as file:
        content = file.read(100)  # Assuming the content is in the first 100 characters
        print(content)
        assert '{"x": "10.0", "y": "8.04"}' in content

@given(u'the "Anscombe_quartet_data1.csv" source file does not exist')
def step_impl(context):
    file_path = "Anscombe_quartet_data1.csv"
    assert not os.path.exists(file_path)

@when(u'we run command "python src/acquire.py -o quartet Anscombe_quartet_data1.csv"')
def step_impl(context):
    command = "python src/acquire.py -o quartet Anscombe_quartet_data1.csv"
    subprocess.run(command, shell=True)

@then(u'the log contains "ERROR - File not found: Anscombe_quartet_data1.csv"')
def step_impl(context):
    log_path = "app.log"
    with open(log_path, "r") as log_file:
        log_content = log_file.read()
        assert "ERROR - File not found: Anscombe_quartet_data1.csv" in log_content

@given('an input file "{file}"')
def step_given_input_file(context, file):
    context.input_file = file

@when('the command is executed with the "{option}" option')
def step_when_command_executed(context, option):
    context.command_output = run_extraction_process(f"--limit {option}")

@when('the command is executed without a limit option')
def step_when_command_executed_no_limit(context):
    context.command_output = run_extraction_process("")

@then('the output file contains {count} data points')
def step_then_output_contains_count(context, count):
    output_count = len(context.command_output)  # Assuming the output content is stored
    print(output_count)
    if count.isdigit():
        assert output_count == int(count)
    else:
        assert output_count == 0