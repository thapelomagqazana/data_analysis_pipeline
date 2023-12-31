from unittest.mock import Mock, sentinel, call
import pytest
from ..src.kaggleclient import RestAccess  # Replace 'your_module' with the actual module containing RestAccess


def test_rest_access(monkeypatch):
    mock_auth_class = Mock(
        name="Mocked HTTPBasicAuth class",
        return_value=sentinel.AUTH
    )
    monkeypatch.setattr("requests.auth.HTTPBasicAuth", mock_auth_class)
    mock_kaggle_json = {"username": sentinel.USERNAME, "key": sentinel.KEY}
    access = RestAccess(mock_kaggle_json)

    # Check that HTTPBasicAuth was instantiated with the correct parameters
    assert mock_auth_class.mock_calls == [
        call(sentinel.USERNAME, sentinel.KEY)
    ]

    # Check that credentials attribute is set correctly
    assert access.credentials == {
        "username": sentinel.USERNAME,
        "key": sentinel.KEY
    }
