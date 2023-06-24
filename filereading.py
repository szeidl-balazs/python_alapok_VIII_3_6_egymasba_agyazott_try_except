def read_file(file_name):
    try:
        file_name
        target_file = open(file_name)
        content = target_file.read()
        target_file.close()
        print(content)

    except OSError:
        print('Hiba a fájl kezelése közben!')

def get_file_name():
    return input('Which file you want to open? ')

read_file(get_file_name())