def write_file(file_name, file_content):
    with open(file_name, 'w') as file:
        file.write(file_content)

def append_file(file_name, append_content):
    with open(file_name, 'a') as file:
        file.write(append_content)

def read_file(file_name):
    with open(file_name, 'r') as file:
        file_content = file.read()
    return file_content
