def file_read():
    with open('words.txt') as file:
        yield file.read().split()