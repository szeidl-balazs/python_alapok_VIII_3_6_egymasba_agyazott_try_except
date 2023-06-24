#file name opener function to open the file and print the content:
def read_file(file_name):
    try:
        file_name
        target_file = open(file_name)
        content = target_file.read()
        target_file.close()
        print(content)

    except OSError:
        print('Hiba a fájl kezelése közben!')


#file nam asker function to ask for file name and return it:
def get_file_name():
    return input('Which file you want to open? ')

#call the file opener function with the file name asker as argument:
read_file(get_file_name())