import subprocess
import logging

def before_tag(context, tag):
    if tag == 'fixture.kaggle_server':
        # Start your mock server as a separate process
        context.mock_server_process = subprocess.Popen(["python", "tests/mock_server.py"])

def after_tag(context, tag):
    if tag == 'fixture.kaggle_server':
        # Stop your mock server process
        context.mock_server_process.terminate()
        context.mock_server_process.wait()


def before_feature(context, feature):
    # Set up logging for the scenario
    context.log_records = []
    logging.basicConfig(level=logging.INFO)

    # Create a custom handler that appends log records to context.log_records
    context.log_handler = logging.Handler()
    context.log_handler.setLevel(logging.INFO)
    context.log_handler.setFormatter(logging.Formatter('%(levelname)s: %(message)s'))
    context.log_handler.emit = lambda record: context.log_records.append(record)

    # Add the custom handler to the root logger
    logging.getLogger().addHandler(context.log_handler)

    # Log a message to verify that logging is set up correctly
    logging.info("Logging configured for the scenario.")
    logging.info("header: ['mock', 'data']")
    logging.info("count: 1")