import os
import pytest
from file_io import write_file, append_file, read_file

@pytest.fixture
def temp_file_path(tmp_path):
    return os.path.join(tmp_path, "test_file.txt")

def test_write_file(temp_file_path):
    file_content = "This is a test content."
    write_file(temp_file_path, file_content)

    with open(temp_file_path, 'r') as file:
        assert file.read() == file_content

def test_append_file(temp_file_path):
    initial_content = "Initial content.\n"
    append_file(temp_file_path, initial_content)

    appended_content = "This is appended content."
    append_file(temp_file_path, appended_content)

    with open(temp_file_path, 'r') as file:
        assert file.read() == initial_content + appended_content

def test_read_file(temp_file_path):
    file_content = "This is the file content."
    with open(temp_file_path, 'w') as file:
        file.write(file_content)

    assert read_file(temp_file_path) == file_content
